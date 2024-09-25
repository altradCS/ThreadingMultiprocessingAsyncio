import threading
import time
import urllib.request

def download_file(file_name, delay):
    """Simulate an I/O task by downloading a file after a specified delay."""
    url = f'https://raw.githubusercontent.com/ChenChanveasna/testCsB/refs/heads/main/{file_name}'
    print(f'Starting download of {file_name} from {url}', flush=True)
    try:
        time.sleep(delay)
        response = urllib.request.urlopen(url)
        with open(f'ThreadingMultiprocessingAsyncio/{file_name}', 'wb') as file:
            file.write(response.read())
        print(f'Successfully downloaded {file_name}', flush=True)
    except Exception as error:
        print(f'Error downloading {file_name}: {error}')

def execute_io_tasks():
    """Run multiple I/O tasks concurrently using threading."""
    file_names = ['numbers1.txt', 'numbers2.txt', 'numbers3.txt', 'numbers4.txt']
    delay = 3
    threads = []

    # Create and start a thread for each file download task
    for file_name in file_names:
        thread = threading.Thread(target=download_file, args=(file_name, delay))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print('All files have been downloaded.')
