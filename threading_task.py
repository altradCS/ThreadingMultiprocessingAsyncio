# threading_task.py
# threading_task.py
import threading
import time
import random

def download_file(file_number):
    """Simulates downloading a file (you can replace this with actual file operations)."""
    print(f"Starting download of file {file_number}...")
    time.sleep(random.uniform(1, 3))  # Simulates variable download time
    print(f"File {file_number} downloaded.")

def threading_download(num_files=5):
    """Simulates downloading multiple files using threads."""
    threads = []

    for i in range(num_files):
        thread = threading.Thread(target=download_file, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete

    print("All files downloaded.")

if __name__ == '__main__':
    threading_download()
