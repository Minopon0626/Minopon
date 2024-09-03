def stop_action(app):
    # 表示内容を元に戻す（例として元の値を設定）
    app.update_display(current_task="表示内容A", next_time="表示内容B", next_click="表示内容C")

    # 「スタート」ボタンを有効にし、「ストップ」ボタンを無効にする
    app.start_button.config(state="normal")
    app.stop_button.config(state="disabled")
