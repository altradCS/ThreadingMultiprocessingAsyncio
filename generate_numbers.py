import random

def generate_numbers(filename='numbers.txt', count=1000, max_num=1000000):
    """Generates a file with large random numbers."""
    with open(filename, 'w') as f:
        for _ in range(count):
            number = random.randint(2, max_num)
            f.write(f"{number}\n")
    print(f"Generated {count} random numbers in {filename}")

if __name__ == '__main__':
    generate_numbers()
