import random


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
