import threading
import time
import requests

def simulate_io_task(file_name, duration):
    
    print(f"Starting download for {file_name}...")
    time.sleep(duration) 

    try:
        response = requests.get("https://raw.githubusercontent.com/SopheakpanhaUM/ThreadingMultiprocessingAsyncio/refs/heads/main/numbers.txt", timeout=10)
        response.raise_for_status()
        numbers = response.text.splitlines()
        print(f"Processed {len(numbers)} lines from {file_name}.\n")

    except requests.RequestException as e:
        print(f"Failed to download {file_name}. Error: {e}")
    
    print(f"Finished downloading and processing {file_name}.\n")
    
def run_io_tasks():
        
    file_names = ['file_number1.txt', 'file_number2.txt', 'file_number3.txt', 'file_number4.txt', 'file_number5.txt']
    duration = 2  
    threads = []

    for file_name in file_names: 
        thread = threading.Thread(target = simulate_io_task, args = (file_name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All downloads and processing completed.")

