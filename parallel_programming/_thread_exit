import _thread
import time

# Function that runs indefinitely
def infinite_thread():
    while True:
        print("Thread is running...")
        time.sleep(1)

# Create a thread
thread_id = _thread.start_new_thread(infinite_thread, ())

# Allow the thread to run for 3 seconds
time.sleep(3)

# Terminate the thread
_thread.exit_thread()
print("Main thread exiting...")