import time
import signal
import sys

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGKILL, signal_handler)
print('Press Ctrl+C')
signal.pause()

def bother_me():
    try:
        while True:
            time.sleep(1)
            print("Insult")
    except KeyboardInterrupt as e:
        print("Mock")
        bother_me()

bother_me()
