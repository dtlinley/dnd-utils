import elf_traits
import copy
import common_traits

skin = []
skin.extend(copy.deepcopy(elf_traits.wood_skin))
skin.extend(copy.deepcopy(elf_traits.high_skin))

traits = [
    skin,
    common_traits.physical_characteristics,
]
