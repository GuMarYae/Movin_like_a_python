def main():

    def printTriangle(number):
        if number < 1:                 # this is the base case
            return                     # when number reaches 0, the function stops

        printTriangle(number - 1)      # Python keeps calling this line with smaller numbers
                                       # 4 calls 3, 3 calls 2, 2 calls 1, 1 calls 0
                                       # think of it like the number quickly getting smaller each time
                                       # but really this same line keeps calling the function again
                                       # those function calls are stored in the stack until it reaches 0
                                       # then each waiting call continues with the same next instruction
                                       # in other words, the print line does not happen yet
                                       # it must finish going down first

        print("." * number)            # after the function finally reaches 0, it stops going down
                                       # now all the paused function calls that were waiting can finish
                                       # recursion uses LIFO, which means last in, first out
                                       # so the call with 1 finishes first, then 2, then 3, and keeps going up
                                       # that means Python prints the smallest line first and the biggest line last
                                       # because of that, the triangle grows upward in the correct order
                                       # if it printed 100 first, then 99, then 98, the triangle would be upside down

    num = input("enter a number: ")    # asks the user to type a number
    number = int(num)                  # changes the input from text into an integer
    printTriangle(number)              # starts the recursive function

main() #really dont need a main for this code but 
       #practicing it for bigger projects is imparative