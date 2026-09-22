#!/usr/bin/env python3
first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
quotient = first / second
if quotient.is_integer():
    quotient = int(quotient)
print(f"{first} / {second} = {quotient}")
print(f"{first} * {second} = {first * second}")
