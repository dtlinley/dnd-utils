import common_traits
import copy
import tiefling_names

skin_colours = copy.deepcopy(common_traits.skin_colours)
skin_colours.extend([
    {'attribute': 'pink skin', 'weight': 1, 'subtraits': []},
    {'attribute': 'crimson skin', 'weight': 1, 'subtraits': []},
    {'attribute': 'deep red skin', 'weight': 1, 'subtraits': []},
    {'attribute': 'light red skin', 'weight': 1, 'subtraits': []},
    {'attribute': 'blue-black skin', 'weight': 0.1, 'subtraits': []},
])

hair_colours = [
    {'attribute': 'black hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'dark-brown hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'brown hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'dark red hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'purple hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'blue hair', 'weight': 1, 'subtraits': []},
]

horns = [
    {'attribute': 'ram horns', 'weight': 1, 'subtraits': []},
    {'attribute': 'straight horns', 'weight': 1, 'subtraits': []},
    {'attribute': 'small horns', 'weight': 1, 'subtraits': []},
    {'attribute': 'spiral horns', 'weight': 1, 'subtraits': []},
]

for skin in skin_colours:
    skin['subtraits'] = [hair_colours, horns]

traits = [
    skin_colours,
    common_traits.physical_characteristics,
    {
        'androgynous': tiefling_names.female_names + tiefling_names.male_names,
        'female': tiefling_names.female_names,
        'male': tiefling_names.male_names,
    },
    tiefling_names.virtue_names
]
