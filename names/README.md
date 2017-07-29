# Name Generation
Data and tools for the creation of names

## Markov Name Generation

Randomly generate names using a markov process. The simplest case is generating names from a single corpus
```
python markov_model_builder.py -o 5 city/corpora/american.txt > city/models/american.mrkv
python markov_name_generator.py -n 15 city/models/american.mrkv
Amana Colonies
Willmar
Lakewood
Phoenix
Woodward
New Harmony
East Haven
Calais
Oraibi
Alamogordo
Breckenridge
Wayne
Hood River
Biddeford
Homestead
```

A more advanced (and somewhat chaotic) approach is to combine corpora into one model
```
python markov_model_builder.py -o 4 \
 human/corpora/english_surname/localities.txt \
 human/corpora/english_surname/byname.txt \
 > human/models/english_surnames.mrkv
python markov_name_generator.py -n 15 human/models/english_surnames.mrkv 
Leafe
Newnham
Orpet
Grill
Fidge
Dove
Skeate
Pullalove
Veale
Bonser
Stretchett
Poe
Smollett
Bradfer
Stripling
```

