import common_traits
import orc_names

skin_colours = [
    {'attribute': 'grey skin', 'weight': 1, 'subtraits': [common_traits.white_hair_colours]},
    {'attribute': 'pink-grey skin', 'weight': 1, 'subtraits': [common_traits.white_hair_colours]},
    {'attribute': 'green-grey skin', 'weight': 1, 'subtraits': [common_traits.white_hair_colours]},
    {'attribute': 'greenish skin', 'weight': 1, 'subtraits': [common_traits.white_hair_colours]},
]

traits = [
    skin_colours,
    common_traits.physical_characteristics,
    {
        'androgynous': orc_names.female_names + orc_names.male_names,
        'female': orc_names.female_names,
        'male': orc_names.male_names,
    }
]
