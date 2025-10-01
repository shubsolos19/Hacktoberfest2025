# GCD using Euclidean Algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
x, y = 48, 18
print(f"GCD of {x} and {y} is:", gcd(x, y))
