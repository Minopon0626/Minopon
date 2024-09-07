from utility_functions import delayed_click, delayed_update, delayed_drag_and_drop

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
        delayed_drag_and_drop(root, 550, 410, 1060, 600)
    ))

    root.after(10000, lambda: (
        delayed_update(root, current_task_label, 0, "母港に戻る"),
        delayed_click(root, 70, 220)
    ))

    # 3. 10秒後に「ボーキ完了」に更新
    root.after(20000, lambda: delayed_update(root, current_task_label, 0, "ボーキ完了"))