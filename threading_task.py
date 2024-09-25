import threading
import time

def simulate_io_task(file_name, duration):
    """Simulate io time-consuming task."""
    print(f"Starting I/O task for {file_name}...")
    time.sleep(duration)
    print(f"Completed io task for {file_name}")

def run_io_tasks():
    """Run multiple I/O tasks in parallel using threading."""
    threads = []
    for i in range(5):  
        thread = threading.Thread(target=simulate_io_task, args=(f'file_{i}.txt', 2))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  