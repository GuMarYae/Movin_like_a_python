# Programming Vocabulary (Most Important First)

- **Reference**: A name that refers to or points to an object or variable.
  - **Colloquially:** "Points to it" or "is connected to it."
  - Example:

    ```python
    x = [1, 2, 3]
    y = x
    ```

    `y` references the same list as `x`.

- **Denote**: To represent or stand for something.
  - **Colloquially:** "Means" or "stands for."
  - Example:

    ```python
    x = 10
    ```

    `x` denotes the value `10`.

- **Invoke**: To call or execute a function or method.
  - **Colloquially:** "Run it" or "call it."
  - Example:

    ```python
    print("Hello")
    ```

    `print()` is invoked.

- **By convention**: A commonly accepted way of writing code. Not required by the language, but considered good practice.
  - **Colloquially:** "That's just how programmers normally do it."
  - Example:

    ```python
    first_name = "Tony"
    ```

    Variables are by convention written in `snake_case`.

- **Omit / Omitted**: To leave something out.
  - **Colloquially:** "Leave it out" or "don't include it."
  - Example:

    ```python
    print("Hello")
    ```

    Parentheses cannot be omitted in Python 3.

- **Instantiate**: To create an object from a class.
  - **Colloquially:** "Make an object from the blueprint."
  - Example:

    ```python
    person = Person()
    ```

    `Person()` instantiates a new object.

- **Implement / Implementation**: The actual code that makes something work.
  - **Colloquially:** "How you actually made it work" or "the code behind it."
  - Example:

    ```python
    def add(a, b):
        return a + b
    ```

    The body of `add()` is its implementation.

- **Initialize**: To give a variable or object its starting value.
  - **Colloquially:** "Give it its starting value."
  - Example:

    ```python
    count = 0
    ```

- **Access**: To use or retrieve a variable, object, or function.
  - **Colloquially:** "Get to it" or "use it."
  - Example:

    ```python
    print(x)
    ```

- **Modify**: To change an existing value.
  - **Colloquially:** "Change it."
  - Example:

    ```python
    numbers[0] = 100
    ```

- **Declare**: To introduce a variable, function, or class.
  - **Colloquially:** "Tell the program this thing exists."
  - Example (C++):

    ```cpp
    int age;
    ```

- **Define**: To provide the actual code or implementation.
  - **Colloquially:** "Tell the program exactly what it is or what it does."
  - Example:

    ```python
    def greet():
        print("Hi")
    ```

- **Assign**: To give a value to a variable using `=`.
  - **Colloquially:** "Put a value in it" or "give it a value."
  - Example:

    ```python
    x = 25
    ```

- **Parameter**: The variable listed in a function definition.
  - **Colloquially:** "The placeholder waiting for a value."
  - Example:

    ```python
    def add(a, b):
    ```

    `a` and `b` are parameters.

- **Argument**: The value passed into a function.
  - **Colloquially:** "The actual value you give it."
  - Example:

    ```python
    add(5, 10)
    ```

    `5` and `10` are arguments.

- **Return**: To send a value back from a function.
  - **Colloquially:** "Send the answer back."
  - Example:

    ```python
    return total
    ```

- **Scope**: Where a variable can be accessed.
  - **Colloquially:** "Where you're allowed to use it."

- **Global**: Accessible throughout the program.
  - **Colloquially:** "Everybody can get to it."

- **Local**: Accessible only inside its function or block.
  - **Colloquially:** "Only available in here."

- **Instance**: A specific object created from a class.
  - **Colloquially:** "One actual object made from the blueprint."
  - Example:

    ```python
    dog = Dog()
    ```

- **Attribute**: A variable that belongs to an object.
  - **Colloquially:** "A piece of data that belongs to that object."
  - Example:

    ```python
    dog.name
    ```

- **Method**: A function that belongs to a class or object.
  - **Colloquially:** "A function the object/class can do."
  - Example:

    ```python
    dog.bark()
    ```

- **Pass**: To send data into a function.
  - **Colloquially:** "Give it something to work with."
  - Example:

    ```python
    add(5, 10)
    ```

- **Import**: To bring code from another module into your program.
  - **Colloquially:** "Bring some outside code in so I can use it."
  - Example:

    ```python
    from math import sqrt
    ```

- **Module**: A Python file containing code.
  - **Colloquially:** "Another Python file with useful code in it."

- **Library**: A collection of modules.
  - **Colloquially:** "A collection of code somebody already built for you to use."

- **Mutable**: Can be changed after creation.
  - **Colloquially:** "You can change it."
  - Example:

    ```python
    myList = [1, 2, 3]
    myList[0] = 100
    ```

- **Immutable**: Cannot be changed after creation.
  - **Colloquially:** "You can't change the original."
  - Example:

    ```python
    name = "Tony"
    ```

    Strings are immutable.

- **Override**: Replace an inherited method with a new implementation.
  - **Colloquially:** "The child class says, 'I'm doing this my own way.'"

- **Overload**: Multiple functions or constructors with the same name but different parameters (language dependent).
  - **Colloquially:** "Same function name, different versions depending on what you give it."

- **Recursion**: A function calling itself.
  - **Colloquially:** "The function runs itself again."

- **Encapsulation**: Hide implementation details and protect data.
  - **Colloquially:** "Keep the data protected and control how people mess with it."

- **Abstraction**: Separate the use of a function from its implementation.
  - **Colloquially:** "You know how to use it without needing to know all the shit happening behind the scenes."

- **Inheritance**: A class can inherit the data and methods of another class.
  - **Colloquially:** "The child class gets stuff from the parent class."

- **Polymorphism**: The same method can have different implementations depending on the object or class.
  - **Colloquially:** "Same command, different behavior depending on who's doing it."

---

# More Obvious Terms (Still Important)

- **Object**: An instance of a class.
  - **Colloquially:** "The actual thing created from the blueprint."

- **Class**: A blueprint for creating objects.
  - **Colloquially:** "The blueprint."

- **Variable**: A named storage location for data.
  - **Colloquially:** "A name holding a value."

- **Function**: A reusable block of code.
  - **Colloquially:** "A chunk of code you can run whenever you need it."

- **Expression**: Code that produces a value.
  - **Colloquially:** "Code that gives you an answer."
  - Example:

    ```python
    5 + 3
    ```

- **Statement**: A complete instruction.
  - **Colloquially:** "Tell the computer to do something."
  - Example:

    ```python
    x = 5
    ```

- **Literal**: A value written directly in code.
  - **Colloquially:** "The actual value typed directly into the code."
  - Examples:

    ```python
    10
    "Hello"
    True
    ```

- **Identifier**: The name of a variable, function, class, or module.
  - **Colloquially:** "The name you gave something."
  - Example:

    ```python
    age = 25
    ```

    `age` is the identifier.

- **Concatenate**: To join strings together.
  - **Colloquially:** "Stick strings together."
  - Example:

    ```python
    "Hello " + "Tony"
    ```

- **Iterate**: To repeat through a loop or collection.
  - **Colloquially:** "Go through each one."
  - Example:

    ```python
    for item in myList:
    ```

- **Compile**: To translate source code into machine code.
  - **Colloquially:** "Convert your code into something the computer can run."

- **Interpret**: To execute code through an interpreter rather than compiling it ahead of time.
  - **Colloquially:** "Python reads and runs your code as the program is running."

- **Syntax**: The rules for writing code correctly.
  - **Colloquially:** "The grammar rules of programming."

- **Semantic (Semantics)**: The meaning or behavior of the code.
  - **Colloquially:** "What the code actually means/does."
  - Example:

    ```python
    x = "5" + "5"
    ```

    The syntax is correct, but the semantics produce `"55"` instead of `10`.

---

# Professor Words to Watch For

- **Reference** → "points to"
- **Denote** → "means / stands for"
- **Invoke** → "call / run"
- **By convention** → "how programmers normally do it"
- **Omit** → "leave out"
- **Instantiate** → "create an object"
- **Implementation** → "the actual code/how it works"
- **Parameter** → "placeholder"
- **Argument** → "actual value passed in"
- **Identifier** → "the name"
- **Mutable** → "can change"
- **Immutable** → "can't change"
- **Scope** → "where you can use it"
- **Encapsulation** → "protect/control the data"
- **Abstraction** → "hide the behind-the-scenes details"
- **Inheritance** → "child gets stuff from parent"
- **Polymorphism** → "same method, different behavior"
