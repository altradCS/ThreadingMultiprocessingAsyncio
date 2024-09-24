import threading
import time
import requests

def simulate_io_task(file_name, duration):
  print(f"Start processing task {file_name}...")
  time.sleep(duration) 
  url = requests.get('https://raw.githubusercontent.com/ChhunSokvisothh/number/refs/heads/main/numbers.txt')

  if url.status_code == 200:
      numbers = url.text.splitlines()
      print(f"Processed {len(numbers)} lines from {file_name}.")
  else:
      print(f"Failed to download {file_name}. Status code: {url.status_code}")
      
  print(f"Finished processing task {file_name} in {duration} seconds.")

def run_io_tasks():
  files = ["chunk1.txt", "chunk2.txt", "chunk3.txt", "chunk4.txt"]
  duration = 1.032490432
  
  threads = []
  
  for i in range(len(files)):
      thread = threading.Thread(target=simulate_io_task, args=(files[i], duration))
      threads.append(thread)
      thread.start()
  
  for thread in threads:
      thread.join()
  print("Processings and downloads tasks are completed.")