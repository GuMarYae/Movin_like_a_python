def main():
    # Dictionary of contacts.
    # Key = person's name
    # Value = person's phone number
    myContacts = {
        "Sarah": "228-223-1842",
        "John": "601-555-2381",
        "Alice": "504-555-9173",
        "Bob": "225-555-6428",
        "Martha": "225-555-6428",
        "Charlie": "318-555-7305",
        "David": "850-555-4819",
        "Eve": "251-555-3662",
        "Frank": "985-555-1947"
    }

    # See if Fred is on the list.
    # "Fred" is searched as a KEY, not a value.
    if "Fred" in myContacts:
        print("Fred is in the contact list dictionary:", myContacts["Fred"])
    else:
        print("Fred is not found")

    # Get a list of contacts that all use the number below.
    # findNames() returns a list.
    # That returned list is stored inside nameList.
    nameList = findNames(myContacts, "225-555-6428")

    # Print the heading.
    print("Names for 225-555-6428:", end=" ")

    # Loop through ONLY the matching names.
    for name in nameList:
        print(name, end=" ")

    # Move to the next line.
    print()

    # Print all names and phone numbers.
    printAll(myContacts)


def findNames(dictionary, numberInDictionary):

    # Create an empty list to store matching names.
    nameList = []

    # Loop through every KEY in the dictionary.
    for name in dictionary:

        # name = variable containing "Sarah". So name is a KEY.

        # dictionary[name] = value for that key = 228-223-1842

        # Given:
        # myContacts = {
        #     "Sarah": "228-223-1842",
        #     "John": "601-555-2381",
        # }
        #
        # And:
        # name = "Sarah"
        #
        # Then:
        # myContacts[name]
        #
        # Becomes:
        # myContacts["Sarah"]
        #
        # Which returns:
        # "228-223-1842"

        # Compare the phone number stored in the dictionary
        # with the phone number passed into the function.
        if dictionary[name] == numberInDictionary:

            # 💥 name = variable that holds the key ("Sarah")
            # 💥 myContacts[name] = looks up the value for that key
            # 💥 dictionary[name] = also looks up the value for that key because
            #    'dictionary' is the function parameter that refers to
            #    the myContacts dictionary.
            # 💥 numberInDictionary = the value you're comparing it to.

            # Since the phone numbers match,
            # save ONLY the matching KEY (the person's name).
            #
            # Before:
            # nameList = []
            #
            # After Bob:
            # nameList = ["Bob"]
            #
            # After Martha:
            # nameList = ["Bob", "Martha"]
            nameList.append(name)

    # Return the completed list back to main().
    return nameList


# Print every contact in alphabetical order.
def printAll(contacts):

    print("All names and numbers")

    # sorted() returns the keys in alphabetical order.
    for key in sorted(contacts):

        # key = the person's name.
        # contacts[key] = the phone number that belongs to that name.
        print(key, contacts[key])


# Start the program.
main()