import threading
import requests

def simulate_io_task(file_name):
    try:
        with requests.get(file_name) as req:
            req.raise_for_status() 
            output = req.url[req.url.rfind('/') + 1:]
            with open(output, 'wb') as f:
                for chunk in req.iter_content(chunk_size=128):
                    f.write(chunk)
            print(f"File '{output}' downloaded.")
            return output
    except Exception as e:
        return str(e)

def run_io_tasks():
    files = [
        "https://raw.githubusercontent.com/S0KPiseth/4k-youtube-downloader-with-UI/refs/heads/main/functions.py",
        "https://raw.githubusercontent.com/S0KPiseth/MultiTimer/refs/heads/main/UI.py",
    ]
    threads = []
    for file in files:
        t = threading.Thread(target=simulate_io_task, args=(file,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    print("All I/O tasks completed.")

