
import sys

# Prompt the user to enter filing status
# 0 = Single
# 1 = Married Filing Jointly
# 2 = Married Filing Separately
# 3 = Head of Household
status = int(input("Enter the filing status: "))

# Prompt the user to enter taxable income
income = float(input("Enter the taxable income: "))

if status == 0:  # Compute tax for single filers

    # ==========================================================
    # Example Used:
    # Filing Status = Single
    # Taxable Income = $50,000
    #
    # The U.S. tax system is progressive.
    # This means different portions of your income are taxed
    # at different tax rates.
    #
    # Income = $50,000
    #
    # First $8,350        -> taxed at 10%
    # Next $25,600        -> taxed at 15%
    # Remaining $16,050   -> taxed at 25%
    #
    # The same $50,000 is NOT taxed at one rate.
    # It is split into tax brackets.
    # ==========================================================

    if income <= 8350:
        # Tax Bracket:
        # $0 to $8,350

        # If income is $8,350 or less,
        # every dollar is taxed at 10%.

        tax = income * 0.10

    elif income <= 33950:
        # Tax Bracket:
        # $8,351 to $33,950

        # The first $8,350 is always taxed at 10%.

        # Everything ABOVE $8,350
        # is taxed at 15%.

        # Example if income were $10,000:
        #
        # First $8,350 -> 10%
        # Remaining $1,650 -> 15%

        tax = 8350 * 0.10 + \
              (income - 8350) * 0.15

    elif income <= 82250:
        # Tax Bracket:
        # $33,951 to $82,250

        # Example:
        # income = $50,000

        # First tax bracket:
        # $0 to $8,350
        # Tax the first $8,350 at 10%.

        # Second tax bracket:
        # $8,351 to $33,950
        # Tax the next $25,600
        # (33,950 - 8,350)
        # at 15%.

        # Third tax bracket:
        # Income above $33,950
        #
        # Remaining income:
        # 50,000 - 33,950 = 16,050
        #
        # Tax ONLY this remaining
        # $16,050 at 25%.

        tax = 8350 * 0.10 + \
              (33950 - 8350) * 0.15 + \
              (income - 33950) * 0.25

    elif income <= 171550:
        # Tax Bracket:
        # $82,251 to $171,550

        # Fill the first three tax brackets completely.

        # First $8,350 -> 10%
        # Next $25,600 -> 15%
        # Next $48,300 -> 25%

        # Tax ONLY the remaining income
        # above $82,250 at 28%.

        tax = 8350 * 0.10 + \
              (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + \
              (income - 82250) * 0.28

    elif income <= 372950:
        # Tax Bracket:
        # $171,551 to $372,950

        # Fill the first four tax brackets completely.

        # First $8,350 -> 10%
        # Next $25,600 -> 15%
        # Next $48,300 -> 25%
        # Next $89,300 -> 28%

        # Tax ONLY the remaining income
        # above $171,550 at 33%.

        tax = 8350 * 0.10 + \
              (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + \
              (171550 - 82250) * 0.28 + \
              (income - 171550) * 0.33

    else:
        # Tax Bracket:
        # Above $372,950

        # Fill the first five tax brackets completely.

        # First $8,350 -> 10%
        # Next $25,600 -> 15%
        # Next $48,300 -> 25%
        # Next $89,300 -> 28%
        # Next $201,400 -> 33%

        # Tax ONLY the remaining income
        # above $372,950 at 35%.

        tax = 8350 * 0.10 + \
              (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + \
              (171550 - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 + \
              (income - 372950) * 0.35

elif status == 1:  # Compute tax for married filing jointly
    print("Left as exercise")

elif status == 2:  # Compute tax for married filing separately
    print("Left as exercise")

elif status == 3:  # Compute tax for head of household
    print("Left as exercise")

else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", format(tax, ".2f"))