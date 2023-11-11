import _thread
import time


# Shared variable
counter = 0
lock = _thread.allocate_lock()

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(5):
        with lock:
            counter += 1
            print(f"Counter: {counter}")
        time.sleep(1)

# Create two threads
_thread.start_new_thread(increment_counter, ())
_thread.start_new_thread(increment_counter, ())


# Keep the main thread alive for a while
time.sleep(6)

print(f'final counter =  {counter}') #10