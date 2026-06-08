# Function Definition Rules by Language

## Python

Python cares where functions are placed.

You gotta define the function before you use it.

```python
def main():
    print("Hello")

main()
```

✅ Works

```python
main()

def main():
    print("Hello")
```

❌ Error

Easy rule:

```text
Python = Define first, use later
```

---

## C++

C++ can use function prototypes.

```cpp
void mainFunction();

int main()
{
    mainFunction();
}

void mainFunction()
{
    cout << "Hello";
}
```

✅ Works

The prototype tells C++:

```text
"Trust me bro, this function exists somewhere below."
```

Easy rule:

```text
C++ = Prototype first, define later if you want
```

---

## Java

Java methods can usually be placed anywhere inside the class.

```java
public class Test
{
    public static void main(String[] args)
    {
        hello();
    }

    public static void hello()
    {
        System.out.println("Hello");
    }
}
```

✅ Works

Java already knows about the methods in the class.

Easy rule:

```text
Java = Methods can be anywhere in the class
```

---

## JavaScript / Node.js

Functions are usually hoisted.

```javascript
hello();

function hello()
{
    console.log("Hello");
}
```

✅ Works

JavaScript already knows about the function before it runs.

Easy rule:

```text
JavaScript / Node = Usually doesn't care
```

---

# Quick Cheat Sheet

```text
Python      = Define first

C++         = Prototype first

Java        = Anywhere in the class

JavaScript  = Usually wherever
Node.js     = Usually wherever
```
