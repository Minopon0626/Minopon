import time

def expedition_action(current_task_label):
    # 遠征の処理
    update_label(current_task_label, "遠征中...")
    time.sleep(2)  # 仮に処理に2秒かかるとします
    update_label(current_task_label, "遠征完了")

# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)
