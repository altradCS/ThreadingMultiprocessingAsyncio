
from multiprocessing_task import multiprocessing_prime
from threading_task import threading_download
from async_task import async_write_primes
import asyncio


def main():
    print("Running Multiprocessing Task...")
    primes = multiprocessing_prime()  # Run multiprocessing task to get prime numbers

    print("\nRunning Threading Task...")
    threading_download()  # Run threading task to simulate file downloads

    print("\nRunning Async IO Task...")
    asyncio.run(async_write_primes(primes))  # Run async IO task to write prime numbers to files


if __name__ == '__main__':
    main()
