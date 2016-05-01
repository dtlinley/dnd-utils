# Dwarf Name File Format

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


