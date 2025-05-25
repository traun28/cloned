#include <stdio.h>

int main() {
    double n1 = 0.0, n2 = 0.0, result = 0.0;
    char operation = ' ';
    while (1) {
        while (scanf("%lf %c %lf", &n1, &operation, &n2) != 3) {
            printf("Error.\n");
            while ((getchar()) != '\n'); // Clear the input buffer
        }
        switch (operation) {
            case '+':
                result = n1 + n2;
                printf("%lf\n", result);
                return 0;
            case '-':
                result = n1 - n2;
                printf("%lf\n", result);
                return 0;
            case '*':
                result = n1 * n2;
                printf("%lf\n", result);
                return 0;
            case '/':
                if (n2 != 0) {
                    result = n1 / n2;
                    printf("%lf\n", result);
                    return 0;
                } else {
                    printf("Error! Division by zero.\n");
                    return 1;
                }
            default:
                printf("Error! Invalid Operator.\n");
                break;
        }
    }
    return 0;
}def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input"i)



def advanced_calculator():
    """
    A more advanced command-line calculator that allows multiple operations
    and includes better error handling.
    """
    print("--- Advanced Calculator ---")

    while True:
        try:
            num1_str = input("Enter first number (or 'q' to quit): ").lower()
            if num1_str == 'q':
                print("Exiting calculator. Goodbye!")
                break
            num1 = float(num1_str)

            operator = input("Enter operator (+, -, *, /): ")
            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator. Please use +, -, *, or /.")
                continue # Go back to the beginning of the loop

            num2_str = input("Enter second number: ").lower()
            if num2_str == 'q': # Allow quitting after first number too
                print("Exiting calculator. Goodbye!")
                break
            num2 = float(num2_str)

            result = None
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue # Go back to the beginning of the loop
                else:
                    result = num1 / num2

            print(f"Result: {num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("Invalid number input. Please enter numerical values.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

# Call the advanced calculator function to run it
advanced_calculator()
