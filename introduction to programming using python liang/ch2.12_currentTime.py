# Going to use the time module to help display the current time.
import time

# Get the current time in seconds since Jan. 1, 1970 (Unix Epoch).
currentTime = time.time()
# print(currentTime)

# Remove the decimal part.
# You can use either int() or // whenever you want a whole number.
secondsTOT = int(currentTime)
# print(secondsTOT)

# % 60 returns the current second (0 to 59).
currentSecond = int(secondsTOT % 60)

# Convert total seconds into total minutes.
# You can use either int() or // to get a whole number.
totalMinutes = int(secondsTOT / 60)

# % 60 returns the current minute (0 to 59).
currentMinute = int(totalMinutes % 60)

# Convert total minutes into total hours.
# You can use either int() or // to get a whole number.
totalHours = int(totalMinutes / 60)

# % 24 returns the current hour (0 to 23).
currentHour = totalHours % 24

# Display the current GMT time.
print("The current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")