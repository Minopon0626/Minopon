import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import random

# カードクラス
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"{self.color} {self.number}"

    def matches(self, other_card):
        return self.color == other_card.color or self.number == other_card.number

# デッキクラス
class Deck:
    def __init__(self):
        colors = ['赤', '青', '緑', '黄色']  # カードの色
        numbers = list(range(10))  # カードの数字
        # 各色、各数字のカードを2枚ずつ作成
        self.cards = [Card(color, number) for color in colors for number in numbers for _ in range(2)]
        random.shuffle(self.cards)  # カードをシャッフル

    def draw(self, count=1):
        # カードを引く（リストから取り出す）
        return [self.cards.pop() for _ in range(count)]

    def add_to_bottom(self, card):
        # カードを山札の一番下に追加し、シャッフル
        self.cards.insert(0, card)
        random.shuffle(self.cards)

# サーバークラス
class Server:
    def __init__(self, gui):
        self.deck = Deck()
        self.players = []
        self.player_hands = {}  # 各プレイヤーの手札を保存
        self.client_sockets = []
        self.top_card = self.deck.draw()[0]
        self.lock = threading.Lock()
        self.game_started = False
        self.gui = gui
        self.current_turn = 0  # 現在のプレイヤーのターンを示すインデックス
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 12345))
        self.server_socket.listen(5)
        self.gui.log_message("サーバーがポート12345で待機中...")

    def accept_connections(self):
        """クライアントからの接続を待機し、接続があればプレイヤーリストに追加"""
        while True:
            client_socket, client_address = self.server_socket.accept()
            player_name = client_socket.recv(1024).decode('utf-8')
            self.players.append(player_name)
            self.client_sockets.append(client_socket)
            self.player_hands[player_name] = []  # プレイヤーの手札を空で初期化
            self.gui.log_message(f"{player_name} が接続しました: {client_address}")
            self.gui.update_player_list(self.players, self.current_turn)  # プレイヤーリストの更新
            client_socket.send("プレイヤーが接続されました。ゲーム開始を待ってください。".encode('utf-8'))

    def handle_client(self, client_socket, player_name, player_index):
        """クライアントごとのゲーム処理"""
        while not self.game_started:
            threading.Event().wait(2)

        player_hand = self.deck.draw(7)
        self.player_hands[player_name] = player_hand  # プレイヤーの手札を保存
        self.gui.update_player_list(self.players, self.current_turn)  # プレイヤーリストの更新
        client_socket.send(f"最初の場のカードは {self.top_card}".encode('utf-8'))

        while True:
            try:
                if player_index == self.current_turn:
                    client_socket.send("あなたのターンです".encode('utf-8'))
                    client_socket.send(f"あなたの手札: {[str(card) for card in player_hand]}".encode('utf-8'))
                    message = client_socket.recv(1024).decode('utf-8')

                    if message.startswith('play'):
                        card_index = int(message.split()[1])
                        card_to_play = player_hand[card_index]

                        if card_to_play.matches(self.top_card):
                            with self.lock:
                                self.top_card = card_to_play
                            player_hand.pop(card_index)
                            self.gui.update_player_list(self.players, self.current_turn)  # プレイヤーリストの更新
                            self.broadcast(f"カード {card_to_play} を場に出しました", exclude_socket=None)
                            self.broadcast(f"場のカードは {self.top_card} です", exclude_socket=None)
                            if not player_hand:
                                client_socket.send(f"{player_name} が勝利しました！".encode('utf-8'))
                                break
                        else:
                            client_socket.send("出せないカードです".encode('utf-8'))

                    elif message == 'draw':
                        drawn_card = self.deck.draw()[0]
                        player_hand.append(drawn_card)
                        self.gui.update_player_list(self.players, self.current_turn)  # プレイヤーリストの更新
                        client_socket.send(f"{drawn_card} を引きました".encode('utf-8'))

                    # ターンを次のプレイヤーに渡す
                    with self.lock:
                        self.current_turn = (self.current_turn + 1) % len(self.players)
                        self.gui.update_player_list(self.players, self.current_turn)  # ターンが変わったらリストを更新

                else:
                    client_socket.send("他のプレイヤーのターンです".encode('utf-8'))
                    threading.Event().wait(2)  # 他プレイヤーが操作する時間待機

            except:
                self.client_sockets.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, exclude_socket=None):
        """すべてのクライアントにメッセージを送信（除外されたソケットを除く）"""
        for client_socket in self.client_sockets:
            if client_socket != exclude_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except:
                    self.client_sockets.remove(client_socket)
                    client_socket.close()

    def start_game(self):
        """ゲームを開始"""
        self.game_started = True
        self.gui.log_message("ゲームが開始されました！")

        # プレイヤーをランダムに並び替え
        random.shuffle(self.players)
        self.gui.update_player_list(self.players, self.current_turn)

        for client_socket in self.client_sockets:
            client_socket.send("ゲームが開始されました！".encode('utf-8'))

        for player_name, client_socket in zip(self.players, self.client_sockets):
            thread = threading.Thread(target=self.handle_client, args=(client_socket, player_name, self.players.index(player_name)))
            thread.start()

# GUIクラス
class ServerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("カードゲームサーバー")

        # 左側のログ表示用スクロールテキストウィジェット
        self.log_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.log_area.grid(row=0, column=0, padx=10, pady=10)

        # 右側のプレイヤーリスト表示用
        self.player_list_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=30, height=20)
        self.player_list_area.grid(row=0, column=1, padx=10, pady=10)

        # ゲーム開始ボタン
        self.start_button = tk.Button(self.root, text="ゲーム開始", command=self.start_game)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

        self.server = Server(self)

        # 接続を待機するスレッドを開始
        self.connection_thread = threading.Thread(target=self.server.accept_connections)
        self.connection_thread.start()

    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def update_player_list(self, players, current_turn):
        """プレイヤーリストを更新し、誰のターンかを表示"""
        self.player_list_area.delete(1.0, tk.END)
        for index, player in enumerate(players):
            turn_indicator = "＞" if index == current_turn else "  "
            hand_size = len(self.server.player_hands.get(player, []))
            self.player_list_area.insert(tk.END, f"{turn_indicator} {player}: 手札 {hand_size}枚\n")
        self.player_list_area.see(tk.END)

    def start_game(self):
        """ゲーム開始ボタンが押された時にゲームを開始"""
        if len(self.server.players) >= 2:  # 最低2人のプレイヤーが必要
            self.server.start_game()
        else:
            self.log_message("最低2人のプレイヤーが必要です")

    def run(self):
        """GUIを開始"""
        self.root.mainloop()

if __name__ == "__main__":
    gui = ServerGUI()
    gui.run()
