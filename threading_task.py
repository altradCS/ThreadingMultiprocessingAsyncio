# Part 2: Threading with I/O-bound Tasks
#   In this part, you will simulate downloading multiple files concurrently using threading. Each thread will simulate an I/O-bound task by 
#       downloading a small dataset or processing the previously downloaded data file.
#         Steps:
#     1. Download files using threads:
#       Simulate downloading or processing files (e.g., multiple chunks of the large numbers.txt file or some other 
#       data files hosted in your gitbuh account).
#       Use threading to process multiple tasks at once.
import threading
import time

def simulate_io_task(file_name, duration):
  # Simulate I/O-bound task by downloading a file or processing the data
  with open(file_name, "r") as f:
    data = f.read()
    # Process the data
    print(f"Processed {file_name}: {data[:10]}...")  
  time.sleep(duration)
  print(f"{file_name} completed.")

def run_io_tasks():
  files = ["numbers1.txt", "numbers2.txt", "numbers3.txt"]
  num_threads = len(files)

  threads = []
  for i in range(num_threads):
    file_name = files[i]
    thread = threading.Thread(target=simulate_io_task, args=(file_name, 2))
    threads.append(thread)
    thread.start()

  # Wait for all threads to finish
  for thread in threads:
    thread.join()
    
  print("I/O tasks completed.")
