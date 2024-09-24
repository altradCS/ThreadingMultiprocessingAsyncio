import threading
import time

def simulate_io_task(file_name, duration):
    """Simulate an I/O task by sleeping for a specified duration."""
    print(f"Starting download for {file_name}...")
    time.sleep(duration)  # Simulating I/O delay
    print(f"Completed download for {file_name}.")

def run_io_tasks():
    """Run multiple I/O tasks concurrently using threads."""
    tasks = [
        ("file1.txt", 2),
        ("file2.txt", 3),
        ("file3.txt", 1),
    ]
    
    threads = []
    
    for file_name, duration in tasks:
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()  # Wait for all threads to complete
