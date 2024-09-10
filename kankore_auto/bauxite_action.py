from utility_functions import delayed_click, delayed_update, delayed_drag_and_drop, return_to_home_port

def bauxite_click(root, current_task_label):
    """
    1. 母港画面から編成をクリック
    2. 編成画面から編成を変更する
    3. ボーキ完了と表示
    """

    # 1. ラベルを「編成をクリック」に更新してから、編成をクリック
    delayed_update(root, current_task_label, 0, "編成をクリック")
    delayed_click(root, 300, 360)

    # 2. 5秒後に「編成を変更」に更新してから、ドラッグ・アンド・ドロップを実行
    root.after(5000, lambda: (
        delayed_update(root, current_task_label, 0, "旗艦を変更"),
        delayed_drag_and_drop(root, 550, 410, 1060, 750)
    ))

    # 3. 10秒後に「母港に戻る」に更新してから、母港をクリック
    root.after(10000, lambda: (
        return_to_home_port(root, current_task_label)
    ))

    # 4. 15秒後に「母港から出撃」に更新してから、出撃をクリック
    root.after(15000, lambda: (
        delayed_update(root, current_task_label, 0, "母港から出撃"),
        delayed_click(root, 300, 550)
    ))


    root.after(20000, lambda: (
        delayed_update(root, current_task_label, 0, "出撃から出撃"),
        delayed_click(root, 350, 490)
    ))

    root.after(25000, lambda: (
        delayed_update(root, current_task_label, 0, "鎮守府海域から南西海域を選択"),
        delayed_click(root, 510, 830)
    ))

    root.after(30000, lambda: (
        delayed_update(root, current_task_label, 0, "南西海域からヒ船団会場護衛作戦を選択"),
        delayed_click(root, 1020, 700)
    ))

    root.after(35000, lambda: (
        delayed_update(root, current_task_label, 0, "決定を選択"),
        delayed_click(root, 1010, 830)
    ))

    root.after(40000, lambda: (
        delayed_update(root, current_task_label, 0, "出撃開始を選択"),
        delayed_click(root, 920, 830)
    ))

    # 海域に突入

    root.after(45000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # start to C

    root.after(55000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 戦闘開始 Cマス

    # 戦闘は30秒ほど

    root.after(85000, lambda: (
        delayed_update(root, current_task_label, 0, "追撃せずを選択"),
        delayed_click(root, 430, 520)
    ))

    # 戦闘終了, リザルトは10秒ほどあとに出現

    root.after(95000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    root.after(100000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    root.after(105000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # Cマス報酬受け取り完了

    root.after(110000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # C to D

    root.after(120000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 戦闘開始 Dマス

    # 戦闘は30秒ほど
    # 空襲なので追撃選択肢なし

    root.after(150000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    root.after(155000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    root.after(160000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # Dマス報酬受け取り完了

    # 報酬受け取り後自動移動


    # 能動選択
    root.after(170000, lambda: (
        delayed_update(root, current_task_label, 0, "能動選択[J]を選択"),
        delayed_click(root, 710, 480)
    ))

    # Jマス移動

    root.after(180000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 戦闘開始 Jマス

    # 戦闘は50秒ほど
    root.after(230000, lambda: (
        delayed_update(root, current_task_label, 0, "追撃せずを選択"),
        delayed_click(root, 430, 520)
    ))

    root.after(240000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    root.after(245000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    root.after(250000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # Jマス報酬受け取り完了

    # 羅針盤
    root.after(255000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # J to K

    root.after(270000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 戦闘開始 Kマス

    # 戦闘は30秒ほど

    root.after(300000, lambda: (
        delayed_update(root, current_task_label, 0, "追撃せずを選択"),
        delayed_click(root, 430, 520)
    ))

    root.after(310000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    root.after(315000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    root.after(320000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # Kマス報酬受け取り完了

    # 羅針盤
    root.after(325000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # K to M

    root.after(335000, lambda: (
        delayed_update(root, current_task_label, 0, "輪形陣を選択"),
        delayed_click(root, 1060, 440)
    ))

    # 戦闘開始 Dマス

    # 戦闘は40秒ほど
    # 空襲なので追撃選択肢なし

    root.after(375000, lambda: (
        delayed_update(root, current_task_label, 0, "戦闘評価更新"),
        delayed_click(root, 1010, 200)
    ))

    root.after(385000, lambda: (
        delayed_update(root, current_task_label, 0, "経験値回収"),
        delayed_click(root, 1010, 200)
    ))

    root.after(390000, lambda: (
        delayed_update(root, current_task_label, 0, "進撃を選択"),
        delayed_click(root, 430, 520)
    ))

    # Dマス報酬受け取り完了

    # 羅針盤
    root.after(400000, lambda: (
        delayed_update(root, current_task_label, 0, "羅針盤を回転"),
        delayed_click(root, 1010, 200)
    ))

    # goal到達
    root.after(410000, lambda: (
        delayed_update(root, current_task_label, 0, "報酬を受け取り"),
        delayed_click(root, 1010, 200)
    ))

    # 3. 10秒後に「ボーキ完了」に更新
    root.after(45000, lambda: delayed_update(root, current_task_label, 0, "ボーキ完了"))