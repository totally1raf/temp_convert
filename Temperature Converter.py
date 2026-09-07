print("Hello, this is a temperature converter")
print("As of now, it can convert Celcius into Fahrenheit, Kelvin or Reamur")
print(" ")

print("For converting Celcius into Fahrenheit, type 'Fahrenheit' on the unit selector below")
print("For converting Celcius into Kelvin, type 'Kelvin' on the unit selector below")
print("For converting Celcius into Reamur, type 'Reamur' on the unit selector below")
unit = str(input("Input Unit of Temperature: "))

if unit == "Fahrenheit":
    number_input = float(input("Input number in Celcius: "))
    answer = (number_input * 1.8) + 32
    print(" ")
    print(f"It is {answer} {unit}")
elif unit == "Kelvin":
    number_input = float(input("Input number in Celcius: "))
    answer = number_input + 273.15
    print(" ")
    print(f"It is {answer} {unit}")
elif unit == "Reamur":
    number_input = float(input("Input number in Celcius: "))
    answer = number_input * 0.8
    print(" ")
    print(f"It is {answer} {unit}")
else:
    print("Unit invalid, type 'Fahrenheit' for Fahrenheit, type 'Kelvin' for Kelvin, type 'Reamur' for Reamur when using the converter")