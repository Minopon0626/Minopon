from timer import start_timer

def start_expedition(label_second_fleet, label_third_fleet, label_fourth_fleet):
    # 第二艦隊, 第三艦隊, 第四艦隊のタイマーを開始
    start_timer(600, label_second_fleet)  # 10分 = 600秒
    start_timer(1200, label_third_fleet)  # 20分 = 1200秒
    start_timer(4800, label_fourth_fleet)  # 1時間20分 = 4800秒

# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)
