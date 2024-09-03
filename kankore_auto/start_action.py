def start_action(app):
    # 新しい表示内容を設定
    app.update_display(current_task="更新された表示内容A", next_time="更新された表示内容B", next_click="更新された表示内容C")

    # 「スタート」ボタンを無効にし、「ストップ」ボタンを有効にする
    app.start_button.config(state="disabled")
    app.stop_button.config(state="normal")
