n = int(input("Enter the nth-fibonacci number: "))

def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
for num in nth_fibonacci(n):
    print(num)