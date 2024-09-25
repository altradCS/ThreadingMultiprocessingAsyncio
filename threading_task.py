import threading
import time

def simulate_io_task(file_name, duration):
    print(f"Starting I/O task on {file_name}, will take {duration} seconds.")
    time.sleep(duration)  # Simulates an I/O operation like reading/writing a file
    print(f"Completed I/O task on {file_name}.")

def run_io_tasks():
    threads = []
    files = ["file1.txt", "file2.txt", "file3.txt"]
    durations = [2, 3, 1]  # Simulate different durations for each I/O task

    for file, duration in zip(files, durations):
        thread = threading.Thread(target=simulate_io_task, args=(file, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete
