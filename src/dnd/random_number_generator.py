import random


def single_roll(type_of_dice: int = 20) -> int:
    """Generates random number from range of numbers.

    Args:
        number_out_of (int, optional): The end of the range of numbers. Defaults to 20.

    Returns:
        int: Random number from one to whatever was specified.
    """
    roll = random.randint(1, type_of_dice)
    return roll

# def multiple_rolls(number_of_rolls: int, type_of_dice: int = 6) -> list[int]:
#     for roll in range(number_of_rolls):
#         print(roll)