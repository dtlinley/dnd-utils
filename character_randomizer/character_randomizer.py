import random
import copy

import dragonborn_traits
import dwarf_traits
import elf_traits
import gnome_traits
import halfling_traits
import human_traits
import half_elf_traits
import half_orc_traits
import tiefling_traits

def pickByWeight(list, value):
    if (value <= list[0]['weight'] or len(list) is 1):
        return list[0]
    return pickByWeight(list[1:], value - list[0]['weight'])

def normalize(list):
    sum = 0.0
    listcopy = copy.deepcopy(list)
    for item in listcopy:
        sum = sum + item['weight']
    for item in listcopy:
        pre_normal = item['weight']
        item['weight'] = pre_normal / sum
    return listcopy

def pickTrait(list):
    trait = pickByWeight(normalize(list), random.random())
    traits = [trait]
    for sub in trait['subtraits']:
        traits.extend(pickTrait(sub))
    return traits


def createCharacter():
    races = [
        {'attribute': 'dragonborn', 'weight': 1, 'subtraits': dragonborn_traits.traits},
        {'attribute': 'dwarf', 'weight': 4, 'subtraits': dwarf_traits.traits},
        {'attribute': 'elf', 'weight': 4, 'subtraits': elf_traits.traits},
        {'attribute': 'gnome', 'weight': 2.5, 'subtraits': gnome_traits.traits},
        {'attribute': 'half-elf', 'weight': 6, 'subtraits': half_elf_traits.traits},
        {'attribute': 'half-orc', 'weight': 3, 'subtraits': half_orc_traits.traits},
        {'attribute': 'halfling', 'weight': 2, 'subtraits': halfling_traits.traits},
        {'attribute': 'human', 'weight': 10, 'subtraits': human_traits.traits},
        {'attribute': 'tiefling', 'weight': 1, 'subtraits': tiefling_traits.traits},
    ]
    genders = [
        {'attribute': 'male', 'weight': 500, 'subtraits': [races]},
        {'attribute': 'female', 'weight': 500, 'subtraits': [races]},
        {'attribute': 'androgynous', 'weight': 1, 'subtraits': [races]},
    ]

    return map(lambda x: x['attribute'], pickTrait(genders))

print createCharacter()
