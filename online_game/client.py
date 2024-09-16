import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# クライアントのGUIクラス
class ClientGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("カードゲームクライアント")

        # プレイヤー名入力用のウィジェット
        tk.Label(self.root, text="プレイヤー名").grid(row=0, column=0, padx=10, pady=5)
        self.player_name_entry = tk.Entry(self.root)
        self.player_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # 接続ボタン
        self.connect_button = tk.Button(self.root, text="接続", command=self.connect_to_server)
        self.connect_button.grid(row=0, column=2, padx=10, pady=5)

        # ゲームログ用のスクロールテキストウィジェット
        self.log_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.log_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # プレイするカードのインデックス入力用ウィジェット
        tk.Label(self.root, text="カードのインデックス (play [index])").grid(row=2, column=0, padx=10, pady=5)
        self.card_index_entry = tk.Entry(self.root)
        self.card_index_entry.grid(row=2, column=1, padx=10, pady=5)

        # プレイボタン
        self.play_button = tk.Button(self.root, text="カードをプレイ", command=self.play_card)
        self.play_button.grid(row=2, column=2, padx=10, pady=5)
        self.play_button.config(state=tk.DISABLED)

        # カードを引くボタン
        self.draw_button = tk.Button(self.root, text="カードを引く", command=self.draw_card)
        self.draw_button.grid(row=3, column=1, padx=10, pady=5)
        self.draw_button.config(state=tk.DISABLED)

        self.client_socket = None
        self.receive_thread = None
        self.is_my_turn = False  # 自分のターンかどうかを管理するフラグ

    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def connect_to_server(self):
        player_name = self.player_name_entry.get()
        if not player_name:
            messagebox.showerror("エラー", "プレイヤー名を入力してください")
            return

        try:
            # サーバーに接続
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(('127.0.0.1', 12345))
            self.client_socket.send(player_name.encode('utf-8'))

            # 接続が成功した場合、ログに表示
            self.log_message("サーバーに接続しました！")

            # サーバーからのメッセージを受信するスレッドを開始
            self.receive_thread = threading.Thread(target=self.receive_messages)
            self.receive_thread.start()

            # ボタンの有効化
            self.connect_button.config(state=tk.DISABLED)
            self.player_name_entry.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("接続エラー", f"サーバーへの接続に失敗しました: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.log_message(message)

                    # 自分のターンの場合、ボタンを有効化
                    if "あなたのターンです" in message:
                        self.play_button.config(state=tk.NORMAL)
                        self.draw_button.config(state=tk.NORMAL)
                        self.is_my_turn = True
                    elif "他のプレイヤーのターンです" in message:
                        self.play_button.config(state=tk.DISABLED)
                        self.draw_button.config(state=tk.DISABLED)
                        self.is_my_turn = False
                else:
                    break
            except:
                self.log_message("サーバーとの接続が切れました")
                self.client_socket.close()
                break

    def play_card(self):
        if not self.is_my_turn:
            messagebox.showerror("エラー", "自分のターンではありません")
            return

        card_index = self.card_index_entry.get()
        if not card_index.isdigit():
            messagebox.showerror("エラー", "有効なカードのインデックスを入力してください")
            return

        try:
            self.client_socket.send(f"play {card_index}".encode('utf-8'))
            self.card_index_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("エラー", f"カードのプレイに失敗しました: {e}")

    def draw_card(self):
        if not self.is_my_turn:
            messagebox.showerror("エラー", "自分のターンではありません")
            return

        try:
            self.client_socket.send("draw".encode('utf-8'))
        except Exception as e:
            messagebox.showerror("エラー", f"カードを引くことに失敗しました: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = ClientGUI()
    gui.run()
