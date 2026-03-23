def add(a, b):
    total = a + b
    return total


print(add(10, 34))


def adder(a, b):
    total = a + b
    print(total)


adder(56, 69)


def sum(args):
    x = 0
    for i in args:
        x += i
    return x


print(sum([1, 2, 3, 4, 5]))

print(sum((1, 2, 3, 4, 5)))


# Default arguments
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Greetings from function")


greetings()
greetings("Evening")
