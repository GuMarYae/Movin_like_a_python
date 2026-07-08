def main():

    j = 4
    k = 2
    i = 3

    # Nested if statement example.
    # The second if only runs if the first if is True.
    if (i > k):
        if (j > k):
            print("Both i and j are bigger than k!")

    # This else lines up with the FIRST if, not the second one.
    # It only runs when i is less than or equal to k.
    else:
        print("i is less than or equal to k")

    # Another nested if example.
    if (i > k):
        if (j > k):
            print("Both i and j are bigger than k!")
        # This else lines up with the SECOND if.
        # It only runs when j is less than or equal to k.
        else:
            print("j is less than or equal to k")



    # ---------------------------------------------------------
    # Nested if/else version
    # ---------------------------------------------------------

    score = 89
    grade = "F"

    if (score == 100):
        grade = "Damn, A ahh"

    else:
        # We are INSIDE the else block.
        if (score >= 90):
            grade = "A"

        else:
            # We are INSIDE another else block.
            if (score >= 80):
                grade = "B"

            else:
                if (score >= 70):
                    grade = "C"

                else:
                    if (score >= 60):
                        grade = "D"

                    else:
                        grade = "F"

    # We moved back to the left because ALL of the if statements are finished.
    # This print() runs no matter which grade was assigned.
    print("You have a:", grade)



    # ---------------------------------------------------------
    # elif version (Cleaner)
    # ---------------------------------------------------------

    score = 99

    if (score == 100):
        grade = "Damn, A ahh"

    # elif lines up with if because it is part of the SAME decision.
    # It is NOT inside the previous if.
    elif (score >= 90):
        grade = "A"

    elif (score >= 80):
        grade = "B"

    elif (score >= 70):
        grade = "C"

    elif (score >= 60):
        grade = "D"

    else:
        grade = "F"

    # Again, we move back to the left because the entire if/elif/else chain is over.
    # This print() always executes.
    print("You have a:", grade)


main()