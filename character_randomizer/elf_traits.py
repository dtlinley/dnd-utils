import common_traits
import copy

hair_colours = copy.deepcopy(common_traits.white_hair_colours)
hair_colours.extend([
    {'attribute': 'green hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'blue hair', 'weight': 1, 'subtraits': []},
])

faerun_hair = [
    {'attribute': 'copper hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'black hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'golden blonde hair', 'weight': 1, 'subtraits': []},
]
moon_hair = [
    {'attribute': 'silver-white hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'black hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'blue hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'blonde hair', 'weight': 0.5, 'subtraits': []},
    {'attribute': 'brown hair', 'weight': 0.5, 'subtraits': []},
    {'attribute': 'red hair', 'weight': 0.5, 'subtraits': []},
]
wood_hair = [
    {'attribute': 'brown hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'black hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'copper hair', 'weight': 0.5, 'subtraits': []},
    {'attribute': 'blonde hair', 'weight': 0.5, 'subtraits': []},
]

skin_colours = copy.deepcopy(common_traits.skin_colours)
for skin in skin_colours:
    skin['subtraits'] = [hair_colours]

high_skin = copy.deepcopy(skin_colours)
high_skin.extend([
    {'attribute': 'bronze skin', 'weight': 1, 'subtraits': [faerun_hair]},
    {'attribute': 'alabaster skin', 'weight': 0.7, 'subtraits': [moon_hair]},
    {'attribute': 'whitish-blue skin', 'weight': 0.3, 'subtraits': [moon_hair]},
])
wood_skin = copy.deepcopy(skin_colours)
wood_skin.extend([
    {'attribute': 'copper skin', 'weight': 1.7, 'subtraits': [wood_hair]},
    {'attribute': 'coppery-green skin', 'weight': 0.3, 'subtraits': [wood_hair]},
])

subraces = [
    {'attribute': 'wood elf', 'weight': 1, 'subtraits': [wood_skin]},
    {'attribute': 'high elf', 'weight': 1, 'subtraits': [high_skin]},
]

traits = [
    subraces,
    common_traits.physical_characteristics,
]
