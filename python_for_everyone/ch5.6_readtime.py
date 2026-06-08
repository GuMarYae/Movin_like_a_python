#this code show how to reuse a function

def main():
    print("Please enter a time: hours, the minutes. ");
#this has to become true before the next line is invoked
    hours = readIntBetween(0, 23);
#then this has to become true finally
    minutes = readIntBetween(0, 59);
    print("You entered ", hours," hours and ", minutes, " minutes.");


def readIntBetween(low, high):
    
    def getValue():
        '''
        getValue is vatting the compaisins from hours cause the readIntBetween() is being called
        so the first time its comparing from 0 and 23, its not even on the minutes variale name yet
        look at line 7, hours is being called as a function so its stuck there until we enver ONE value 
        bigger than 0 and less than 23
        
        thennn, it askes the same question for miniues variable name
        
        put it like this, normally a variable name sotres a value but thiese variable names are 
        inviking functions autimatically until the functions are satisfied, boom
        
        '''
        return int(input("Enter a value between " + str(low) + " and " + str(high) + " :"))
        
    value = getValue()   
    
    while (value < low or value > high):
        print ("Out of range, try again.");
        value = getValue();
        
    return value;
   
main()
        
        