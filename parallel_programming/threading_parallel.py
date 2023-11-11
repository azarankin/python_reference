import threading
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

# Create a thread
thread1 = threading.Thread(target=print_numbers, args= (1, 5))
thread2 = threading.Thread(target=print_numbers_jump_by_10, args= (0.5, 5))

# Start the thread
thread1.start()
thread2.start()

# Wait for the thread to finish
thread1.join()
thread2.join()

print("Main thread exiting...")