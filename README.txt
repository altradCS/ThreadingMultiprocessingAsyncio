Lab Assignment: Exploring Multiprocessing, Threading, and Async IO with Data file.

Objective:
In this assignment, you will create a Python program that:

1. Uses multiprocessing to perform CPU-bound tasks (e.g., prime number calculation) on large data.
2. Uses threading to perform I/O-bound tasks (e.g., file downloads).
3. Uses async IO to perform non-blocking I/O tasks (e.g., file writing).

You will work with real file from your GitHub account.


Part 1: Multiprocessing with CPU-bound Tasks
  In this part, you will use multiprocessing to process a file containing a list of large numbers and calculate whether each number is prime. This task will involve splitting the data across multiple processes to fully utilize the CPU.

    Steps:
    1 Upload the data:
       Upload a file (numbers.txt) containing a list of large numbers (one per line) to GitHub repository.
       Download the file in your Python code using a URL.
    
    2. Process the file using multiprocessing:
       Create a function that reads the file, divides the data into chunks, and uses the multiprocessing.Pool to calculate whether each number is prime.
       Use the is_prime function to check if a number is prime.


Part 2: Threading with I/O-bound Tasks
  In this part, you will simulate downloading multiple files concurrently using threading. Each thread will simulate an I/O-bound task by 
      downloading a small dataset or processing the previously downloaded data file.
        Steps:
    1. Download files using threads:
      Simulate downloading or processing files (e.g., multiple chunks of the large numbers.txt file or some other data files hosted in your gitbuh account).
      Use threading to process multiple tasks at once.

Part 3: Async IO with Non-blocking I/O-bound Tasks
    In this part, you will perform file writing tasks asynchronously using async IO. You will simulate writing results to files asynchronously, which can help you manage a large number of I/O operations without blocking the program.

    Steps:
       Use Async IO for writing files:
        1. Write the prime numbers calculated in Part 1 to multiple files asynchronously.
        2. Ensure the program doesn’t block while writing to files.

Requirements:
Modularize (Functions): split the logic for multiprocessing, threading, and async IO into different modules and call them from a main.py file.

Project Structure:
project/
│
├── multiprocessing_task.py
├── threading_task.py
├── async_task.py
├── generate_numbers.py
└── main.py

Lab Submission:
Clone this project, do the necessary, then push it up to github.
