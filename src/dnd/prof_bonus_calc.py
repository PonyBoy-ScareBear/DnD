def prof_calc(xp: int = 0) -> int:
    """Calculates proficiency bonus using experience points.

    Args:
        xp (int, optional): Experience Points. Defaults to 0.

    Returns:
        prof_bonus (int): Proficiency Bonus.
    """
    if xp < 300:
        proficiency_bonus = 2
    elif xp < 900:
        proficiency_bonus = 2
    elif xp < 2700:
        proficiency_bonus = 2
    elif xp < 6500:
        proficiency_bonus = 2
    elif xp < 14000:
        proficiency_bonus = 3
    elif xp < 23000:
        proficiency_bonus = 3
    elif xp < 34000:
        proficiency_bonus = 3
    elif xp < 48000:
        proficiency_bonus = 3
    elif xp < 64000:
        proficiency_bonus = 4
    elif xp < 85000:
        proficiency_bonus = 4
    elif xp < 100000:
        proficiency_bonus = 4
    elif xp < 120000:
        proficiency_bonus = 4
    elif xp < 140000:
        proficiency_bonus = 5
    elif xp < 165000:
        proficiency_bonus = 5
    elif xp < 195000:
        proficiency_bonus = 5
    elif xp < 225000:
        proficiency_bonus = 5
    elif xp < 265000:
        proficiency_bonus = 6
    elif xp < 305000:
        proficiency_bonus = 6
    elif xp < 355000:
        proficiency_bonus = 6
    else:
        proficiency_bonus = 6
    prof_bonus = proficiency_bonus
    return prof_bonus
