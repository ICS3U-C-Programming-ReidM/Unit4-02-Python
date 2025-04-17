#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program calculates the factorial of a positive integer

while True:
    user_num = input("Enter a whole number: ")

    try:
        number = float(user_num)

        if not number.is_integer():
            print(user_num, "is not an integer.")
            continue

        number = int(number)

        if number < 0:
            print(user_num, "is not a positive integer.")
            continue

        break  # Valid input

    except ValueError:
        print(user_num, "is not an integer.")

factorial = 1
i = 1

while True:
    factorial *= i
    i += 1
    if i > number:
        break

print("The factorial of", number, "is:", factorial)
