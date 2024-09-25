import threading
import time
import requests

# simulated I/O task (e.g., downloading or processing a file)
def simulate_io_task(file_name, duration):
  print(f"Starting I/O task for file: {file_name}")
  time.sleep(duration)  
  print(f"Completed I/O task for file: {file_name}")

# function to run I/O-bound tasks using threading
def run_io_tasks():
  # file names (I/O tasks)
  io_tasks = [("file1.txt", 5), ("file2.txt", 3), ("file3.txt", 4)] 
    
  threads = []

  # create a thread for each I/O task
  for file_name, duration in io_tasks:
    thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

