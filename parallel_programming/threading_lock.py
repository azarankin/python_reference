import threading
import time

# Shared variable
counter = 0
lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(5):
        with lock:
            counter += 1
            print(f"Counter: {counter}")
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread exiting...")

print(f'final counter =  {counter}') #10