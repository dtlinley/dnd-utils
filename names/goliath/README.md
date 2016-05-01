# Goliath Names Creation

The goliath name generation process is outlined in "Races of Stone" p.g. 72-74. It breaks down into the follow:
1. First names are built of 2-4 syllables
  - A syllable ending in a consonant must be followed by a joiner. This is to make it sound less harsh
2. Last names are built of 4-7+ syllables
  - A syllable ending in a consonant must be followed by a joiner.
  - Cannot end with a consonant. Keep adding syllable until ending in a vowel
3. Honourifics are built from two words
  - A table is selected (each table with a unique feel), then one option is chosen per "roll"

## Using the Script

The `goliath-name-generator.py` script must be supplied a JSON file match the goliath file format. Optionally, the script can be told how many names it should create.

```
python goliath-name-generator.py -n 3 goliath_names.json 

First Name                    Honourific                    Last Name                     
mavuaeanae                    "Boar Friend"                 leaganevuaamomevu             
lekath                        "Trail Seeker"                kauaemakoovoloa               
olothai                       "Hidden Healer"               vathoaganiolathothovalethuvea
```

## Goliath Name File Format


```
{
  "population": "goliath",
  "sources": ["optional sources"],
  "syllables":[
    "syllable",
    ...
  ],
  "joiners":[
    "vowel-heavy syllable",
    ...
  ],
  "honours": [
    {
      "name": "optional name. Honourifics are created by joining one word per 'roll' table",
      "roll_1": [
        "word",
        ...
      ],
      "roll_2": [
        "word",
        ...
      ]
    },
    ...
  ]
}
```
