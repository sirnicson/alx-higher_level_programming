#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            num += 1
    except IndexError:
        pass  # Ignore the IndexError if x is larger than the list size
    print()  # Ensure a newline after printing the list
    return num

