# this code reads numbers from the user
# removes the two smallest numbers
# then adds up the remaining numbers

def readFloats():

    values = []  # create an empty list to store the numbers

    print("Please enter values, Q to quit: ")  # tell the user what to do

    userInput = input("")  # read the first value from the keyboard

    while(userInput.upper() != "Q"):  # keep looping until the user enters Q

        values.append(float(userInput))  # convert the input to a float and add it to the list

        userInput = input("Another value or Q to quit: ")  # ask for another value

    return values  # return the completed list of numbers


def removeMinimumValues(values):

    smallestPosition = 0  # assume the first value is the smallest

    for i in range(1, len(values)):  # scan the rest of the list

        for i in range(1, len(values)):  # start at index 1 because index 0 is already being treated 
                                         #as the smallest

            smallestPosition = i  # save the index of the new smallest value

    values.pop(smallestPosition)  # remove the smallest value from the list


def main():

    scores = readFloats()  # get all the scores from the user

    if len(scores) > 1:  # make sure there are at least two values

        removeMinimumValues(scores)  # remove the first smallest value

        removeMinimumValues(scores)  # remove the second smallest value

        tot = sum(scores)  # add up the remaining values

        print(tot)  # display the total

    else:

        print("Atleast two minimum numbers are needed")  # not enough values entered


main()  # start the program