"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When you enter a non valid numbers like '?,<,@'
2. When will a ZeroDivisionError occur?
When you try to divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    denominator = 0
    numerator = int(input("Enter the numerator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")