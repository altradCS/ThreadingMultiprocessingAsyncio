import threading
import time

def simulate_io_task(file_name, duration):
  print(f"Starting task for processing {file_name}...")
  time.sleep(duration)  
  print(f"Finished task for processing {file_name} in {duration} seconds.")

def run_io_tasks():
  files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
  durations = [3, 2, 1, 5] 
  
  threads = []
  
  for i in range(len(files)):
      thread = threading.Thread(target=simulate_io_task, args=(files[i], durations[i]))
      threads.append(thread)
      thread.start()
  
  for thread in threads:
      thread.join()
