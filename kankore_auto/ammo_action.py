def ammo_action(app):
    # 弾薬ボタンがクリックされたときの処理を記述
    app.update_display(current_task="弾薬実行中")

    # いずれかのタイマーが終了したかどうかを確認
    if not app.timer.timer_running_a or not app.timer.timer_running_b or not app.timer.timer_running_c:
        app.update_display(next_time="いずれかのタイマーが終了")
        app.start_action()  # タイマーが終了している場合、スタートボタンと同じ処理を実行

        # コンソールに終了したタイマーを表示
        if not app.timer.timer_running_a:
            print("タイマーAが終了しました")
        if not app.timer.timer_running_b:
            print("タイマーBが終了しました")
        if not app.timer.timer_running_c:
            print("タイマーCが終了しました")
