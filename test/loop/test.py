import time

sec = 1
while True:
    print(sec)
    sec += 1
    if sec == 60:
        sec = 1
    time.sleep(1)
