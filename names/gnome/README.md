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
python gnome-name-generator.py -n 3 --gender male gnome_names.json 

TODO Sample Output
```

## Gnome Name File Format

TODO
