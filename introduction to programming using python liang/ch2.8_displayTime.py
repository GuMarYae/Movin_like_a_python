# user enters input
seconds = eval(input("Enter an integer in seconds: "))
print("you entered",seconds, " seconds")

minutes = seconds//60 #minutes in seconds
print(seconds, " seconds is ", minutes," minutes")

remainingSeconds = seconds % 60
print("remaining seconds is ", remainingSeconds, " seconds")
# % returns the remainder after division.
# Use it whenever you need the leftover amount.

#final
print(seconds, " seconds is ", minutes, " minutes and ", remainingSeconds, " seconds")