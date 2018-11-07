import common_traits
import dragonborn_names

colours = [
    {'attribute': 'black', 'weight': 0.1, 'subtraits': []},
    {'attribute': 'blue', 'weight': 0.1, 'subtraits': []},
    {'attribute': 'brass', 'weight': 50, 'subtraits': []},
    {'attribute': 'bronze', 'weight': 50, 'subtraits': []},
    {'attribute': 'copper', 'weight': 50, 'subtraits': []},
    {'attribute': 'gold', 'weight': 50, 'subtraits': []},
    {'attribute': 'green', 'weight': 0.1, 'subtraits': []},
    {'attribute': 'red', 'weight': 0.1, 'subtraits': []},
    {'attribute': 'silver', 'weight': 50, 'subtraits': []},
    {'attribute': 'white', 'weight': 0.1, 'subtraits': []},
]

traits = [
    colours,
    common_traits.physical_characteristics,
    {
        'androgynous': dragonborn_names.female_names + dragonborn_names.male_names,
        'female': dragonborn_names.female_names,
        'male': dragonborn_names.male_names,
    },
    dragonborn_names.clan_names
]
