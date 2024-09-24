import threading
import time

def simulate_io_task(file_name, duration):
    print(f"Starting I/O task for {file_name}")
    time.sleep(duration)
    print(f"Finished I/O task for {file_name}")

def run_io_tasks():

    tasks = [
        ("file_1.txt", 2),  
        ("file_2.txt", 3),  
        ("file_3.txt", 1),  
    ]

    threads = []  

    for file_name, duration in tasks:
        thread = threading.Thread(target = simulate_io_task, args = (file_name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All I/O tasks completed.")