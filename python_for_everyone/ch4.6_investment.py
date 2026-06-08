# BY CONVENTION, PYTHON DEVS USE ALL CAPS FOR CERTAIN VARIABLES
# BECAUSE PYTHON DOES NOT HAVE TRUE CONSTANTS
# ALL CAPS TELLS DEVELOPERS NOT TO CHANGE THIS VALUE

# interest rate percentage
RATE = 5.0  # 5 percent yearly interest

# starting amount of money
INITIAL_BALANCE = 10000.0  # initial balance is 10,000


# ask user to enter number of years as text input
numYearsInput = input("Enter the number of years: ")

# convert the string input into an integer
numYears = int(numYearsInput)


# set current balance equal to the starting balance
balance = INITIAL_BALANCE

# loop from year 1 up to and including numYears
for year in range(1, numYears + 1):

    # calculate interest for the current year
    # balance multiplied by rate divided by 100
    interest = balance * RATE / 100

    # add the interest to the current balance
    balance += interest

    # print year and balance in formatted columns
    # %4d FORMATS YEAR AS AN INTEGER WITH MINIMUM WIDTH OF 4 SPACES
    # %10.2f FORMATS BALANCE AS A FLOAT WITH MINIMUM WIDTH OF 10 SPACES
    # .2 MEANS EXACTLY 2 NUMBERS AFTER THE DECIMAL
    # VALUES ARE INSERTED FROM LEFT TO RIGHT
    # year GOES INTO %4d
    # balance GOES INTO %10.2f
    print("%4d %10.2f" % (year, balance))
      