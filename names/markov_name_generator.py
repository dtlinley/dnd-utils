import argparse
import pickle
import random

parser = argparse.ArgumentParser(description="Markov name generator. Uses pretrained models to generate names")
parser.add_argument("model", nargs='+', type=file, help="The markov model(s) to use for name generation")
parser.add_argument("-n", type=int, help="The number of names to generate", default=10)
parser.add_argument("--min", type=int, help="The minimum size of a name", default=1)
parser.add_argument("--max", type=int, help="The maximum size of a name", default=15)
parser.add_argument("-i", "--iterations", dest="iterations", type=int, help="The maximum number of attempts to create the names", default=1000)
args = parser.parse_args()

models = list()
for model_file in args.model:
  model = pickle.load(model_file)
  models.append(model)
  
names = set()
i = 0
while len(names) < args.n and i < args.iterations:
    model = random.choice(models)
    name = model.generate()
    if len(name) >= args.min and len(name) <= args.max:
        names.add(name)
    i += 1

for name in names:
    print name
