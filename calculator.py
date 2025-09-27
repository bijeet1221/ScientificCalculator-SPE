import math

def square_root(x: float) -> float:
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)

def factorial(x: int) -> int:
    if x < 0:
        raise ValueError("Cannot compute factorial of negative number")
    return math.factorial(x)

def natural_log(x: float) -> float:
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    return math.log(x)

def power(x: float, b: float) -> float:
    return math.pow(x, b)


if __name__ == "__main__":
    while True:
        print("\n=== Scientific Calculator ===")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        try:
            if choice == "1":
                num = float(input("Enter a number: "))
                print(f"√{num} = {square_root(num)}")

            elif choice == "2":
                num = int(input("Enter an integer: "))
                print(f"{num}! = {factorial(num)}")

            elif choice == "3":
                num = float(input("Enter a number: "))
                print(f"ln({num}) = {natural_log(num)}")

            elif choice == "4":
                base = float(input("Enter base (x): "))
                exp = float(input("Enter exponent (b): "))
                print(f"{base}^{exp} = {power(base, exp)}")

            elif choice == "5":
                print("Exiting calculator. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter 1-5.")

        except ValueError as e:
            print(f"Error: {e}")
