# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple Calculator CLI")
    while True:
        print("\nOptions: add, subtract, multiply, divide, quit")
        choice = input("Enter operation: ").strip().lower()
        if choice == 'quit':
            print("Exiting calculator.")
            break
        if choice not in ('add', 'subtract', 'multiply', 'divide'):
            print("Invalid operation. Try again.")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == 'add':
                print("Result:", add(a, b))
            elif choice == 'subtract':
                print("Result:", subtract(a, b))
            elif choice == 'multiply':
                print("Result:", multiply(a, b))
            elif choice == 'divide':
                print("Result:", divide(a, b))
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
