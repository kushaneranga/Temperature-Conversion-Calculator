print("*** Converting the Fahrenheit Celsius ***")
print("Convert Celsius to Fahrenheit: type-F ")
print("Convert Fahrenheit to Celsius: type-C ")
inp = input("What do you want: ")
if inp == "F":
    fahrenheit = float(input("Enter the Temperature in Celsius: "))
    f = (fahrenheit * 1.8) + 32
    print("Fahrenheit: ", f)
elif inp == "C":
    celsius = float(input("Enter the Temperature in fahrenheit: "))
    c = (celsius - 32) * 5 / 9
    print("Celsius: ", c)
print("Thank You!")
