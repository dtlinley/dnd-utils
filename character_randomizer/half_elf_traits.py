import elf_traits
import copy
import common_traits
import elf_names

skin = []
skin.extend(copy.deepcopy(elf_traits.wood_skin))
skin.extend(copy.deepcopy(elf_traits.high_skin))

traits = [
    skin,
    common_traits.physical_characteristics,
    {
        'androgynous': elf_names.female_names + elf_names.male_names,
        'female': elf_names.female_names,
        'male': elf_names.male_names,
    },
    elf_names.family_names
]
