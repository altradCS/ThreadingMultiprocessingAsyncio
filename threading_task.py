import threading
import time

def simulate_io_task(file_name, duration):
    """Simulate an I/O-bound task by sleeping for a given duration."""
    print(f"Starting I/O task for: {file_name}")
    time.sleep(duration)  # Simulate the time taken for the I/O operation
    print(f"Completed I/O task for: {file_name}")

def run_io_tasks():
    """Run multiple I/O tasks concurrently using threading."""
    # Define a list of file names and durations for the tasks
    tasks = [
        ("file_1.txt", 2),
        ("file_2.txt", 3),
        ("file_3.txt", 1),
        ("file_4.txt", 4),
    ]

    threads = []

    # Create and start threads for each I/O task
    for file_name, duration in tasks:
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All I/O tasks completed.")
