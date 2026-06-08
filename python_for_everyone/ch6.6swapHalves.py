def swap(a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        
def main():
    myList = []
    numbers = input("Enter an even length of numbers: ")
    count = 2
    
    while(numbers != "Q"):
        myList.append(float(numbers))
        #invoke again for another entry while in the while loop
        
        numbers = input("Enter value number " + str(count) + "or Q to quit: " )
        count = count + 1
    
    i = 0
    j = len(myList) //2
    
        
    while i < len(myList) // 2 :
        #we'll make a swap function after, we'll put it at the top)
        swap(myList,i,j)
        i += 1
        j += 1
        print(myList)
        
    
        
#never indent main() inside of def main() lol  
main()