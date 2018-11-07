import common_traits
import halfling_names

hair_colours = [
    {'attribute': 'brown hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'sandy-brown hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'dirty-blonde hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'dark brown hair', 'weight': 1, 'subtraits': []},
]

skin_colours = [
    {'attribute': 'tan', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'light tan', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'ruddy skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'reddish-pale skin', 'weight': 1, 'subtraits': [hair_colours]},
]

subraces = [
    {'attribute': 'stout halfling', 'weight': 1, 'subtraits': []},
    {'attribute': 'lightfoot halfling', 'weight': 1, 'subtraits': []},
]

traits = [
    subraces,
    common_traits.physical_characteristics,
    skin_colours,
    {
        'androgynous': halfling_names.female_names + halfling_names.male_names,
        'female': halfling_names.female_names,
        'male': halfling_names.male_names,
    },
    halfling_names.family_names
]
