#This program cumputes the volumes of two cubes

def cubeVolume(param1):
    volume = param1 ** 3;
    return volume

def main():
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)
    print("The volume for result 1 is : ", result1)
    print("The volume for result 2 is : ", result2)
    
    
#since the source code is only functions, you have to call the main function to execute the program
main()