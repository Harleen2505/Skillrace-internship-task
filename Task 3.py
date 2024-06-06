import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Set the timer for 5 minutes (300 seconds)
countdown_timer(300)
