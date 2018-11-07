import common_traits
import arabic_names
import celtic_names

female_names = arabic_names.female_names + celtic_names.female_names
male_names = arabic_names.male_names + celtic_names.male_names

traits = [
    common_traits.physical_characteristics,
    common_traits.skin_colours,
    {
        'androgynous': female_names + male_names,
        'female': female_names,
        'male': male_names,
    }
]
