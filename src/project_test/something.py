def greet():
    return "hello there"


def other():
    x = greet()
    print(x)


if __name__ == "__main__":
    other()
