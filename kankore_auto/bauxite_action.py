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

    # 3. 10秒後に「ボーキ完了」に更新
    root.after(45000, lambda: delayed_update(root, current_task_label, 0, "ボーキ完了"))