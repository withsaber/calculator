# Predefined credentials
USERNAME = "student"
PASSWORD = "pass123"

# Function to authenticate the user
def authenticate_user():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == USERNAME and password == PASSWORD:
            print("Authentication successful!")
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials. You have {attempts} attempts left.\n")
    
    print("Failed to authenticate after 3 attempts. Exiting...")
    return False

# Functions for each arithmetic operation
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

# Function to display the menu and perform operations
def calculator_menu():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                result = addition(num1, num2)
            elif choice == '2':
                result = subtraction(num1, num2)
            elif choice == '3':
                result = multiplication(num1, num2)
            elif choice == '4':
                result = division(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a valid option from the menu.")

# Main program logic
def main():
    if authenticate_user():
        calculator_menu()

if __name__ == "__main__":
    main()
