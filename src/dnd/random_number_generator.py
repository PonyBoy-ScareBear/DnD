import random


def rand_int_gen(number_out_of: int = 20) -> int:
    """Generates random number from range of numbers.

    Args:
        number_out_of (int, optional): The end of the range of numbers. Defaults to 20.

    Returns:
        int: Random number from one to whatever was specified.
    """
    integer = random.randint(1, number_out_of)
    return number_out_of, integer
