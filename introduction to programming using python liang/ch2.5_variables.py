def main():

    i = j = k = l = m = n = o = 1;
    print(i,j,k,l,m,n,o);
main()

# using / and // i. idvision
# / uses float division and // uses integer division

print("Float answer is ",5/3, " and integer answer is ", 5//3)

#int vs eval
##using int() cannot be a string of a real number , like a decimal number

print(eval("3.4"))
print("try printing: print(int('3.4'))")


print(int("00000003"))
print("try printing: eval('00000003') with eval. thatll crash. so they have their pros and cons")