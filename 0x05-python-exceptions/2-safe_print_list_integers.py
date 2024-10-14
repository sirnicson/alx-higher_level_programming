#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    for i in range(x):
        try:
            # Try to print the current item as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip if the current item is not an integer
            continue
        except IndexError:
            # Handle the case where x exceeds the length of my_list
            break
    print()  # Print a newline after all integers have been printed
    return count
