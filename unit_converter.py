def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def km_to_miles(km):
    miles = km * 0.621371
    return miles


def miles_to_km(miles):
    km = miles / 0.621371
    return km


print("Unit Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kilometers to Miles")
print("4. Miles to Kilometers")

choice = input("Choose an option (1-4): ")
value_text = input("Enter the value to convert: ")
value = float(value_text)

if choice == "1":
    result = celsius_to_fahrenheit(value)
    print(f"{value} Celsius is {result} Fahrenheit")
elif choice == "2":
    result = fahrenheit_to_celsius(value)
    print(f"{value} Fahrenheit is {result} Celsius")
elif choice == "3":
    result = km_to_miles(value)
    print(f"{value} kilometers is {result} miles")
elif choice == "4":
    result = miles_to_km(value)
    print(f"{value} miles is {result} kilometers")
else:
    print("Invalid choice.")