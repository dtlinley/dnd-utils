import random

def pickByWeight(list, value):
    if (value <= list[0]['weight'] or len(list) is 1):
        return list[0]
    return pickByWeight(list[1:], value - list[0]['weight'])

def normalize(list):
    sum = 0.0
    copy = list[:]
    for item in copy:
        sum = sum + item['weight']
    for item in copy:
        pre_normal = item['weight']
        item['weight'] = pre_normal / sum
    return copy

def pickTrait(list):
    trait = pickByWeight(normalize(list), random.random())
    traits = [trait]
    for sub in trait['subtraits']:
        traits.extend(pickTrait(sub))
    return traits


def createCharacter():
    hair_colours = [
        {'attribute': 'blonde', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'brunette', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'red-haired', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'black-haired', 'weight': 0.5, 'subtraits': []},
    ]
    dwarf_subraces = [
        {'attribute': 'hill dwarf', 'weight': 1, 'subtraits': []},
        {'attribute': 'mountain dwarf', 'weight': 1, 'subtraits': []},
    ]
    elf_subraces = [
        {'attribute': 'wood elf', 'weight': 1, 'subtraits': []},
        {'attribute': 'high elf', 'weight': 1, 'subtraits': []},
    ]
    gnome_subraces = [
        {'attribute': 'forest gnome', 'weight': 1, 'subtraits': []},
        {'attribute': 'rock gnome', 'weight': 1, 'subtraits': []},
        {'attribute': 'deep gnome', 'weight': 0.01, 'subtraits': []},
    ]
    halfling_subraces = [
        {'attribute': 'stout halfling', 'weight': 1, 'subtraits': []},
        {'attribute': 'lightfoot halfling', 'weight': 1, 'subtraits': []},
    ]
    dragonborn_colours = [
        {'attribute': 'black', 'weight': 0.1, 'subtraits': []},
        {'attribute': 'blue', 'weight': 0.1, 'subtraits': []},
        {'attribute': 'brass', 'weight': 50, 'subtraits': []},
        {'attribute': 'bronze', 'weight': 50, 'subtraits': []},
        {'attribute': 'copper', 'weight': 50, 'subtraits': []},
        {'attribute': 'gold', 'weight': 50, 'subtraits': []},
        {'attribute': 'green', 'weight': 0.1, 'subtraits': []},
        {'attribute': 'red', 'weight': 0.1, 'subtraits': []},
        {'attribute': 'silver', 'weight': 50, 'subtraits': []},
        {'attribute': 'white', 'weight': 0.1, 'subtraits': []},
    ]
    physical_characteristics = [
        {'attribute': 'one-eyed', 'weight': 0.01, 'subtraits': []},
        {'attribute': 'old', 'weight': 0.2, 'subtraits': []},
        {'attribute': 'young', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'short', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'tall', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'grizzled', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'thin', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'fat', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'muscled', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'handsome', 'weight': 0.5, 'subtraits': []},
        {'attribute': 'ugly', 'weight': 0.5, 'subtraits': []},
    ]
    races = [
        {'attribute': 'human', 'weight': 10, 'subtraits': [hair_colours]},
        {'attribute': 'halfling', 'weight': 2, 'subtraits': [hair_colours, halfling_subraces]},
        {'attribute': 'elf', 'weight': 4, 'subtraits': [hair_colours, elf_subraces]},
        {'attribute': 'half-elf', 'weight': 6, 'subtraits': [hair_colours]},
        {'attribute': 'half-orc', 'weight': 3, 'subtraits': [hair_colours]},
        {'attribute': 'dragonborn', 'weight': 1, 'subtraits': [dragonborn_colours]},
        {'attribute': 'tiefling', 'weight': 1, 'subtraits': [hair_colours]},
        {'attribute': 'gnome', 'weight': 2.5, 'subtraits': [hair_colours, gnome_subraces]},
        {'attribute': 'dwarf', 'weight': 4, 'subtraits': [hair_colours, dwarf_subraces]},
    ]
    genders = [
        {'attribute': 'male', 'weight': 500, 'subtraits': [races, physical_characteristics]},
        {'attribute': 'female', 'weight': 500, 'subtraits': [races, physical_characteristics]},
        {'attribute': 'androgynous', 'weight': 1, 'subtraits': [races, physical_characteristics]},
    ]

    return map(lambda x: x['attribute'], pickTrait(genders))

print createCharacter()
