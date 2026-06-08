myList = [11,22,43,44,55,66,77,88,99,1010]

for eachElement in myList:
    if (eachElement > 0):
        #end doesnt make a new line
        #by default, python does print (something, end = "\n") we juast dont want it to make a new line
        print("| ", end = "")
        print(eachElement, " ",end = "")
#this just removes the little % prompt thats aadded 
#without it: | 11  | 22  | 43  | 44  | 55  | 66  | 77  | 88  | 99  | 1010  %   
print()

for eachElement in range(len(myList)):
    if (eachElement > 0):
        #end doesnt make a new line
        #by default, python does print (something, end = "\n") we juast dont want it to make a new line
        print("| ", end = "")
        print(myList[eachElement], " ",end = "")
print()