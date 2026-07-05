# int vs eval
# int() cannot convert a decimal string like "3.4"

print(eval("3.4"))
print("Try printing: print(int('3.4'))")

print(int("00000003"))
print("Try printing: eval('00000003'). It'll crash, so both have pros and cons.")

############################################################
############ The correct way to use them both ###############
############################################################

# Sales tax

# User enters the purchase amount.
# Example: 197.55
purchaseAmount = eval(input("Enter purchase amount: "))

# Find 6% sales tax.
# 197.55 * 0.06 = 11.853
tax = purchaseAmount * 0.06

# Keep only 2 decimal places.
# 11.853 * 100 = 1185.3
# int(1185.3) = 1185
# 1185 / 100 = 11.85
salesTax = int(tax * 100) / 100

print("Sales tax is:", salesTax)