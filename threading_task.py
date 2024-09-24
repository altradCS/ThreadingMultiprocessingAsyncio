import threading
import time
import urllib.request

def simulate_io_task(file_name, duration):
  url = f'https://raw.githubusercontent.com/ChenChanveasna/testCsB/refs/heads/main/{file_name}'
  print(f'Downloading {file_name} from {url}', flush=True)
  try:
    time.sleep(duration)
    response = urllib.request.urlopen(url)
    with open(f'ThreadingMultiprocessingAsyncio\{file_name}', 'wb') as f:
      f.write(response.read())
    print(f'Downloaded {file_name}', flush=True)
  
  except Exception as e:
    print(f'Failed to download {file_name}. Error: {e}')

def run_io_tasks():
  file_lists = ['numbers1.txt','numbers2.txt','numbers3.txt','numbers4.txt']
  duration = 3
  threads = []
  
  for file in file_lists:
    thread = threading.Thread(target=simulate_io_task, args=(file, duration))
    threads.append(thread)
    thread.start()
    
  for thread in threads: # waiting for all the threads to be executed
    thread.join()
  
  print('Downloaded all the files.')
