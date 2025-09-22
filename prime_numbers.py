def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes

def main():
    """Main function to generate and display the first 40 prime numbers."""
    count = 40
    primes = generate_first_n_primes(count)
    
    print(f"The first {count} prime numbers are:")
    print("-" * 40)
    
    # Print primes in rows of 10 for better readability
    for i in range(0, len(primes), 10):
        row = primes[i:i+10]
        print(" ".join(f"{prime:3d}" for prime in row))
    
    print("-" * 40)
    print(f"Total: {len(primes)} prime numbers")
    print(f"Largest prime: {max(primes)}")

if __name__ == "__main__":
    main()