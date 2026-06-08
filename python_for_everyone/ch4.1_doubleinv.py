# ------------------------------------------------------------
# Purpose:
# This program calculates how many years it takes for an
# initial investment to double using compound interest.
# It keeps adding yearly interest to the balance
# until the balance reaches twice the starting amount.
# ------------------------------------------------------------

# Annual interest rate in percent
rate = 5.00

# Starting amount of money
initial_balance = 1000.0

# Target amount is double the starting balance
target = 2 * initial_balance

# Current balance starts equal to the initial balance
balance = initial_balance

# Counter to track how many years pass
year = 0

# Loop continues as long as balance is less than target
while (balance < target):

    # Increase year counter by 1
    year += 1

    # Calculate interest earned this year
    interest = balance * rate / 100

    # Add interest to the current balance
    balance += interest

# When loop finishes, balance has reached or exceeded target
print("The investment doubled after", year, "years.")