import argparse
import pickle
import random

parser = argparse.ArgumentParser(description="Markov name generator. Uses pretrained models to generate names")
parser.add_argument("model", nargs='+', type=file, help="The markov model(s) to use for name generation")
parser.add_argument("-n", type=int, help="The number of names to generate", default=10)
args = parser.parse_args()

models = list()
for model_file in args.model:
  model = pickle.load(model_file)
  models.append(model)
  
names = set()
while len(names) < args.n:
    model = random.choice(models)
    name = model.generate()
    names.add(name)

for name in names:
    print name
