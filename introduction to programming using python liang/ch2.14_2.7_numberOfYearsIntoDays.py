# Minutes in one day.
minutesPerDay = 60 * 24
print("Minutes in one day:", minutesPerDay)

# Minutes in one year.
minutesPerYear = minutesPerDay * 365
print("Minutes in one year:", minutesPerYear)

# Ask the user for the total number of minutes.
totalMinutes = eval(input("Enter the total number of minutes: "))
print("Total minutes entered:", totalMinutes)
#################### calculations ##############################################
# Find the total number of whole years.
years = totalMinutes // minutesPerYear
print("Whole years:", years)

# Find the minutes left over after removing the full years.
#                   user number      525600
remainingMinutes = totalMinutes % minutesPerYear
print("Remaining minutes:", remainingMinutes)

# Convert the remaining minutes into whole days.
days = remainingMinutes // minutesPerDay
print("Remaining days:", days)

# Display the final answer.
print()
print(totalMinutes, "minutes is approximately", years, "years and", days, "days.")



###########################################################################################
# 💥💥💥 BEGINNER NOTE ABOUT THE MODULUS (%) OPERATOR 💥💥💥
#
# 😵 The modulus (%) is what confuses a LOT of beginners.
#
# The reason is because you're using TWO variables together:
#
#     remainingMinutes = totalMinutes % minutesPerYear
#
# Instead of thinking:
#
#     "What the heck is modulus?!"
#
# Think:
#
#     "What's LEFT OVER after I remove all the whole years?" 🤔
#
# Example:
#
# totalMinutes = 600000
# minutesPerYear = 525600
#
# First, find the whole years:
#
#     years = totalMinutes // minutesPerYear
#
#     600000 // 525600 = 1
#
# So we know 1 whole year fits.
#
# One whole year uses:
#
#     525600 minutes
#
# We started with:
#
#     600000 minutes
#
# So what's left?
#
#     600000
#   - 525600
#   --------
#      74400 minutes left
#
# Python does ALL of that automatically when you write:
#
#     remainingMinutes = totalMinutes % minutesPerYear
#
# 🚨 THE MENTAL TRICK 🚨
#
# Whenever you see:
#
#     a % b
#
# Think:
#
#     1️⃣ Divide a by b.
#
#     2️⃣ Figure out how many WHOLE times b fits into a.
#
#     3️⃣ Multiply that whole number by b.
#
#     4️⃣ Subtract it from a.
#
#     5️⃣ 🎉 Whatever is LEFT OVER is the answer!
#
# Example:
#
#     600000 % 525600
#
# Step 1️⃣
#
#     600000 // 525600 = 1
#
# Step 2️⃣
#
#     1 * 525600 = 525600
#
# Step 3️⃣
#
#     600000
#   - 525600
#   --------
#      74400 ✅
#
# So:
#
#     600000 % 525600
#
# returns:
#
#     74400
#
# 💡 The biggest thing that helped me understand % was this:
#
#     "Mentally, I divide FIRST...
#      then I subtract the whole groups...
#      and whatever is LEFT OVER is what % returns."
#
# Once you start thinking:
#
#     % = "What's left over?"
#
# instead of:
#
#     % = "Modulus"
#
# these problems become WAY easier. 🚀
###########################################################################################