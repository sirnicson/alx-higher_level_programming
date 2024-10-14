#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            # Check if the index exists in both lists
            a = my_list_1[i]
            b = my_list_2[i]

            # Attempt division
            result = a / b

        except IndexError:
            print("out of range")
            result = 0  # Out of range, set result to 0

        except TypeError:
            print("wrong type")
            result = 0  # Wrong type, set result to 0

        except ZeroDivisionError:
            print("division by 0")
            result = 0  # Division by zero, set result to 0

        finally:
            # Append the result (or 0 in case of an error) to the new list
            new_list.append(result)

    return new_list
