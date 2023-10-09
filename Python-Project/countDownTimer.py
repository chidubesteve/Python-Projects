import time

def countDown(userTime):
    while userTime:
        mins,sec = divmod(userTime, 60)
        time.sleep(1)
        print('{:02d}:{:02d}'.format(mins, sec))
        userTime -= 1
    print('Countdown has ended!')

userTime = int(input('Enter start time (in secs): '))
countDown(userTime)