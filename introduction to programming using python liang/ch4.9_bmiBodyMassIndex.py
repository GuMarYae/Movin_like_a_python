#this is easy to understand code at this point.. its utiliaing the if elif else statements
#prompt the user for weight in pounds

weight = eval(input("Enter your weight , yo: "))
height = eval(input("Bet, now enter your height, in inches that is : "))

CONST_kilogramsPerPound = 0.45359237
CONST_metersPerInch = 0.0254

#compute BMI
weightInKilograms = weight * CONST_kilogramsPerPound
heightInMeters = height * CONST_metersPerInch
bmi = weightInKilograms / (heightInMeters**2)

print("BMI is : ", bmi, ".2f")

if(bmi < 18.5):
    print("Light weight, bruh, lol.")
    
elif(bmi < 25):
    print("Normal")
elif(bmi < 30):
    print("big back ahh")
else: print("All that weight better be in dat ahh")