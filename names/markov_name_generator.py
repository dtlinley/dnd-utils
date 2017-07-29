import argparse
import pickle

parser = argparse.ArgumentParser(description="Markov name generator. Uses pretrained models to generate names")
parser.add_argument("model", type=file, help="The markov model to use for name generation")
parser.add_argument("-n", type=int, help="The number of names to generate", default=10)
args = parser.parse_args()

model = pickle.load(args.model)
names = set()
while len(names) < args.n:
    name = model.generate()
    names.add(name)

for name in names:
    print name
