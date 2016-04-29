import random
import json
import collections
import argparse


Name = collections.namedtuple('Name', ['text', 'gender', 'meaning'])
Affix = collections.namedtuple('Affix', ['text', 'gender', 'meaning'])


class NameCreationException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


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
def select_proper_affixations(name_data, affix_type, gender=None):
    affixations = name_data['proper_names'][affix_type]
    if gender is not None:
        affixations = [a for a in affixations if 'gender' not in a or a['gender'] == gender]
    if len(affixations) == 0:
        raise NameCreationException("No " + affix_type + " for gender "+ gender)
    return affixations


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
    prefixes = select_proper_affixations(name_data, "prefixes", gender)
    prefix = choose_affix(prefixes)
    # The suffix gender must be equal the most refined gender between `gender` and `prefix.gender`
    # in order to avoid mixed-gender names
    suffix_selection_gender = gender
    if prefix.gender is not None:
        suffix_selection_gender = prefix.gender
    suffixes = select_proper_affixations(name_data, "suffixes", suffix_selection_gender)
    suffix = choose_affix(suffixes)
    name = prefix.text + suffix.text
    meaning = prefix.meaning + " " + suffix.meaning
    if prefix.gender is not None:
        created_gender = prefix.gender
    else:
        created_gender = suffix.gender
    return Name(name, created_gender, meaning)


def pretty_print(rows):
    col_width = max(len(word) for row in rows for word in row) + 1 # padding
    for row in rows:
        print "".join(word.ljust(col_width) for word in row)


parser = argparse.ArgumentParser(description="Name Generator")
parser.add_argument("name_file", type=file, help="a file listing the possible components of a name")
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
