# Understanding Temp Swapping

Sometimes we want the bigger number first so subtraction does not give a negative answer.

Example:

```text
number1 = 5
number2 = 10
```

Without swapping:

```text
5 - 10 = -5
```

After swapping:

```text
10 - 5 = 5
```

## My Understanding

`temp` is assigned `number1`, which is `5`. At that exact moment, `temp` gets its **own copy** of the value `5`. It does **not** stay connected to `number1`.

```text
temp = number1

temp = 5
number1 = 5
number2 = 10
```

Next, `number1` is assigned `number2`, which is `10`. This changes `number1` to `10`, but it does **not** change `temp` because `temp` already copied the value `5`.

```text
number1 = number2

temp = 5
number1 = 10
number2 = 10
```

Finally, `number2` is assigned `temp`. Since `temp` still contains `5`, `number2` becomes `5`.

```text
number2 = temp

temp = 5
number1 = 10
number2 = 5
```

The reason this works is because code executes **from top to bottom**. Each line finishes before the next one starts.

The biggest idea to remember is:

> Assignment (`=`) copies the value on the right into the variable on the left. It does **not** create a permanent connection between the variables.

## Step by Step

```text
Start:
number1 = 5
number2 = 10

temp = number1

temp = 5
number1 = 5
number2 = 10

number1 = number2

temp = 5
number1 = 10
number2 = 10

number2 = temp

temp = 5
number1 = 10
number2 = 5
```

Final result:

```text
number1 = 10
number2 = 5
```

## Common Way (Works in Most Languages)

```python
temp = number1
number1 = number2
number2 = temp
```

## Python Shortcut

Python lets you swap both variables in one line:

```python
number1, number2 = number2, number1
```

This is shorter, but the `temp` method is the one you'll commonly see across many programming languages.

## Example

```python
import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Swap so the larger number comes first.
# This avoids a negative subtraction answer unless one is intended.
if (number1 < number2):
    temp = number1
    number1 = number2
    number2 = temp

answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

if (number1 - number2 == answer):
    print("You are correct!")
else:
    print("Your answer is wrong.")
```
