import time
import sys

for i in range(10, 0, -1):
    sys.stdout.write("\r残り {} 秒".format(i))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rタイマー終了！\n")
sys.stdout.flush()
