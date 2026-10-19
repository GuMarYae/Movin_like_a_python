# VERSION 2: Defining fib() OUTSIDE main()
# Keep def fib() at the SAME indentation level as def main().
# Even though fib() is outside main(), main() can still call it.

def main():
    index = int(input("Enter index for a Fibonacci number: "))

    # Call fib() from inside main()
    print("The Fibonacci number at index", index, "is", fib(index))


# Define fib() OUTSIDE main() at the same indentation level
def fib(theIndex):
    if theIndex == 0:
        return 0
    else:
        if theIndex == 1:
            return 1
        else:
            return fib(theIndex - 1) + fib(theIndex - 2) 