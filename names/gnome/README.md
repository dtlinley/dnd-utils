# Gnome Name Creation

The gnome name generation process is outlined in "Races of Stone" p.g. 49-50:

1. Choose 1-3 name fragments
  - If only one fragment, add a special ending
  - Fragments are often joined together by one of a list of vowels
  - Female names (of size > 1) are given gendered name-endings 
2. Choose 0-2 nicknames
  - There are two strategies in "Races of Stone"
    - If the gnome name has two fragments, add a nickname OR
    - Choose 0-2 nicknames

## Using the Script

The `gnome-name-generator.py` script must be supplied a JSON file matching the gnome file format. Optionally, the script can be told how many names it should create and the gender of the created names.

```
python gnome-name-generator.py -n 3 --gender female gnome_names.json 
Name               Meaning            Nickname           Gender             
Enneflana          Husband/Wife Earth Ale                female             
Callada            Cousin                                female             
Gaergaerae         Defence Defence    Sun Sun            female
```

## Gnome Name File Format

```
{
  "population": "the group of gnomes these names will work for. e.g. all gnome, forest gnomes, etc.",
  "sources": ["where these names were found"],
  "names":[
    { "fragment": "name fragment. Normally a syllable",     "meanings": ["list of possible meanings"]},
    ...
  ],
  "joiners": ["strings inserted in-between name fragments"],
  "small_name_endings": {
    "male": ["the possible strings appended to the end of a one-fragment male name"],
    "female": ["the possible strings appended to the end of a one-fragment female name"]
  },
  "big_name_endings": {
    "male": ["the possible strings appended to the end of a 2-or-more-fragment male name"],
    "female": ["the possible strings appended to the end of a 2-or-more fragment female name"]
  },
  "nicknames":["a list of possible nicknames"]
}
```
