myList = [1, 2, 3, 4, 5, 6]

# range(1, 6) means:
# i = 1, 2, 3, 4, 5
# It STARTS at 1 and STOPS BEFORE 6.
for i in range(1, 6):

    # IMPORTANT: Don't get confused by myList[i - 1].
    #
    # LEFT side of =  means the LOCATION being changed.
    # RIGHT side of = means the VALUE being taken/read.
    #
    # myList[i - 1] = myList[i]
    #
    # When i = 1:
    # myList[1 - 1] = myList[1]
    # myList[0] = myList[1]
    # myList[0] = 2
    #
    # So index 0 changes from 1 to 2.
    #
    # BEFORE:
    # [1, 2, 3, 4, 5, 6]
    #
    # AFTER FIRST LOOP:
    # [2, 2, 3, 4, 5, 6]
    #
    # LEFT = receives the value
    # RIGHT = gives the value
    myList[i - 1] = myList[i]


# After the entire first loop:
# [2, 3, 4, 5, 6, 6]


# range(0, 6) means:
# i = 0, 1, 2, 3, 4, 5
for i in range(0, 6):
    print(myList[i])


# VERY IMPORTANT:
#
# myList[i - 1] can have TWO different jobs
# depending on which side of = it is on.
#
# LEFT SIDE:
# myList[i - 1] = myList[i]
# myList[i - 1] RECEIVES a new value.
#
# RIGHT SIDE:
# myList[i] = myList[i - 1]
# myList[i - 1] GIVES its current value.
#
# SAME myList[i - 1]
# DIFFERENT JOB depending on which side of = it is on.
#
# EASY RULE:
# LEFT = RECEIVES / CHANGES
# RIGHT = GIVES / READS