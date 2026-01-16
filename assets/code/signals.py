import signal
import time

def sig_int(signal,frame):
    print("bye bye")

signal.signal(signal.SIGINT, sig_int)

while True:
    time.sleep(.5)
