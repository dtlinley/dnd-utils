import common_traits
import gnome_names

subraces = [
    {'attribute': 'forest gnome', 'weight': 1, 'subtraits': []},
    {'attribute': 'rock gnome', 'weight': 2, 'subtraits': []},
    {'attribute': 'deep gnome', 'weight': 0.01, 'subtraits': []},
]

traits = [
    subraces,
    common_traits.physical_characteristics,
    common_traits.skin_colours,
    {
        'androgynous': gnome_names.female_names + gnome_names.male_names,
        'female': gnome_names.female_names,
        'male': gnome_names.male_names,
    },
    gnome_names.family_names
]
