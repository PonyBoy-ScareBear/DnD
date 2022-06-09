def lvl_calc(xp: int) -> int:
    if xp < 300:
        level = 1
    elif xp < 900:
        level = 2
    elif xp < 2700:
        level = 3
    elif xp < 6500:
        level = 4
    elif xp < 14000:
        level = 5
    elif xp < 23000:
        level = 6
    elif xp < 34000:
        level = 7
    elif xp < 48000:
        level = 8
    elif xp < 64000:
        level = 9
    elif xp < 85000:
        level = 10
    elif xp < 100000:
        level = 11
    elif xp < 120000:
        level = 12
    elif xp < 140000:
        level = 13
    elif xp < 165000:
        level = 14
    elif xp < 195000:
        level = 15
    elif xp < 225000:
        level = 16
    elif xp < 265000:
        level = 17
    elif xp < 305000:
        level = 18
    elif xp < 355000:
        level = 19
    else:
        level = 20
    return level


def prof_calc(xp: int) -> int:
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
    return proficiency_bonus
