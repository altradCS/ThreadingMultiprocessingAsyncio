import random

def generate_numbers_file(filename, num_numbers, min_value, max_value):
    """Generates a file with random numbers."""
    with open(filename, "w") as f:
        for _ in range(num_numbers):
            number = random.randint(min_value, max_value)
            f.write(f"{number}\n")
    print(f"File '{filename}' with {num_numbers} random numbers generated.")

if __name__ == "__main__":
    # Example parameters; you can modify them as needed
    filename = "numbers.txt"
    num_numbers = 1000  # Number of random numbers to generate
    min_value = 1       # Minimum value for random numbers
    max_value = 100000  # Maximum value for random numbers
    
    generate_numbers_file(filename, num_numbers, min_value, max_value)
