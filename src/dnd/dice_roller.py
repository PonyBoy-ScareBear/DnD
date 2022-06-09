import random


def single_roll(type_of_die: int = 20) -> tuple(int, int):
    """Simulates rolling a single die.

    Args:
        type_of_die (int, optional): Type of die that is being rolled. Defaults to 20.

    Returns:
        type_of_die (int): Type of die that was rolled.
        roll (int): The result of the die roll.
    """
    roll = random.randint(1, type_of_die)
    return type_of_die, roll


def multiple_rolls(number_of_dice: int, type_of_dice: int = 6) -> list[int]:
    """Simulates rolling multiple dice.

    Args:
        number_of_dice (int): The number of dice being rolled.
        type_of_dice (int, optional): The type of dice that are being rolled. Defaults to 6.

    Returns:
        list_of_rolls (list[int]): List of random rolls of dice.
    """
    list_of_rolls = [random.randint(1, type_of_dice) for i in range(number_of_dice)]
    return list_of_rolls
