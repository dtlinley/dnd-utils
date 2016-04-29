# Utilities for Dungeons And Dragons

## Character Randomizer

Creates a random character with gender, race, hair colour and a physical attribute (e.g. old, young, tall, short.)

`python character_randomizer.py`

## Name Generation

Being able to quickly create names is an important skill every DM should master. That, or you can make a computer do it for you.

`python name-generator.py [NAME_DATA.json]`

Where NAME_DATA.json is a JSON file providing name information (prefixes, suffixes, etc) for a particular population (e.g. dwarves). The file must follow the format specified in `names`.

#### Sample Usage
The name generator creates a gender and rough meaning for each name.
```
python name-generator.py --gender female -n 2 names/dwarf_names.json
Name                          Gender                        Meaning                       
Jarydd                        female                        Orc/Ugly Queen                
Therola                       female                        Oath/of Oaths Brewer/Brew/Ale
```
