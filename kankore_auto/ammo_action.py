def ammo_action(app):
    # 弾薬ボタンがクリックされたときの処理を記述
    app.update_display(current_task="弾薬実行中")

    # タイマーが終了したかどうかを確認
    if not app.timer.timer_running:
        app.update_display(next_time="タイマー終了")
        app.start_action()  # タイマーが終了している場合、スタートボタンと同じ処理を実行
