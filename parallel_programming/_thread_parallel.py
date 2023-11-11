import _thread
import time

# Define a function for the thread
def print_numbers(delay, count):
    for i in range(count):
        time.sleep(delay)
        print(f"Thread: {i + 1}")

def print_numbers_jump_by_10(delay, count):
    for i in range(count):
        time.sleep(delay)
        print(f"Thread: {(i+ 1) * 10}")


# Create two threads
_thread.start_new_thread(print_numbers, (1, 5))
_thread.start_new_thread(print_numbers_jump_by_10, (0.5, 5))

# Keep the main thread alive for a while
time.sleep(5)



