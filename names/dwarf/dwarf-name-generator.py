import random
import json
import collections
import argparse


Name = collections.namedtuple('Name', ['text', 'gender', 'meaning'])
NamePart = collections.namedtuple('NamePart', ['text', 'gender', 'meaning'])
Affix = collections.namedtuple('Affix', ['text', 'gender', 'meaning'])


class NameCreationException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def combine_meaning(meaning, *other_meanings):
    combined = meaning
    for other in other_meanings:
        if other is not None:
            if combined is None:
                combined = other
            else:
                combined = combined + " " + other
    return combined


def select_optional_property(affix_dict, prop):
    p = None
    if prop in affix_dict:
        p = affix_dict[prop].encode('utf-8')
    return p


# Choose an affix from the sequence of affixations
#
# Expects the affix sequence to be in the format:
# [
#   {
#     'options': ['affix spelling', 'affix alternative spelling', ...],
#     'meaning': 'optional text describing affix',
#     'gender': 'optional gender'
#   },
#   ...
# ]
#
# Returns an Affix
#
def choose_affix(affixations):
    affix_dict = random.choice(affixations)
    affix = random.choice(affix_dict['options']).encode('utf-8')
    meaning = select_optional_property(affix_dict, 'meaning')
    gender = select_optional_property(affix_dict, 'gender')
    return Affix(affix, gender, meaning)


# Select all affixations that either match the given gender or are unisex
def select_affixations(name_data, affix_type, gender=None):
    affixations = name_data[affix_type]
    if gender is not None:
        affixations = [a for a in affixations if 'gender' not in a or a['gender'] == gender]
    if len(affixations) == 0:
        raise NameCreationException("No " + affix_type + " for gender "+ gender)
    return affixations


# Random generate part of a name
#
# Expects the data to be in the following format:
#
# {
#   'prefixes': [ { 'options': ['affix1', ...], 'meaning': 'text describing affix', 'gender': 'optional gender' }, ... ]
#   'suffixes': [ { 'options': ['affix1', ...], 'meaning': 'text describing affix', 'gender': 'optional gender' }, ... ]
# }
def create_name_part(name_part_data, gender=None):
    prefixes = select_affixations(name_part_data, "prefixes", gender)
    prefix = choose_affix(prefixes)
    # The suffix gender must be equal the most refined gender between `gender` and `prefix.gender`
    # in order to avoid mixed-gender names
    suffix_selection_gender = gender
    if prefix.gender is not None:
        suffix_selection_gender = prefix.gender
    suffixes = select_affixations(name_part_data, "suffixes", suffix_selection_gender)
    suffix = choose_affix(suffixes)
    name = prefix.text + suffix.text
    meaning = combine_meaning(prefix.meaning, suffix.meaning)
    if prefix.gender is not None:
        created_gender = prefix.gender
    else:
        created_gender = suffix.gender
    return NamePart(name, created_gender, meaning)


# Randomly generate a name from the provided data
#
# Expects the name data to be in the following format:
# { 'race': 'name of race',
#   'sources': ['source of the data', 'other source', ...],
#   'proper_names': {
#     'prefixes': [ { 'options': ['affix1', ...], 'meaning': 'text describing affix', 'gender': 'optional gender' }, ... ]
#     'suffixes': [ { 'options': ['affix1', ...], 'meaning': 'text describing affix', 'gender': 'optional gender' }, ... ]
#   }
#   'surnames': {
#     'prefixes': [ { 'options': ['affix1', ...], 'meaning': 'text describing affix', 'gender': 'optional gender' }, ... ]
#     'suffixes': [ { 'options': ['affix1', ...], 'meaning': 'text describing affix', 'gender': 'optional gender' }, ... ]
#   }
# }
#
def create_name(name_data, gender=None):
    first_name = create_name_part(name_data['proper_names'], gender)
    last_name_selection_gender = gender
    if first_name.gender is not None:
        last_name_selection_gender = first_name.gender
    last_name = create_name_part(name_data['surnames'], last_name_selection_gender)
    if first_name.gender is not None:
        created_gender = first_name.gender
    elif last_name.gender is not None:
        created_gender = last_name.gender
    else:
        created_gender = "Unisex"
    meaning = combine_meaning(first_name.meaning, last_name.meaning)
    return Name(first_name.text + " " + last_name.text, created_gender, meaning)


def pretty_print(rows):
    col_width = max(len(word) for row in rows for word in row) + 1 # padding
    for row in rows:
        print "".join(word.ljust(col_width) for word in row)


parser = argparse.ArgumentParser(description="Dwarf Name Generator")
parser.add_argument("name_file", type=file, help="a file listing the possible components of dwarven names")
parser.add_argument("-n", dest="num_names", type=int, help="the number of names to create", default=10)
gender_help = "limit the name creation to unisex names and gendered names equal to GENDER"
parser.add_argument("-g", "--gender", dest="gender", help=gender_help, default=None)
args = parser.parse_args()

try:
    name_data = json.load(args.name_file)
    names = [create_name(name_data, args.gender) for num in range(0, args.num_names)]
    header = [["Name", "Gender", "Meaning"]]
    pretty_print(header + names)
except NameCreationException as e:
    print "Could not create names due to error. " + e.value
