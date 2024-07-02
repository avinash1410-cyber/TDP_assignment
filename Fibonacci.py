def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to n terms
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

def main():
    try:
        # Prompt user for input
        n = int(input("Enter the number of terms (n) for Fibonacci sequence: "))
        
        # Check if n is valid
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate Fibonacci sequence
        fibonacci_sequence = generate_fibonacci(n)
        
        # Print the Fibonacci sequence
        print(f"Fibonacci sequence with {n} terms:")
        print(fibonacci_sequence)
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()