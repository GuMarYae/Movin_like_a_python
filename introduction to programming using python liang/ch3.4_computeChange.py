# Ask the user to enter a dollar amount.
# Example: 10.99 means 10 dollars and 99 cents.
# amount = eval(input("Enter the money amount. For example, 10.99. Go: "))

# Hardcode a value so I don't have to type it every time I test.
amount = eval("10.99")


# Turn the dollar amount into cents.
# 10.99 becomes 1099.
# Whole numbers are easier to work with than decimals.
allIntoCents = int(amount * 100)
print("$", amount, "is", allIntoCents, "total pennies.")


# Figure out how many whole dollars we have.
# Below gives us the whole number and throws away anything after the decimal.
# 1099 // 100 = 10
numberOfDollars = allIntoCents // 100
print("Dollars:", numberOfDollars)


# Remove the dollars and keep only the leftover cents.
# % gives us whatever is left after the dollars are taken out.
# 1099 % 100 = 99
remainingCents = allIntoCents % 100
print("Remaining cents:", remainingCents)


# Figure out how many quarters fit into the remaining cents.
# We use remainingCents because the dollars are already gone.
# 99 // 25 = 3
quartersFromRemainingCents = remainingCents // 25
print("Quarters:", quartersFromRemainingCents)


# We don't need the 25 cents anymore because it's already a quarter.
# % 25 removes that part and keeps only the remaining cents.
# 99 % 25 = 24
remainingCents = remainingCents % 25
print("Remaining cents:", remainingCents)


# Figure out how many dimes fit into the remaining cents.
# 24 // 10 = 2
dimesFromRemainingCents = remainingCents // 10
print("Dimes:", dimesFromRemainingCents)


# We don't need the 10 cents anymore because it's already a dime.
# % 10 removes that part and keeps only the remaining cents.
# 24 % 10 = 4
remainingCents %= 10 # 💥 this way is equivilent
print("Remaining cents:", remainingCents)


# Figure out how many nickels fit into the remaining cents.
# 4 // 5 = 0
nickelsFromRemainingCents = remainingCents // 5
print("Nickels:", nickelsFromRemainingCents)


# We don't need the 5 cents anymore because it's already a nickel.
# % 5 removes that part and keeps only the remaining cents.
# 4 % 5 = 4
# NOTE:  ☝🏾
# If the number is smaller than the divisor, nothing can be divided out.
# That means % leaves the number unchanged.
#
# Examples:
# 4 % 5 = 4
# 3 % 10 = 3
# 2 % 25 = 2
#
# No groups fit, so nothing gets removed.
remainingCents = remainingCents % 5
print("Remaining cents:", remainingCents)


# Whatever is left has to be pennies.
# There are no smaller coins left to count.
penniesFromRemainingCents = remainingCents
print("Pennies:", penniesFromRemainingCents)