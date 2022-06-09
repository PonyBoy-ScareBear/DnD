import pandas as pd
import dice_roller
from dnd.dice_roller import single_roll


# Early Travel Day
dessarin_valley_early_day = pd.DataFrame()
dessarin_valley_early_day['roll'] = list(range(19))
dessarin_valley_early_day['roll'] = dessarin_valley_early_day['roll']+2
dessarin_valley_early_day['encounter'] = [
    'Aarakocra scouts', 'Knights of Samular', 'Pilgrims', 'Elk Tribe Hunters',
    '1d3 ankhegs', '1d3 + 1 bugbears', '1d4 + 1 orcs', 'Dwarf miners', 'Caravan',
    'Homestead', 'Air cult scouts', 'Water cult marauders', 'Earth cult robbers', 'Fire cult raiders',
    '1d4 + 1 gnolls', 'Shepherds', '1d6 + 2 wolves', '1d3 ogres', '1d2 perytons']
# Early Travel Night
dessarin_valley_early_night = pd.DataFrame()
dessarin_valley_early_night['roll'] = list(range(19))
dessarin_valley_early_night['roll'] = dessarin_valley_early_night['roll']+2
dessarin_valley_early_night['encounter'] = [
    '1d4 + 1 jackalweres', 'Pilgrims', '1d2 owlbears', 'Elk Tribe Hunters',
    '1d3 ankhegs', '1d3 + 1 bugbears', '1d4 + 1 orcs', 'Air cult scouts', 'Water cult marauders',
    'Earth cult robbers', 'Fire cult raiders', '1d4 + 1 gnolls', '1d6 + 2 wolves', '1d3 ogres',
    '1d2 gargoyles', '1d3 + 1 ghouls', '1d2 perytons', '1d3 wights', 'The Watchful Knight']
# Later Travel Day
dessarin_valley_late_day = pd.DataFrame()
dessarin_valley_late_day['roll'] = list(range(19))
dessarin_valley_late_day['roll'] = dessarin_valley_late_day['roll']+2
dessarin_valley_late_day['encounter'] = [
    'Aarakocra war band', '1d3 manticores', '1d3 + 1 trolls', 'Elk Tribe Hunters',
    'Knights of Samular', 'Homestead', '1d4 + 1 gargoyles', 'Air cult skyriders', 'Water cult raiders',
    '1d6 + 2 bugbears', 'Fire cult war band', 'Earth cult marauders', '2d4 ogres', 'Caravan',
    '2d4 mephits', 'Dwarf miners', '1d3 elementals', '1 bulette', '1d2 hill giants']
# Later Travel Night
dessarin_valley_late_night = pd.DataFrame()
dessarin_valley_late_night['roll'] = list(range(19))
dessarin_valley_late_night['roll'] = dessarin_valley_late_night['roll']+2
dessarin_valley_late_night['encounter'] = [
    '2d6 jackalweres', '1d3 manticores', '1d3 + 1 trolls', 'Elk Tribe Hunters',
    '1d8 will-o-wisps', '1d2 ghasts and 1d4 + 2 ghouls', '1d4 + 1 gargoyles', 'Air cult skyriders', 'Water cult raiders',
    '1d6 + 2 bugbears', 'Fire cult war band', 'Earth cult marauders', '2d4 ogres', '1d4 + 1 wights',
    '2d4 mephits', '1d3 vampire spawn', '1d3 elementals', '1 bulette', '1d2 hill giants']
# River Travel
dessarin_valley_river = pd.DataFrame()
dessarin_valley_river['roll'] = list(range(19))
dessarin_valley_river['roll'] = dessarin_valley_river['roll']+2
dessarin_valley_river['encounter'] = [
    'Aarakocra scouts', 'Aarakocra scouts', 'Air cult skyriders', 'Air cult skyriders',
    'River pirates', 'River pirates', 'River pirates', 'River pirates', 'Keelboat',
    'Keelboat', 'Keelboat', 'Keelboat', 'Keelboat', '1d4 merrow',
    '1d4 merrow', '2d4 ghouls', '2d4 ghouls', '1 water elemental', '1 water elemental']


def dessarin_valley_encounter(encounter_type: str) -> pd.DataFrame():
    """Generates random encounter in Dessarin Valley

    Args:
        encounter_type (str): 'early day', 'early night', 'late day', 'late night', or 'river'

    Returns:
        dv_encounter (pd.DataFrame()): Pandas DataFrame with columns 'roll' and 'encounter' with a single row populated.
    """
    encounter_occurrence = dice_roller.single_roll(20)
    if encounter_occurrence < 18:
        dv_encounter = pd.DataFrame()
        dv_encounter['roll'] = 9999
        dv_encounter['encounter'] = 'NO ENCOUNTER OCCURRED'
    else:
        d12 = dice_roller.single_roll(12)
        d8 = dice_roller.single_roll(8)
        encounter_roll = d12 + d8
        if encounter_type == 'early day':
            dv_encounter = dessarin_valley_early_day[dessarin_valley_early_day['roll'] == encounter_roll]
        elif encounter_type == 'early night':
            dv_encounter = dessarin_valley_early_night[dessarin_valley_early_night['roll'] == encounter_roll]
        elif encounter_type == 'late day':
            dv_encounter = dessarin_valley_late_day[dessarin_valley_late_day['roll'] == encounter_roll]
        elif encounter_type == 'late night':
            dv_encounter = dessarin_valley_late_night[dessarin_valley_late_night['roll'] == encounter_roll]
        else:
            dv_encounter = dessarin_valley_river[dessarin_valley_river['roll'] == encounter_roll]
    return dv_encounter
