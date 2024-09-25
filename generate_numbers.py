import random

def create_file_with_random_numbers(filename, quantity, min_val, max_val):
    """Creates a file containing randomly generated numbers."""
    path = f'ThreadingMultiprocessingAsyncio/{filename}'  # This ensures the file is saved in the same directory when running main.py
    with open(path, "w") as file:
        for _ in range(quantity):
            number = random.randint(min_val, max_val)
            file.write(f"{number}\n")
    print(f"Generated '{filename}' with {quantity} random numbers.")
