class Stack:
    def __init__(currentObj, elements = []):
        currentObj.__elements= elements
        

## There is no if statement here. The == operator itself checks a condition and returns True or False.
## Example: 
#       num = 5. Python: print(num == 7) -> False | 
#       Java: System.out.println(num == 7) -> false
##      C++: cout << (num == 7) -> 0/false | 
#       JavaScript/Node: console.log(num == 7) -> false
## So: return len(currentObj.__elements) == 0 is simply asking: "Is the number of elements equal to 0?" True or False.
## i know im used to seeing t or f in for loops while loops but just writing 
#  0=== , 7==5 ect will also push out a t or f
# so this is saying push out a t or f id 0 == 0 or not
    def isEmpty(currentObj):
        return len(currentObj.__elements) == 0
    
    #r you can do 
    def izEmpty(currentObject):
        if len(currentObject.__elements) == 0:
            return True
        else:
            return False
    
# returning the element at the top of the stack
# without remiving it from the stack

## IMPORTANT: currentObj = the Stack object, while currentObj.__elements = the list INSIDE the Stack.
## isEmpty() was created in the Stack class, so use currentObj.isEmpty().
## currentObj.__elements.isEmpty() is wrong because it asks the list to run isEmpty(), and lists don't have that method.
## RULE: Look at which class the method was defined in. An object of that class is what calls the method.
    def peek(currentObj):
        if currentObj.isEmpty():
            return None
    ## YES. It's checking the list inside the current Stack object you created in main().
    ## Example:
    ## stack1 = Stack()
    ## stack1.push(5)
    ## stack1 = the Stack object
    ## The list inside stack1 contains [5].
    ## When you call stack1.isEmpty(), it's basically asking: "Is the list inside stack1 empty?"
    ## Since [5] has one value, the answer is False.
    #######
    ## if true put it to the front
        else:
            return currentObj.__elements[len(currentObj.__elements) -1]
        
    
    ## stores a new element to the top of the stack   
    def push(currentObj, value):
        currentObj.__elements.append(value)
        
    def pop(currentObj):
        if currentObj.isEmpty():
            return None
        else:
            return currentObj.__elements.pop()
        
    def getSize(currentObj):
        return len(currentObj.__elements)