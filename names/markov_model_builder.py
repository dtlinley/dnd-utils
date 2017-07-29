import argparse
import pickle
from markov_names import NameGenerator

parser = argparse.ArgumentParser(description="Markov model trainer. Outputs a pickled markov model")
parser.add_argument("corpus", nargs='+', type=file, help="All corpus files used to train the model")
parser.add_argument("-p", "--prior", dest="prior", type=float, help="The prior", default=0.0)
parser.add_argument("-o", "--order", dest="order", type=int, help="The maximum order of the model", default=1)
args = parser.parse_args()

corpora = set()
for corpus in args.corpus:
    texts = set(text.strip() for text in corpus)
    corpora.update(texts)

model = NameGenerator(corpora, args.order, args.prior)
pickled = pickle.dumps(model)
print pickled

