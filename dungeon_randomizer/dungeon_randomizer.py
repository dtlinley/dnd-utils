import random
import copy

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
    traits = [trait['attribute']]
    for sub in trait['subtraits']:
        traits.extend([pickTrait(sub)])
    return traits
