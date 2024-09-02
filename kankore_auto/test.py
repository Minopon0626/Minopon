import tkinter as tk

def create_table_row(parent, label_text, value_text):
    # 1列目はグレーの背景、2列目は白の背景
    label_frame = tk.Frame(parent, bg="lightgray", padx=10, pady=5, borderwidth=1, relief="solid")
    label = tk.Label(label_frame, text=label_text, bg="lightgray", font=("Arial", 12))
    label.pack(fill="both", expand=True)

    value_frame = tk.Frame(parent, bg="white", padx=10, pady=5, borderwidth=1, relief="solid")
    value_label = tk.Label(value_frame, text=value_text, bg="white", font=("Arial", 12))
    value_label.pack(fill="both", expand=True)
    
    return label_frame, value_frame

def main():
    # ウィンドウを作成
    root = tk.Tk()
    root.title("情報表示アプリ")  # ウィンドウのタイトルを設定
    root.geometry("400x200")  # ウィンドウのサイズを設定
    root.configure(bg="lightgray")  # ウィンドウの背景色を薄いグレーに設定

    # テーブルの行を作成
    row1_label, row1_value = create_table_row(root, "現在すること", "表示内容A")
    row2_label, row2_value = create_table_row(root, "次の稼働時間まで", "表示内容B")
    row3_label, row3_value = create_table_row(root, "次クリックする場所", "表示内容C")
    
    # 各行を表示
    row1_label.grid(row=0, column=0, sticky="nsew")
    row1_value.grid(row=0, column=1, sticky="nsew")
    
    row2_label.grid(row=1, column=0, sticky="nsew")
    row2_value.grid(row=1, column=1, sticky="nsew")
    
    row3_label.grid(row=2, column=0, sticky="nsew")
    row3_value.grid(row=2, column=1, sticky="nsew")

    # グリッドのカラムのウェイトを設定して、列幅を均等にする
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # グリッドの行のウェイトを設定して、行高さを均等にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)

    # ウィンドウを表示
    root.mainloop()

if __name__ == "__main__":
    main()
