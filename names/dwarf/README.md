# Dwarf Name Creation

Dwarf names are made by simply appending prefixes to suffixes

## Using the Script

The dwarf name generator creates a gender and rough meaning for each name.

```
python dwarf-name-generator.py --gender female -n 3 dwarf_names.json
Name                    Gender                  Meaning                 
Kilja Coppercutter      female                  Proud/Powerful Mistress 
Oriip Oakbreaker        female                  Gem Pledge/Promise      
Mordred Goblinsmasher   female                  Brave/Bold Maiden
```

## Dwarf Name File Format

```
{
  "race": "race name",
  "sources": ["source of following data", "book name", "website", "etc."],
  "proper_names": {
    "prefixes":[
        { "gender": "optional gender. If missing, considered unisex",
          "options": ["variations", "of one affix"],
          "meaning": "optional meaning of the affix"
        },
        ...
      ]
    },
    "suffixes":[
        { "gender": "optional gender. If missing, considered unisex",
          "options": ["variations", "of one affix"],
          "meaning": "optional meaning of the affix"
        },
        ...
      ]
  },
  "surnames": {
    "prefixes":[
        { "gender": "optional gender. If missing, considered unisex",
          "options": ["variations", "of one affix"],
          "meaning": "optional meaning of the affix"
        },
      ...
      ]
    },
    "suffixes":[
        { "gender": "optional gender. If missing, considered unisex",
          "options": ["variations", "of one affix"],
          "meaning": "optional meaning of the affix"
        },
      ...
     ]
  }
}
```


