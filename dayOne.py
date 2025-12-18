import math

# this is what we have so far 

# course = "Python for Beginners"

# len(course)          # how many characters in the string
# course.upper()       # whole string to uppercase
# course.lower()       # whole string to lowercase
# course.title()       # Each Word Gets Capitalized
# course.find("Py")    # finds where "Py" starts (gives index number)
# course.replace("Beginners", "Pros")   # swaps text

# "Python" in course   # True/False → checks if word exists in the string


# full_name = "John Smith"
# age = 20
# is_new_patient = False

#basically cin or Scanner cin = new Scanner(System.in)
name = input('what is your name ')


#anything from input is automatically characters of a string
year = input("what year were you born ");
#you would have to convert it into an int long etc if you want to add mult subt etc
year_integer = int(year);

age = 2025 - year_integer;

f"..."  # f-string: Python's shortcut. Anything in { } gets replaced with the value.
        # It's the easiest way to build a sentence using variables.

print (f"you are about  {age}  years old" );

#count the indexes in the string
#get an index
name = "Tony Daniels";
print(f"total characters/indexes in  {name} is {len(name)} letters");
print(f"the index number 5 in {name} is letter {name[5]}")
#to upper cas. Note this takes the string and makes a brqnd new string
name_upper = name.upper();
#lowercase
name_lower = name_upper.lower()+ " updated";
print(name_upper);
print(name_lower);

print(name.find("a" or "e" or"i" or "o" or "u" ))
prod_name = name.replace("Daniels", "MarYae")
print(prod_name);
#to see if  "typed word" is in name: boolean value
print("Tony" in name)
#________________________________________________________________
print("########################################")
x = 3.3
y = int(x)
print (y);

a = 10/3
b = 10//3
print(f"a ={a} and b is simply {b} because of the //. it makes it into a floor or int")
c = 10+3*2**3;
print(f"PEMDAS: the ** is exponents so 2^3 then 8*3 then 24 + 10 is: {c}");
print()
print(''' also this is fire
      i use this in discord well its a bit different this one
      the discord one is next to the number 1, while this one im using is near the letter l''')

d = abs(-10.256);
print(f"absolute value of -{d} = {d}")
print(f"floor of {d} is ({math.floor(d)}");
