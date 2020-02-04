
# PART A - Fahrenheit to Celsius Conversion Calculator
print("Fahrenheit to Celsius Conversion Calculator")

value = int(input("Enter a temperature in Fahrenheit: "))
answer = "{:.2f}".format((value - 32) * (5/9))

print("The temperature in Celsius:", answer + "°C")

# PART B - Area of a Trapezoid Calculator
print("Area of a Trapezoid Calculator")

height = float(input("Enter the height of the trapezoid: "))
bbase = float(input("Enter the length of the bottom base: "))
tbase = float(input("Enter the length of the top base: "))
area = (((bbase + tbase) / 2) * height)

print("The area of the trapezoid is:", area)

# PART C - Original Calculator - Sale Price Calculator
print("Original Calculator - Sale Price Calculator")

original = float(input("Enter the original price of the item: "))
sale = float(input("Enter the discount on the item: "))
final_price = ("{:.2f}".format (original - (original * (sale / 100))))
money_saved = "{:.2f}".format (original * (sale / 100))

print("The final price of the item is", "$" + final_price , "\nYou will save" , "$" + money_saved , "\nThat's a bargain!")


