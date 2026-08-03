def printMonth(year, month):
    # Print the month title first
    printMonthTitle(year, month)

    # Then print the calendar dates
    printMonthBody(year, month)


def printMonthTitle(year, month):
    # Print the month name and year
    print("            ", getMonthName(month), year)

    # Print the days of the week
    print("Sun Mon Tue Wed Thu Fri Sat")


def printMonthBody(year, month):
    # Find which weekday the 1st of the month falls on
    startDay = getStartDay(year, month)

    # Find how many days are in this month
    numberOfDaysInMonth = getNumberOfDaysInMonth(year, month)

    # Print blank spaces before day 1
    for i in range(startDay):
        print("    ", end="")

    # Print every day of the month
    for i in range(1, numberOfDaysInMonth + 1):
        print(format(i, "4d"), end="")

        # After Saturday, move to the next line
        if (i + startDay) % 7 == 0:
            print()

    # Leave a blank line after the calendar
    print()


def getMonthName(month):
    # Convert a month number into its name
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    elif month == 12:
        monthName = "December"

    return monthName


def getStartDay(year, month):
    # January 1, 1800 was a Wednesday (3)
    START_DAY_FOR_JAN_1_1800 = 3

    # Count all days from Jan 1, 1800 to this month
    totalNumberOfDays = getTotalNumberOfDays(year, month)

    # Convert total days into a weekday (0-6)
    return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7


def getTotalNumberOfDays(year, month):
    total = 0

    # Add every day's count for all previous years
    for i in range(1800, year):
        if isLeapYear(i):
            total += 366
        else:
            total += 365

    # Add every day's count for all previous months
    for i in range(1, month):
        total += getNumberOfDaysInMonth(year, i)

    return total


def getNumberOfDaysInMonth(year, month):
    # Months with 31 days
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    # Months with 30 days
    if month in [4, 6, 9, 11]:
        return 30

    # February depends on whether it's a leap year
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28

    return 0


def isLeapYear(year):
    # Leap year rules:
    # 1. Divisible by 400
    # OR
    # 2. Divisible by 4 but NOT by 100
    return year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )


def main():
    # Get input from the user
    year = int(input("Enter full year: "))
    month = int(input("Enter month as a number: "))

    # Print the requested calendar
    printMonth(year, month)


main()

########################### top down design ################################

#A definition I'd remember is:

# Top down design is designing a program from the highest level (big picture) to the lowest level (small details), creating helper functions as they become needed.

# Or even shorter:

# Top down design = Start with WHAT the program should do, then gradually define HOW each part works.

########################### top down design ################################

# 1. Write main()
#    Decide what the program should do.

# 2. Create printMonth()
#    Since main() calls it.

# 3. Create printMonthTitle()
#    Because printMonth() calls it.

# 4. Create printMonthBody()
#    Because printMonth() also calls it.

# 5. Create getMonthName()
#    Because printMonthTitle() needs it.

# 6. Create getStartDay()
#    Because printMonthBody() needs it.

# 7. Create getNumberOfDaysInMonth()
#    Because printMonthBody() needs it.

# 8. Create getTotalNumberOfDays()
#    Because getStartDay() needs it.

# 9. Create isLeapYear()
#    Because getNumberOfDaysInMonth()
#    and getTotalNumberOfDays() need it.

# 10. Test the program and make fixes.



# main()
# │
# ├── printMonth()
# │   ├── printMonthTitle()
# │   │   └── getMonthName()
# │   │
# │   └── printMonthBody()
# │       ├── getStartDay()
# │       │   └── getTotalNumberOfDays()
# │       │       └── getNumberOfDaysInMonth()
# │       │           └── isLeapYear()
# │       └── getNumberOfDaysInMonth()