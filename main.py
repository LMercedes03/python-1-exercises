from exercises import ex1, ex2, ex3


def main():
    # ex1 --------------------------------------------------
    ex1.hello_world("3")
    # ex2 --------------------------------------------------
    array = [1, 2, 3]
    result = ex2.array_to_string(array)
    print(result, "\n")
    # ex3 --------------------------------------------------
    array = [1.0, 1.1, "1"]
    result = ex3.add_numbers(array)
    print(result)
    # ex4 --------------------------------------------------

if __name__ == '__main__':
    main()
