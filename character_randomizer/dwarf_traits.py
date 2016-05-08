import common_traits
import copy

hair_colours = copy.deepcopy(common_traits.hair_colours)
hair_colours.append({'attribute': 'red-haired', 'weight': 0.5, 'subtraits': []})

skin_colours = [
    {'attribute': 'deep brown skin', 'weight': 0.1, 'subtraits': [hair_colours]},
    {'attribute': 'reddish pale skin', 'weight': 0.1, 'subtraits': [hair_colours]},
    {'attribute': 'light brown skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'deep tan skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'tan skin', 'weight': 1, 'subtraits': [hair_colours]},
]

subraces = [
    {'attribute': 'hill dwarf', 'weight': 1, 'subtraits': []},
    {'attribute': 'mountain dwarf', 'weight': 1, 'subtraits': []},
]

traits = [
    subraces,
    common_traits.physical_characteristics,
    skin_colours,
]
