print("""- Converting the Fahrenheit Celsius  -
Convert Celsius to Fahrenheit: type-F
Convert Fahrenheit to Celsius: type-C""")

inp = input("What do you want: ").upper()
if inp == "F":
    fahrenheit = float(input("Enter the Temperature in Celsius: "))
    f = (fahrenheit * 1.8) + 32
    print("Fahrenheit: ", f)
elif inp == "C":
    celsius = float(input("Enter the Temperature in fahrenheit: "))
    c = (celsius - 32) * 5 / 9
    print("Celsius: ", c)
else:
    print("Please check the character you entered (Also F or C)")
print("-", " ", "END", " ", "-")
