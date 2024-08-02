degrees_fahrenheit  = input("Enter temperature in Fahrenheit: ")
degrees_fahrenheit  = float(degrees_fahrenheit)
degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")