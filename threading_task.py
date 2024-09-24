import threading
import time
import requests


def simulate_io_task(file_name, url, duration):
    print(f"Starting download for {file_name}...")
    time.sleep(duration)  

    response = requests.get(url)
    
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Finished downloading {file_name}.")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")
    

def run_io_tasks():

    threads = []
    duration = 2
    
    # URLs for the files you want to download
    file_urls = [
        "https://raw.githubusercontent.com/Kheav-Kienghok/CSB-Assignment/refs/heads/main/prime1.txt",
        "https://raw.githubusercontent.com/Kheav-Kienghok/CSB-Assignment/refs/heads/main/prime2.txt",
        "https://raw.githubusercontent.com/Kheav-Kienghok/CSB-Assignment/refs/heads/main/prime3.txt"
    ]
    
    for i, url in enumerate(file_urls):
        filename = f"down_load_prime{i + 1}.txt"  
        thread = threading.Thread(target = simulate_io_task, args = (filename, url, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All downloads and processing completed.")