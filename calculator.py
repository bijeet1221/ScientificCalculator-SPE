import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)

if __name__ == "__main__":
    print("=== Scientific Calculator ===")
    num = float(input("Enter a number: "))
    print(f"Square root of {num} = {square_root(num)}")

