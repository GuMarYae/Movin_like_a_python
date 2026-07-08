import random                    # Import the random module (library)

### this is practice on how to use the random import 
    # random = the module (library) that contains random number functions
    # randint = a function inside the random module that returns a random integer
print("This is just a random number generated: ",random.random())
print("This is how you use randint: ",random.randint(1,11))

count = 0                        # Keeps track of how many correct answers the user gets
status = True                    # Controls the while loop (True = keep asking questions)

#genrate random numbers
while (status):                  # Keep looping until the user gets a question wrong


    randomNumber1 = random.randint(1,99)   # Generate a random integer from 1 to 99
    randomNumber2 = random.randint(1,99)   # Generate another random integer from 1 to 99

    # Use + when combining strings into one string (like input()).
    # Use commas when printing multiple values (like print()).
    answer = eval(input("What is " + str(randomNumber1) + " + " + str(randomNumber2) + " ? "))

    # Check if the user's answer matches the correct sum
    if (answer == randomNumber1 + randomNumber2):
        print("Good!")           # Tell the user they got it right
        count += 1               # Increase the number of correct answers by 1
        print("Total correct:", count)   # Print the running total of correct answers
    else:
        status = False           # End the loop because the user answered incorrectly
        print("Wrong!")          # Tell the user they were incorrect
        print("Final score:", count)   # Display the total number of correct answers