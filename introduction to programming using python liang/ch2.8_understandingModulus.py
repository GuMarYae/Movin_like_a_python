###### we want to figure out what day itll be when the user enters
###### what day it currently is based off them meeting in 10 days

currentDay = eval(input("what day is it currently? monday: 1, tuesday = 2, wednesday = 3, thursday = 4, friday = 5, saturday = 6, sunday = 0: "))

tenDaysFrom_currentDay = (currentDay + 10) % 7

if tenDaysFrom_currentDay == 1:
        print("Yall wil meet on Monday")
elif tenDaysFrom_currentDay == 2:
        print("Yall gon meet on Tuesday")
elif tenDaysFrom_currentDay == 3:
    print("Yall gon meet on Wednesday")
elif tenDaysFrom_currentDay == 4:
    print("Yall gon meet on Thurdsday")
elif tenDaysFrom_currentDay == 5:
    print("Yall gon meet on Friday")
elif tenDaysFrom_currentDay ==6:
    print("Yall gon meet on Saturday")
elif tenDaysFrom_currentDay == 0:
    print("Yall gon meet on Sunday")
else: print("Youve entered an invalid number")

###########################################################################################
# % returns the remainder after division.
# Use it whenever you need the leftover amount.
# think of the word, remains
###########################################################################################
## If today is Tuesday, what day of the week will it be in 100 days?

tuesday = 2
dayOneHunna = (tuesday + 100) % 7

if dayOneHunna == 1:
        print("In 100 days Yall wil meet on Monday")
elif dayOneHunna == 2:
        print("In 100 days Yall gon meet on Tuesday")
elif dayOneHunna == 3:
    print("In 100 days Yall gon meet on Wednesday")
elif dayOneHunna == 4:
    print("In 100 days Yall gon meet on Thurdsday")
elif dayOneHunna == 5:
    print("In 100 days Yall gon meet on Friday")
elif dayOneHunna ==6:
    print("In 100 days Yall gon meet on Saturday")
elif dayOneHunna == 0:
    print("In 100 days Yall gon meet on Sunday")
else: print("Youve entered an invalid number")


