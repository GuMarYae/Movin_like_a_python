# Enter the interest rate as a percentage.
# Example: 7.5
annualInterestRate = eval(input("Enter the interest rate: "))

# Convert the annual interest rate into a monthly decimal rate.
# Divide by 1200 because:
# 100 changes the percent into a decimal.
# 12 changes the yearly rate into a monthly rate.
monthlyInterestRate = annualInterestRate / 1200

# Enter the number of years for the loan.
numberOfYears = int(input("Enter the number of years: "))

# Enter the amount of money being borrowed.
loanAmount = float(input("Enter the loan amount: "))

# Calculate the EXACT monthly payment.
# We call it "raw" because it contains all the decimal places.
# Example:
# rawMonthlyPayment = 1013.37498529183
rawMonthlyPayment = loanAmount * monthlyInterestRate / (
    1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)
)

# Calculate the EXACT total payment.
# This is also "raw" because it still has all the decimal places.
rawTotalPayment = rawMonthlyPayment * numberOfYears * 12

# Make the monthly payment look like money.
# *100 moves the decimal 2 places right.
# int() removes everything after the decimal.
# /100 moves the decimal back 2 places.
# Example:
# 1013.37498529183 -> 1013.37
monthlyPayment = int(rawMonthlyPayment * 100) / 100

# Do the same thing for the total payment.
totalPayment = int(rawTotalPayment * 100) / 100

# Print the finished values.
print("The monthly payment is", monthlyPayment)
print("The total payment is", totalPayment)