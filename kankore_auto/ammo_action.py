def ammo_action(app):
    # 弾薬ボタンがクリックされたときの処理を記述
    app.update_display(current_task="弾薬実行中")

    # いずれかのタイマーが終了したかどうかを確認し、終了しているタイマーを起動
    if not app.timer.timer_running_a or not app.timer.timer_running_b or not app.timer.timer_running_c:
        app.update_display(current_task="いずれかのタイマーが終了")
        
        # 終了しているタイマーを再起動
        if not app.timer.timer_running_a:
            print("タイマーAが終了しました。再起動します。")
            app.start_timer_a()  # タイマーAを開始

        if not app.timer.timer_running_b:
            print("タイマーBが終了しました。再起動します。")
            app.start_timer_b()  # タイマーBを開始

        if not app.timer.timer_running_c:
            print("タイマーCが終了しました。再起動します。")
            app.start_timer_c()  # タイマーCを開始
