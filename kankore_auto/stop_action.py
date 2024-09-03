def stop_action(app):
    # タイマーを停止する処理（ここではシンプルな例として表示のみ）
    app.update_display(current_task="タイマー停止中", next_time="タイマー停止")
    app.start_button.config(state="normal")  # スタートボタンを再度有効にする
    app.stop_button.config(state="disabled")  # ストップボタンを無効にする
