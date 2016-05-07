import random
import argparse
import json
import collections


GnomeName = collections.namedtuple("GnomeName", ["name", "meanings", "nickname", "gender"])


def choose(list):
    return random.choice(list)


# Add delimiters produced by get_delimiter between the
# elements of iterable. There will be a single delimiter
# between each of the elements of iterable
def intersperse(iterable, get_delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield get_delimiter()
        yield x


def create_gnome_name(fragments, size, joiners, endings):
    chosen_fragments = []
    chosen_meanings = []
    for _ in range(size):
        choice = choose(fragments)
        fragment = choice['fragment']
        chosen_fragments.append(fragment)
        meanings = choice['meanings']
        chosen_meanings = chosen_meanings + meanings
    chosen_fragments = list(intersperse(chosen_fragments, lambda: choose(joiners)))
    chosen_fragments.append(choose(endings))
    return ("".join(chosen_fragments), chosen_meanings)


def create_full_gnome_name(fragments, nicknames, joiners, big_endings, little_endings):
    num_frags = random.randint(1, 3)
    if num_frags == 1:
        # Single fragment names have their own endings
        creation = create_gnome_name(fragments, 1, joiners, little_endings)
    else:
        creation = create_gnome_name(fragments, num_frags, joiners, big_endings)
    # Deviated from the original gnome-name spec.
    # Before: Only gnomes with two-fragment names got a nickname
    # Now: Every gnome has the chance of getting a nickname
    num_nicknames = random.randint(0, 2)
    nickname = " ".join([choose(nicknames) for _ in range(num_nicknames)])
    name = creation[0]
    meanings = creation[1]
    return (name.capitalize().encode('utf-8'), meanings, nickname.encode('utf-8'))


def pretty_print(rows):
    col_width = max(len(word) for row in rows for word in row) + 1 # padding
    for row in rows:
        print "".join(word.ljust(col_width) for word in row)


parser = argparse.ArgumentParser(description="Gnome Name Generator")
parser.add_argument("name_file", type=file, help="a file listing the components of Gnome names")
parser.add_argument("-n", dest="num_names", type=int, help="the number of names to create", default=10)
parser.add_argument("-g", "--gender", dest="gender", help="the gender of the produced names", default="male")
args = parser.parse_args()

name_data = json.load(args.name_file)
fragments = name_data['names']
nicknames = name_data['nicknames']
joiners = name_data['joiners']
male_big_endings = name_data['big_name_endings']['male']
male_little_endings = name_data['small_name_endings']['male']
for _ in range(5):
    print create_full_gnome_name(fragments, nicknames, joiners, male_big_endings, male_little_endings)
#names = [create_gnome_name(fragments, nicknames) for num in range(0, args.num_names)]
#header = [["Name", "Meaning", "Nickname", "Gender"]]
#pretty_print(header + names)
