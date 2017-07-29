mkdir -p city/models/
mkdir -p human/models/

python markov_model_builder.py -o 5 city/corpora/american.txt > city/models/american.mrkv
python markov_model_builder.py -o 4 city/corpora/england.txt > city/models/english.mrkv
python markov_model_builder.py -o 4 city/corpora/ireland.txt > city/models/irish.mrkv
python markov_model_builder.py -o 3 city/corpora/scotland.txt > city/models/scotish.mrkv
python markov_model_builder.py -o 3 human/corpora/anglo_saxon/anglo_saxon_male_dithematic.txt \
  human/corpora/anglo_saxon/anglo_saxon_male_monothematic.txt \
  > human/models/anglo_male.mrkv
python markov_model_builder.py -o 3 human/corpora/anglo_saxon/anglo_saxon_female_dithematic.txt \
  human/corpora/anglo_saxon/anglo_saxon_female_monothematic.txt \
  > human/models/anglo_female.mrkv
