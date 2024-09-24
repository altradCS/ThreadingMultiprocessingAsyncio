import threading
import time

def simulate_io_task(file_name, duration):
    print(f"Start processing {file_name}")
    time.sleep(duration)  # Simulates a delay
    print(f"Finished processing {file_name}")

def run_io_tasks():
    threads = []
    for i in range(5):
        t = threading.Thread(target=simulate_io_task, args=(f"file_{i}.txt", 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
