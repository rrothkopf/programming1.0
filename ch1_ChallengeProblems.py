# PROBLEM 1
chair_price = 189.99
tax_percent = .095

print("$" + "{:.2f}".format ((chair_price * 8) + ((chair_price * 8) * tax_percent)))

# PROBLEM 2
count = float(input("Enter an amount in USD: "))

dollar = count // 1
quarter = (count - (dollar * 1)) // .25
dime = (count - (dollar * 1) - (quarter * .25)) // .1
nickel = (count - (dollar * 1) - (quarter * .25) - (dime * .1)) // .05
penny = round((count - (dollar * 1) - (quarter * .25) - (dime * .1) - (nickel * .05)) / .01)

print("Dollars :" , dollar , "\nQuarters:" , quarter , "\nDimes: " , dime , "\nNickels: ", nickel , "\nPennies: ", penny)