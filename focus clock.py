import time

def focus_timer(minutes):
    """
    生成一个专注时钟，参数为分钟。
    """
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
