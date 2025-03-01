# Inducil, Raphael Clouiee A.
# BSCpE 1-2
# 3/1/2025
# Practice Activity for Object Oriented Programming
# Menu for program 1-10 (11 is exit)

print("Menu")
print("1. Greater number between two numbers")
print("2. Check If Two Numbers Are Equal")  
print("3. Sum of Two Numbers")
print("4. Product of Two Numbers")
print("5. Quotient of Two Numbers (Decimal Format)")
print("6. Exponentiation: First Number Raised to Second")
print("7. Sum of Ten Numbers")
print("8. Count of Odd Numbers Among Ten Inputs")
print("9. Even Numbers from 0 to 100 (Using For Loop)")
print("10. Numbers from 0 to 100 (Except Those Ending in Zero)")
print("11. Exit")

def repeat():
    answer = input("Do you want to run another program? (yes or no): ").lower()
    return answer == "yes" or answer == "y"

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1. Greater number between two numbers")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        elif num1 < num2:
            print(f"{num2} is greater than {num1}")
        else:
            print(f"{num1} and {num2} are equal")

    elif choice == 2:
        print("2. Check If Two Numbers Are Equal")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num1 == num2:
            print(f"{num1} and {num2} are equal")
        else:
            print(f"{num1} and {num2} are not equal")

    elif choice == 3:
        print("3. Sum of Two Numbers")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")

    elif choice == 4:
        print("4. Product of Two Numbers")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The product of {num1} and {num2} is {num1 * num2}")

    elif choice == 5:
        print("5. Quotient of Two Numbers (Decimal Format)")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"The quotient of {num1} and {num2} is {num1 / num2}")

    elif choice == 6:
        print("6. Exponentiation: First Number Raised to Second")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} raised to the power of {num2} is {num1 ** num2}")

    elif choice == 7:
        print("7. Sum of Ten Numbers")
        total = sum(int(input(f"Enter number {i+1}: ")) for i in range(10))
        print(f"The sum of the ten numbers is {total}")

    elif choice == 8:
        print("8. Count of Odd Numbers Among Ten Inputs")
        total = sum(1 for i in range(10) if int(input(f"Enter number {i+1}: ")) % 2 != 0)
        print(f"The number of odd numbers among the ten inputs is {total}")

    elif choice == 9:
        print("9. Even Numbers from 0 to 100 (Using For Loop)")
        for i in range(101):
            if i % 2 == 0:
                print(i, end=" ")
        print()

    elif choice == 10:
        print("10. Numbers from 0 to 100 (Except Those Ending in Zero)")
        for i in range(101):
            if i % 10 != 0:
                print(i, end=" ")
        print()

    elif choice == 11:
        print("11. Exit")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 11.")

    if not repeat():
        break
