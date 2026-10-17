from OperatorPractice import OperatorPractice
from OperatorPractice import Add
from OperatorPractice import Subtract
from OperatorPractice import Multiply
from OperatorPractice import Divide


s1 = Subtract() # default value is 0 because default constructor is set to 0 in the parens
s2 = Subtract(25)

# s1 - s2 automatically calls s1.__sub__(s2)
# currentObject = s1 holding 0, otherObject = s2 holding 25
print(f"answer is {s1 - s2}") # 0 - 25 = -25


s1 = Subtract(26)

# s1 was reassigned to a new Subtract object holding 26
# s1 - s2 automatically calls s1.__sub__(s2)
print(f"answer is {s1 - s2}") # 26 - 25 = 1


# s1 - s2 returns 1, so subTot now stores 1
subTot = s1 - s2

# This performs s1 - s2 again, so __sub__ is called again
print(f"answer is still {s1 - s2} lets mess around a bit") # 26 - 25 = 1


m1 = Multiply(13)
m2 = Multiply(subTot) # subTot is 1, so m2 is a Multiply object holding 1

# m1 * m2 automatically calls m1.__mul__(m2)
# currentObject = m1 holding 13, otherObject = m2 holding 1
print(f"Now this answer is {m1 * m2}") # 13 * 1 = 13