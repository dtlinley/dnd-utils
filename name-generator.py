import random
import json
import collections


Name = collections.namedtuple('Name', ['text', 'meaning'])
Affix = collections.namedtuple('Affix', ['text', 'meaning'])


# Choose an affix from the sequence of affixations
#
# Expects the affix sequence to be in the format:
# [ { 'options': ['affix1', 'affix2', ...], 'meaning': 'text describing affix' }, ... ]
#
# Returns an Affix
#
def choose_affix(affixations):
    affix_dict = random.choice(affixations)
    affix = random.choice(affix_dict['options']).encode('utf-8')
    meaning = affix_dict['meaning'].encode('utf-8')
    return Affix(affix, meaning)


# Randomly generate a name from the provided data
#
# Expects the name data to be in the following format:
# { 'race': 'name of race',
#   'sources': ['source of the data', 'other source', ...],
#   'proper_names': {
#     'prefixes': [ { 'options': ['affix1', 'affix2', ...], 'meaning': 'text describing affix' }, ... ]
#     'suffixes': [ { 'options': ['affix1', 'affix2', ...], 'meaning': 'text describing affix' }, ... ]
#   }
#   'surnames': {
#     'prefixes': [ { 'options': ['affix1', 'affix2', ...], 'meaning': 'text describing affix' }, ... ]
#     'suffixes': [ { 'options': ['affix1', 'affix2', ...], 'meaning': 'text describing affix' }, ... ]
#   }
# }
#
def create_name(name_json):
    prefix = choose_affix(name_json['proper_names']['prefixes'])
    suffix = choose_affix(name_json['proper_names']['suffixes'])
    name = prefix.text + suffix.text
    meaning = prefix.meaning + " " + suffix.meaning
    return Name(name, meaning)


name_file = open("dwarf_names.json")
dwarf_names = json.load(name_file)
for num in range(0, 10):
    print create_name(dwarf_names)
