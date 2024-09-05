import time
from pyautogui_actions import open_formation, return_to_port, supply

def ammo_action(app):
    """
    弾薬ボタンが押されたときの動作:
    1. 編成を開く
    2. 2秒待機
    3. 母港に戻る
    4. 2秒待機
    5. 補給を行う
    6. 母港に戻る
    7. タイマーの終了を確認して再起動
    """
    # 編成を開く
    open_formation(app)
    
    # 2秒待機
    time.sleep(2)
    
    # 母港に戻る
    return_to_port(app)
    
    # 2秒待機
    time.sleep(2)
    
    # 補給を行う
    supply(app)
    
    # 再度母港に戻る
    return_to_port(app)
    
    # タイマーの終了を確認し、終了したタイマーがあれば再起動
    if not app.timer.timer_running_a or not app.timer.timer_running_b or not app.timer.timer_running_c:
        app.update_display(current_task="いずれかのタイマーが終了")
        
        if not app.timer.timer_running_a:
            print("タイマーAが終了しました。再起動します。")
            app.start_timer_a()

        if not app.timer.timer_running_b:
            print("タイマーBが終了しました。再起動します。")
            app.start_timer_b()

        if not app.timer.timer_running_c:
            print("タイマーCが終了しました。再起動します。")
            app.start_timer_c()
