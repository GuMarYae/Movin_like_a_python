'''
 This program computes information related to a sequence of grades obtained
 from the user. It computes the number of passing and failing grades, 
 computes the average grade and finds the highest and lowest grade. #
'''  

# initialize counter for passing grades
numPassing = 0

# initialize counter for failing grades
numFailing = 0

# initialize total sum of all grades
total = 0

# initialize count of how many grades were entered
count = 0

# start minimum grade at highest possible value
# so any real grade entered will be lower than this
minGrade = 100.0

# start maximum grade at lowest possible value
# so any real grade entered will be higher than this
maxGrade = 0.0 


# ask user to enter first grade or -1 to stop
gradeInput = input("Enter grade number or -1 to finish: ") 

# convert the string input into a float number
grade = float(gradeInput)

# loop will continue as long as grade is greater than 0
# NOTE: this means 0 and negative numbers will stop the loop
while (grade > 0):

    # check if grade is passing
    if (grade >= 60):
        # increase passing counter
        numPassing += 1
    else:
        # increase failing counter
        numFailing += 1

    # check if current grade is lower than current minimum
    if (grade < minGrade):
        # NOT THE OTHER WAY AROUND. THAT COULD RESULT IN A FAULTY GRADE
        minGrade = grade
        # NOT THE OTHER WAY AROUND. THAT COULD RESULT IN A FAULTY GRADE

    # check if current grade is higher than current maximum
    if (grade > maxGrade):
        # update maximum grade
        maxGrade = grade
        
    # add current grade to running total
    total += grade

    # increase grade counter
    count += 1
            
    # reads the next grade
    gradeInput = input("Enter grade number or -1 to finish: ")

    # CAN USE THE SAME VARIABLE BECAUSE WE ALREADY STORED
    # THE PREVIOUS GRADE VALUE ABOVE
    grade = float(gradeInput)


# only calculate average if at least one grade was entered
if (count > 0):

    # compute average grade
    average = total / count

    # display formatted average to 2 decimal places
    print("The average grade is %.2f" % average)

    # display number of passing grades
    print("Number of passing grades is", numPassing)

    # display number of failing grades
    print("Number of failing grades is", numFailing)

    # display maximum grade formatted to 2 decimals
    print("The maximum grade is %.2f" % maxGrade)

    # display minimum grade formatted to 2 decimals
    print("The minimum grade is %.2f" % minGrade)