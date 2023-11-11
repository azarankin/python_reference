import threading
import time

# daemon thread will exit with the program

# Function for a daemon thread
def daemon_function():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True

# Start the daemon thread
daemon_thread.start()

# Allow the main thread to run for 3 seconds
time.sleep(3)

print("Main thread exiting...")