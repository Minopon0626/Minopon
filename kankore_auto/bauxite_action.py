from utility_functions import delayed_click, delayed_update, delayed_drag_and_drop, return_to_home_port, delayed_click_with_countdown, delayed_drag_and_drop_with_countdown, supply_fleets

def bauxite_click(root, current_task_label):
    """
    ボーキ処理開始。母港画面から編成画面へ移動し、旗艦を変更する。
    """
    # 1. 最初にdelayed_clickを呼び出し、カウントダウンを表示
    delayed_click_with_countdown(root, current_task_label, 300, 360, "母港から編成")

    # 2. 5秒後に旗艦を変更する処理
    execute_after_delay(root, 5, delayed_drag_and_drop_with_countdown, root, current_task_label, 550, 410, 1060, 750, "旗艦を変更")

    # 例: 10秒後に delayed_click_with_countdown 関数を実行
    execute_after_delay(root, 10, return_to_home_port, root, current_task_label)

    execute_after_delay(root, 15, delayed_click_with_countdown, root, current_task_label, 300, 550, "母港から出撃")

    execute_after_delay(root, 20, delayed_click_with_countdown, root, current_task_label, 350, 490, "出撃から出撃")

    execute_after_delay(root, 25, delayed_click_with_countdown, root, current_task_label, 510, 830, "南西海域の部分")

    execute_after_delay(root, 30, delayed_click_with_countdown, root, current_task_label, 1000, 700, "7-4")

    execute_after_delay(root, 35, delayed_click_with_countdown, root, current_task_label, 1000, 820, "決定")

    execute_after_delay(root, 40, delayed_click_with_countdown, root, current_task_label, 1000, 820, "出撃開始")

    execute_after_delay(root, 50, delayed_click_with_countdown, root, current_task_label, 1000, 200, "羅針盤")

    # 戦闘中

    execute_after_delay(root, 90, delayed_click_with_countdown, root, current_task_label, 430, 520, "追撃せず")

    execute_after_delay(root, 100, delayed_click_with_countdown, root, current_task_label, 1000, 200, "戦闘評価更新")

    execute_after_delay(root, 105, delayed_click_with_countdown, root, current_task_label, 1000, 200, "経験値取得")

    execute_after_delay(root, 110, delayed_click_with_countdown, root, current_task_label, 430, 520, "進撃")

    execute_after_delay(root, 115, delayed_click_with_countdown, root, current_task_label, 1000, 200, "羅針盤")

    # 戦闘中

    execute_after_delay(root, 160, delayed_click_with_countdown, root, current_task_label, 1000, 200, "戦闘評価更新")

    execute_after_delay(root, 165, delayed_click_with_countdown, root, current_task_label, 1000, 200, "経験値取得")

    execute_after_delay(root, 170, delayed_click_with_countdown, root, current_task_label, 430, 520, "進撃")

    # 進撃選択後自動移動

    execute_after_delay(root, 180, delayed_click_with_countdown, root, current_task_label, 710, 480, "能動選択[J]")

    # 戦闘中 60s

    execute_after_delay(root, 240, delayed_click_with_countdown, root, current_task_label, 430, 520, "追撃せず")

    execute_after_delay(root, 250, delayed_click_with_countdown, root, current_task_label, 1000, 200, "戦闘評価更新")

    execute_after_delay(root, 255, delayed_click_with_countdown, root, current_task_label, 1000, 200, "経験値取得")

    execute_after_delay(root, 260, delayed_click_with_countdown, root, current_task_label, 430, 520, "進撃")

    execute_after_delay(root, 265, delayed_click_with_countdown, root, current_task_label, 1000, 200, "羅針盤")

    # 戦闘中 45s

    execute_after_delay(root, 310, delayed_click_with_countdown, root, current_task_label, 430, 520, "追撃せず")

    execute_after_delay(root, 320, delayed_click_with_countdown, root, current_task_label, 1000, 200, "戦闘評価更新")

    execute_after_delay(root, 325, delayed_click_with_countdown, root, current_task_label, 1000, 200, "経験値取得")

    execute_after_delay(root, 330, delayed_click_with_countdown, root, current_task_label, 430, 520, "進撃")

    execute_after_delay(root, 335, delayed_click_with_countdown, root, current_task_label, 1000, 200, "羅針盤")

    # 戦闘中 45s

    execute_after_delay(root, 380, delayed_click_with_countdown, root, current_task_label, 430, 520, "追撃せず")

    execute_after_delay(root, 390, delayed_click_with_countdown, root, current_task_label, 1000, 200, "戦闘評価更新")

    execute_after_delay(root, 395, delayed_click_with_countdown, root, current_task_label, 1000, 200, "経験値取得")

    execute_after_delay(root, 400, delayed_click_with_countdown, root, current_task_label, 430, 520, "進撃")

    execute_after_delay(root, 405, delayed_click_with_countdown, root, current_task_label, 1000, 200, "羅針盤")

    # 報酬受け取り 20s

    execute_after_delay(root, 425, delayed_click_with_countdown, root, current_task_label, 1000, 200, "報酬受取")

    execute_after_delay(root, 430, supply_fleets, root, current_task_label)

def bauxite_click_6seki(root, current_task_label):
    """
    母港から出撃するための一連の操作。6隻編成での遠征開始。
    """
    # 1. 「編成をクリック」に更新し、編成画面に移動
    delayed_update(root, current_task_label, 0, "編成をクリック")
    delayed_click(root, 300, 360)

    # 2. 5秒後に旗艦を変更
    root.after(5000, lambda: (
        delayed_update(root, current_task_label, 0, "旗艦を変更"),
        delayed_drag_and_drop(root, 550, 410, 1060, 750)  # 旗艦をドラッグ＆ドロップで変更
    ))

    # 3. 10秒後に母港に戻る
    root.after(10000, lambda: (
        return_to_home_port(root, current_task_label)  # 母港に戻る処理
    ))

    # 4. 15秒後に出撃画面へ移動
    root.after(15000, lambda: (
        delayed_update(root, current_task_label, 0, "母港から出撃"),
        delayed_click(root, 300, 550)  # 出撃をクリック
    ))

    # 5. 出撃ボタンをクリック
    root.after(20000, lambda: (
        delayed_update(root, current_task_label, 0, "出撃から出撃"),
        delayed_click(root, 350, 490)  # 出撃確認をクリック
    ))

    # 6. 鎮守府海域から南西海域を選択
    root.after(25000, lambda: (
        delayed_update(root, current_task_label, 0, "鎮守府海域から南西海域を選択"),
        delayed_click(root, 510, 830)
    ))

    # 7. 南西海域からヒ船団会場護衛作戦を選択
    root.after(30000, lambda: (
        delayed_update(root, current_task_label, 0, "南西海域からヒ船団会場護衛作戦を選択"),
        delayed_click(root, 1020, 700)
    ))

    # 8. 作戦決定
    root.after(35000, lambda: (
        delayed_update(root, current_task_label, 0, "決定を選択"),
        delayed_click(root, 1010, 830)
    ))

    # 9. 出撃開始
    root.after(40000, lambda: (
        delayed_update(root, current_task_label, 0, "出撃開始を選択"),
        delayed_click(root, 920, 830)
    ))

    # 10. 羅針盤を回転
    root.after(45000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # 11. 輪形陣を選択 (Cマス)
    root.after(55000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 12. 戦闘開始 (Cマス)
    # 戦闘開始。戦闘は約30秒
    root.after(85000, lambda: (
        delayed_update(root, current_task_label, 0, "追撃せずを選択"),
        delayed_click(root, 430, 520)
    ))

    # 13. 戦闘評価更新 (リザルト画面)
    root.after(95000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    # 14. 経験値回収
    root.after(100000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    # 15. 進撃を選択
    root.after(105000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # 16. 羅針盤を回転 (C to D)
    root.after(110000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # 17. 輪形陣を選択 (Dマス)
    root.after(120000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 18. 戦闘開始 (Dマス)
    # 空襲戦。追撃選択肢なし
    root.after(150000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    # 19. 経験値回収
    root.after(155000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    # 20. 進撃を選択 (Dマス)
    root.after(160000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # 21. 能動選択 (Jマス)
    root.after(170000, lambda: (
        delayed_update(root, current_task_label, 0, "能動選択[J]を選択"),
        delayed_click(root, 710, 480)
    ))

    # 22. 輪形陣を選択 (Jマス)
    root.after(180000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 23. 戦闘開始 (Jマス)
    root.after(230000, lambda: (
        delayed_update(root, current_task_label, 0, "追撃せずを選択"),
        delayed_click(root, 430, 520)
    ))

    # 24. 戦闘評価更新 (Jマスリザルト)
    root.after(240000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    # 25. 経験値回収
    root.after(245000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    # 26. 羅針盤を回転 (J to K)
    root.after(255000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # 27. 輪形陣を選択 (Kマス)
    root.after(270000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 28. 戦闘開始 (Kマス)
    root.after(300000, lambda: (
        delayed_update(root, current_task_label, 0, "追撃せずを選択"),
        delayed_click(root, 430, 520)
    ))

    # 29. 戦闘評価更新 (Kマスリザルト)
    root.after(310000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    # 30. 経験値回収
    root.after(315000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    # 31. 羅針盤を回転 (K to M)
    root.after(325000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # 32. 輪形陣を選択 (Mマス)
    root.after(335000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 33. 戦闘開始 (Mマス)
    root.after(375000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    # 34. 経験値回収
    root.after(385000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    # 35. 羅針盤を回転 (M to Goal)
    root.after(400000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # 36. 報酬受け取り
    root.after(410000, lambda: (
        delayed_update(root, current_task_label, 0, "報酬を受け取り"),
        delayed_click(root, 1010, 200)
    ))

    # 37. ボーキ完了
    root.after(450000, lambda: delayed_update(root, current_task_label, 0, "ボーキ完了"))


def execute_after_delay(root, seconds, func, *args):
    """
    指定した秒数後に任意の関数を実行する関数。

    :param root: Tkinterのrootウィンドウ
    :param seconds: 関数を実行するまでの遅延時間（秒単位）
    :param func: 実行する関数
    :param args: 関数に渡す引数
    """
    milliseconds = seconds * 1000  # 秒をミリ秒に変換
    root.after(milliseconds, lambda: func(*args))
