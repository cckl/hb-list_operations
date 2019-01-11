"""Custom implementations of several standard Python list methods.

Implement your own versions of Python's standard list methods, as functions.

You should use only the primitive operations from Part 1 and 2 in your
implementations. For loops are also allowed, such as the following:

    for element in some_list:
        # Do something with element

Each function imitates a built-in list method, as described by the docstring
for each function.

Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version.
"""

from list_operations import last


def custom_len(input_list):
    """Return number of items in the list."""

    count = 0

    for num in input_list:
        count += 1
    return count 


# For the next four exercises, you'll need to be clever and think about ways
# to use list slice assignment.
#
# NOTE: these are especially contrived. You wouldn't really want
# to typically append things to a list like this (you'd want to to use the
# list.append() method), but we want you to practice list slicing assignment
# in different ways so it sticks in your brain.


def custom_append(input_list, value):
    """Add the value to the end of the list."""

    input_list[input_list[-1]:] = [value] 

    


def custom_extend(input_list, second_list):
    """Append every item in second_list to input_list."""

    new_index = custom_len(input_list)
    input_list[new_index:] = second_list


    


def custom_insert(input_list, index, value):
    """Insert value at index in the list."""

    input_list[index:index] = [value] 


def custom_remove(input_list, value):
    """Remove the first item of the value in list."""

    for item in input_list:
        if item == value:
            del value 
            break

def custom_pop(input_list):
    """Remove the last item in the list and returns it."""

    last_item = last(input_list)
    del input_list[-1]
    return last_item


def custom_index(input_list, value):
    """Return the index of the first item of value found in input_list."""

    length = custom_len(input_list)
    for index in range(0, length):
        if input_list[index] == value:
            return index


def custom_count(input_list, value):
    """Return the number of times value appears in the list."""

    count = 0
    for item in input_list:
        if item == value:
            count += 1
    return count 

def custom_reverse(input_list):
    """Reverse the elements of the input_list.

    Like input_list.reverse(), custom_reverse(input_list) should reverse the
    elements of the original list and return nothing (we call this reversing
    "in place").

    For example:

        >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        >>> custom_reverse(multiples)
        >>> multiples == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
        True

    """
    length = custom_len(input_list)-1

    for i in range(0, length):
        if length == i:
            break
        else:
            print(input_list)
            last_item = input_list[length]
            input_list[length] = input_list[i]
            input_list[i] = last_item
            length = length - 1
    
    print(input_list)




def custom_contains(input_list, value):
    """Return True or False if value is in the input_list."""

    for item in input_list:
        if item == value:
            return True
    
    return False


def custom_equality(some_list, another_list):
    """Return True if passed lists are identical, False otherwise."""

    length = custom_len(some_list)
    for i in range(0, length):
        if some_list[i] != another_list[i]:
            return False
    
    return True



##############################################################################
# Please ask for a code review. Also, give your partner a high-five!
##############################################################################

# This is the part were we actually run the doctests.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
