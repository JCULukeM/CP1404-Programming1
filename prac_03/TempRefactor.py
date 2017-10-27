"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result:", (celsius), "C°")

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        convert_to_fahrenheit(celsius)
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("fahrenheit: "))
        convert_to_celsius(fahrenheit)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")