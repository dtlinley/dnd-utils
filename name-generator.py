import random
import json
import collections
import argparse


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
def create_name(name_data):
    prefix = choose_affix(name_data['proper_names']['prefixes'])
    suffix = choose_affix(name_data['proper_names']['suffixes'])
    name = prefix.text + suffix.text
    meaning = prefix.meaning + " " + suffix.meaning
    return Name(name, meaning)


def pretty_print(rows):
    col_width = max(len(word) for row in rows for word in row) + 1 # padding
    for row in rows:
        print "".join(word.ljust(col_width) for word in row)


parser = argparse.ArgumentParser(description="Name Generator")
parser.add_argument("name_file", type=file, help="a file listing the possible components of a name")
parser.add_argument("-n", dest="num_names", type=int, help="the number of names to create", default=10)
args = parser.parse_args()

name_data = json.load(args.name_file)
names = [create_name(name_data) for num in range(0, args.num_names)]
header = [["Name", "Meaning"]]
pretty_print(header + names)
