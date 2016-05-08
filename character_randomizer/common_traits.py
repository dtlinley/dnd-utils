import copy

hair_colours = [
    {'attribute': 'brown hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'black hair', 'weight': 1, 'subtraits': []},
    {'attribute': 'light-brown hair', 'weight': 1, 'subtraits': []},
]

white_hair_colours = copy.deepcopy(hair_colours)
white_hair_colours.extend([
    {'attribute': 'blonde', 'weight': 1, 'subtraits': []},
    {'attribute': 'red hair', 'weight': 0.6, 'subtraits': []},
])

physical_characteristics = [
    {'attribute': 'one-eyed', 'weight': 0.05, 'subtraits': []},
    {'attribute': 'old', 'weight': 0.4, 'subtraits': []},
    {'attribute': 'young', 'weight': 1, 'subtraits': []},
    {'attribute': 'short', 'weight': 1, 'subtraits': []},
    {'attribute': 'tall', 'weight': 1, 'subtraits': []},
    {'attribute': 'grizzled', 'weight': 1, 'subtraits': []},
    {'attribute': 'thin', 'weight': 1, 'subtraits': []},
    {'attribute': 'fat', 'weight': 1, 'subtraits': []},
    {'attribute': 'muscled', 'weight': 1, 'subtraits': []},
    {'attribute': 'handsome', 'weight': 0.5, 'subtraits': []},
    {'attribute': 'ugly', 'weight': 0.5, 'subtraits': []},
]

skin_colours = [
    {'attribute': 'black skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'dark brown skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'brown skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'light brown skin', 'weight': 1, 'subtraits': [hair_colours]},
    {'attribute': 'tanned skin', 'weight': 1, 'subtraits': [white_hair_colours]},
    {'attribute': 'white skin', 'weight': 1, 'subtraits': [white_hair_colours]},
]

# Return the full dictionary from the given list where the attribute value matches the given name
# Assumes that only one such dictionary exists
#
# @param name {String} The attribute value that is being searched for
# @param list {List of dictionaries} The list to search for a dictionary with a matching attribute value
def find_trait(name, list):
    matching = filter(lambda x: x['attribute'] == name, list)
    return matching[0]
