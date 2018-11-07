import common_traits
import copy
import dwarf_names

hair_colours = copy.deepcopy(common_traits.hair_colours)
hair_colours.append({'attribute': 'red-haired', 'weight': 0.5, 'subtraits': []})

hill_skin_colours = [
    {'attribute': 'deep brown skin', 'weight': 0.1, 'subtraits': [hair_colours]},
    {'attribute': 'reddish pale skin', 'weight': 0.1, 'subtraits': [hair_colours]},
    {'attribute': 'light brown skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'deep tan skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'tan skin', 'weight': 1, 'subtraits': [hair_colours]},
]

# Mountain Dwarfs tend to have lighter skin and be taller
mountain_skin_colours = [
    {'attribute': 'deep brown skin', 'weight': 0.01, 'subtraits': [hair_colours]},
    {'attribute': 'reddish pale skin', 'weight': 0.3, 'subtraits': [hair_colours]},
    {'attribute': 'light brown skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'deep tan skin', 'weight': 0.1, 'subtraits': [hair_colours]},
    {'attribute': 'tan skin', 'weight': 0.5, 'subtraits': [hair_colours]},
]

mountain_characteristics = copy.deepcopy(common_traits.physical_characteristics)
tallness = common_traits.find_trait('tall', mountain_characteristics)
shortness = common_traits.find_trait('short', mountain_characteristics)
tallness['weight'] = 2
shortness['weight'] = 0.5

subraces = [
    {'attribute': 'hill dwarf', 'weight': 1, 'subtraits': [hill_skin_colours, common_traits.physical_characteristics]},
    {'attribute': 'mountain dwarf', 'weight': 1000, 'subtraits': [mountain_skin_colours, mountain_characteristics]},
]

traits = [
    subraces,
    {
        'androgynous': dwarf_names.female_names + dwarf_names.male_names,
        'female': dwarf_names.female_names,
        'male': dwarf_names.male_names,
    },
    dwarf_names.clan_names
]
