import threading
import time

def simulate_io_task(file_name, duration):
    """Simulate an I/O-bound task, such as file download."""
    print(f"Starting I/O task for {file_name}")
    time.sleep(duration)
    print(f"Completed I/O task for {file_name}")

def run_io_tasks():
    """Run I/O-bound tasks concurrently using threads."""
    file_tasks = [
        threading.Thread(target=simulate_io_task, args=(f"file_{i}.txt", 2)) for i in range(5)
    ]

    for task in file_tasks:
        task.start()

    for task in file_tasks:
        task.join()
    print("All I/O tasks completed.")
