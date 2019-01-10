"""Functions that manipulate lists without using Python's built-in list methods.

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations.
They include:

    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

Implement functions that each use just one of the above operations.

The docstring of each function describes what it should do.

DO NOT USE ANY OF THE BUILT IN LIST METHODS, OR len()!
"""


def head(input_list):
    """Return the first element of the input list."""

    return input_list[0]


def tail(input_list):
    """Return all elements of the input list except the first."""

    return input_list[1:]


def last(input_list):
    """Return the last element of the input list."""

    return input_list[-1]


def init(input_list):
    """Return all elements of the input list except the last."""

    return input_list[:-1]


##############################################################################
# Do yourself a favor and get a short code review here.

def first_three(input_list):
    """Return the first three elements of the input list."""

    return input_list[:3]


def last_five(input_list):
    """Return the last five elements of the input list."""

    return input_list[-5:]


def middle(input_list):
    """Return all elements of input_list except the first two and the last two."""

    return input_list[2:-2]


def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of input_list."""

    return input_list[2:6]


def inner_four_end(input_list):
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list."""

    return input_list[4:8]


def replace_head(input_list):
    """Replace the head of input_list with the value 42 and return nothing."""
    input_list[0] = 42
    


def replace_third_and_last(input_list):
    """Replace third and last elements of input_list with 37 and return nothing."""

    input_list[2] = 37
    input_list[-1] = 37


def replace_middle(input_list):
    """Replace all elements of a list but the first and last two with 42 and 37."""

    input_list[2:-2] = [42,37]


def delete_third_and_seventh(input_list):
    """Remove third and seventh elements of input_list and return nothing."""

    del input_list[2]
    del input_list[-2]


def delete_middle(input_list):
    """Remove all elements from input_list except the first two and last two."""

    del input_list[2:-2]


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#
# Please ask for a code review from an Education team member before proceeding.
##############################################################################

# This is the part were we actually run the doctests.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
