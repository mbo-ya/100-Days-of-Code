import locale # format currency values

# set locale to user default
locale.setlocale(locale.LC_ALL, '')

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? Ksh"))
split_ways = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

each_to_pay = locale.currency((total_bill + ((tip/100) * total_bill)) / split_ways)

print("Each person should pay: " + str(each_to_pay))