import mss

"""
画面をキャプチャする
"""

with mss.mss() as sct:
    # モニター1のスクリーンショットを取得
    screenshot = sct.shot(output='screenshot.png')
