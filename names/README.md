# Name Generation
Data and tools for the creation of names

## Markov Name Generation

Randomly generate names using a markov process. Starter models can be created by running the `build` script.

The simplest case is generating names from a single corpus
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

It is more common to want names generated from many different sources. In this case, generating names from multiple models at the same time
```
python markov_name_generator.py -n 20 \
> city/models/american.mrkv \
> city/models/english.mrkv 
Kalamazoo
Great Torringham
Bodmin
Lubec
Burgess Hill
Jarrow
Benton
Epworth
Burnley
Guildford-upon Trentwood
Manitowoc
Brandon
Hobart
Newport
Crediton
Michigan City
Evansville
Belper
Bulwell
Neosho
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

