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
        meaning = choose(meanings)
        chosen_meanings.append(meaning)
    chosen_fragments = list(intersperse(chosen_fragments, lambda: choose(joiners)))
    chosen_fragments.append(choose(endings))
    name = "".join(chosen_fragments).capitalize().encode('utf-8')
    meaning = " ".join(chosen_meanings).encode('utf-8')
    return (name, meaning)


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
    nickname = " ".join([choose(nicknames) for _ in range(num_nicknames)]).encode('utf-8')
    name = creation[0]
    meanings = creation[1]
    return (name, meanings, nickname)


def pretty_print(rows):
    col_width = max(len(word) for row in rows for word in row) + 1 # padding
    for row in rows:
        print "".join(word.ljust(col_width) for word in row)


parser = argparse.ArgumentParser(description="Gnome Name Generator")
parser.add_argument("name_file", type=file, help="a file listing the components of Gnome names")
parser.add_argument("-n", dest="num_names", type=int, help="the number of names to create", default=10)
parser.add_argument("-g", "--gender", dest="gender", help="the gender of the produced names", default=None)
args = parser.parse_args()

name_data = json.load(args.name_file)
fragments = name_data['names']
nicknames = name_data['nicknames']
joiners = name_data['joiners']
male_big_endings = name_data['big_name_endings']['male']
male_little_endings = name_data['small_name_endings']['male']
female_big_endings = name_data['big_name_endings']['female']
female_little_endings = name_data['small_name_endings']['female']
if args.gender == "male":
    genders = ["male" for _ in range(args.num_names)]
elif args.gender == "female":
    genders = ["female" for _ in range(args.num_names)]
else:
    genders = [choose(["male", "female"]) for _ in range(args.num_names)]
names = []
for gender in genders:
    if gender == "male":
        little_endings = male_little_endings
        big_endings = male_big_endings
    else:
        little_endings = female_little_endings
        big_endings = female_big_endings
    creation = create_full_gnome_name(fragments, nicknames, joiners, big_endings, little_endings)
    names.append(GnomeName(creation[0], creation[1], creation[2], gender))

header = [["Name", "Meaning", "Nickname", "Gender"]]
pretty_print(header + names)
