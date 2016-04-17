import random

def pickByWeight(list, value):
    if (value <= list[0]['weight'] or len(list) is 1):
        return list[0]['attribute']
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
    return pickByWeight(normalize(list), random.random())

def createCharacter():
    genders = [{'attribute': 'male', 'weight': 0.5}, {'attribute': 'female', 'weight': 0.5}]
    hair_colours = [
        {'attribute': 'blonde', 'weight': 0.5},
        {'attribute': 'brunette', 'weight': 0.5},
        {'attribute': 'red-haired', 'weight': 0.5},
        {'attribute': 'black-haired', 'weight': 0.5}
    ]
    physical_characteristics = [
        {'attribute': 'old', 'weight': 0.5},
        {'attribute': 'young', 'weight': 0.5},
        {'attribute': 'short', 'weight': 0.5},
        {'attribute': 'tall', 'weight': 0.5},
        {'attribute': 'grizzled', 'weight': 0.5},
        {'attribute': 'thin', 'weight': 0.5},
        {'attribute': 'fat', 'weight': 0.5},
        {'attribute': 'muscled', 'weight': 0.5},
    ]
    races = [
        {'attribute': 'human', 'weight': 10},
        {'attribute': 'halfling', 'weight': 2},
        {'attribute': 'elf', 'weight': 4},
        {'attribute': 'half-elf', 'weight': 6},
        {'attribute': 'half-orc', 'weight': 3},
        {'attribute': 'dragonborn', 'weight': 1},
        {'attribute': 'tiefling', 'weight': 1},
        {'attribute': 'gnome', 'weight': 2.5},
        {'attribute': 'dwarf', 'weight': 4},
    ]

    gender = pickTrait(genders)
    hair = pickTrait(hair_colours)
    physical = pickTrait(physical_characteristics)
    race = pickTrait(races)
    return 'A ' + gender + ', ' + hair + ' ' + physical + ' ' + race

print createCharacter()
