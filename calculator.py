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
