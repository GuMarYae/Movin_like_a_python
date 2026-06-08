from unicodedata import digit  # not actually needed, program does not use it


def main():
    # ask the user to enter a number
    # input() returns text, so we convert it into an integer
    inputNumber = input("Enter an integer between 0 and 999: ");
    number = int(inputNumber);
    
    # call intName() to convert the number into words
    print(intName(number));
    

def intName(number):

    # part stores the portion of the number we are currently processing
    # example: if the number is 777, we will break it down step by step
    part = number;
    
    # name will slowly build the english phrase
    # example: "seven hundred seventy seven"
    name = "";
    
    if(part >= 100): # so say we have 777 the next line will just confirm that its in the 700's
                     # so digitName = 777 // 100 = 7 + hundred
                     # so now, name IS 7 
        
        # integer division extracts the hundreds digit
        # example: 777 // 100 = 7
        name = digitName(part // 100) + " hundred";
        
                     #first time that "part" is actually broken down
                     # Now, part = 777 % 100 = 77
        
        # modulus removes the hundreds and keeps the remainder
        # example: 777 % 100 = 77
        part = part % 100; 
        
        #so its literally breaking down the number into smaller parts each time
        #right here, part is again, 77


    if(part >= 20):
        #this means that name == 7 hundred + the modulus of 77.
        #tensDigit is if part >= 70 then itll add to name, seventy .. so now its seven hundred seventy
        
        # numbers 20-99 follow the pattern "twenty, thirty, forty..."
        # tensDigit() finds the correct tens word
        name = name + " " + tensDigit(part)
        
        #now, part = 77 % 10 which is 7
        
        # remove the tens digit so we only keep the ones place
        part = part % 10


    elif (part >= 10):
        # we use ELIF here because numbers 10-19 are special cases in English
        # example: 13 = "thirteen", not "ten three"
        #
        # if we used another "if", both blocks could run and break the logic
        #
        # example with bad logic:
        # if part >= 20
        # if part >= 10
        #
        # then a number like 13 could be processed incorrectly
        #
        # elif guarantees that ONLY ONE of these sections runs
        
        name = name + " " + teensDigit(part);
        
        # after processing teen numbers, nothing is left
        part = 0;


    if(part > 0):
        # if a digit remains (1 through 9)
        # convert it to its word form
        name = name + " " + digitName(part);
        
    
    # return the completed english phrase
    return name;
    


def digitName(digit):
    # converts a single digit into its english word
    
    if digit == 1:
        return "one"
    if digit == 2:
        return "two"
    if digit == 3:
        return "three"          
    if digit == 4:
        return "four"
    if digit == 5:
        return "five"
    if digit == 6:
        return "six"
    if digit == 7:
        return "seven"
    if digit == 8:
        return "eight"
    if digit == 9:  
        return "nine"
    if digit == 0:   
        return "zero"
    
    # return empty if nothing matched
    return "";
        


def teensDigit(digit):
    # handles numbers from 10 to 19
    # these numbers are irregular in English
    
    if digit == 10:
        return "ten"
    if digit == 11:
        return "eleven"
    if digit == 12:
        return "twelve"          
    if digit == 13:
        return "thirteen"
    if digit == 14:
        return "fourteen"
    if digit == 15:
        return "fifteen"
    if digit == 16:
        return "sixteen"
    if digit == 17:
        return "seventeen"
    if digit == 18:  
        return "eighteen"
    if digit == 19:   
        return "nineteen"
    
    return "";


def tensDigit(digit):
   # returns the tens word for numbers 20-99
   # important: check from largest to smallest
   # because Python stops at the first true condition

   if digit >= 90:
        return "ninety"
   if digit >= 80:
        return "eighty"
   if digit >= 70:
        return "seventy"
   if digit >= 60:
        return "sixty"      
   if digit >= 50:
        return "fifty"
   if digit >= 40:
        return "forty"
   if digit >= 30:
        return "thirty"
   if digit >= 20:    
        return "twenty"

   return "";  


# program starts here
main();