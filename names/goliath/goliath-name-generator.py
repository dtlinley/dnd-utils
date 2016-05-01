import random
import argparse
import json
import collections


GoliathName = collections.namedtuple("GoliathName", ["first", "honourific", "last"])


def is_vowel(char):
    return char in "aeiou"


def is_consonant(char):
    return not is_vowel(char)


def create_goliath_honourific(honours):
    table = random.choice(honours)
    first = random.choice(table['roll_1'])
    second = random.choice(table['roll_2'])
    return "\"" + first + " " + second + "\""


def create_goliath_name(syllables, joiners, num_parts):
    name = random.choice(syllables)
    for part_num in range(0, num_parts - 1):
        last_char = name[-1]
        if is_consonant(last_char):
            next_syll = random.choice(joiners)
        else:
            next_syll = random.choice(syllables)
        name += next_syll
    return name


def create_full_goliath_name(syllables, joiners, honours):
    num_first_parts = random.randint(2, 4)
    first_name = create_goliath_name(syllables, joiners, num_first_parts)
    num_last_parts = random.randint(4, 7)
    last_name = create_goliath_name(syllables, joiners, num_last_parts)
    # This is unbounded, but written as stated in "Races of Stone"
    while is_consonant(last_name[-1]):
        next_syll = random.choice(joiners)
        last_name += next_syll
    honourific = create_goliath_honourific(honours)
    return GoliathName(first_name, honourific, last_name)


def pretty_print(rows):
    col_width = max(len(word) for row in rows for word in row) + 1 # padding
    for row in rows:
        print "".join(word.ljust(col_width) for word in row)


parser = argparse.ArgumentParser(description="Goliath Name Generator")
parser.add_argument("name_file", type=file, help="a file listing the components of Goliath names")
parser.add_argument("-n", dest="num_names", type=int, help="the number of names to create", default=10)
args = parser.parse_args()

name_data = json.load(args.name_file)
syllables = name_data['syllables']
joiners = name_data['joiners']
honours = name_data['honours']
names = [create_full_goliath_name(syllables, joiners, honours) for num in range(0, args.num_names)]
header = [["First Name", "Honourific", "Last Name"]]
pretty_print(header + names)