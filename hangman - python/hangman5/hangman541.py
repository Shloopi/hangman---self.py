def func(num1, num2):
    """ this function returns the sum of two integer numbers.
    
    Args:
        num1 (int): an integer number.
        num2 (int): an integer number.
    """
    return num1 + num2


def main():
    help(func)
    print(func(3, 5))
    print(func(4, 6))
    print(func(7, 8))
    
if __name__ == "__main__":
    main()
    