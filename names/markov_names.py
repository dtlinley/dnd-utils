import random


class Categorical(object):
    """A Categorical represents a distribution of observations, where the
    likelihood of any given observation defaults to `prior` 
    """

    def __init__(self, support, prior):
        self.counts = {x: prior for x in support}
        self.total = sum(self.counts.itervalues())

    def observe(self, event, count=1):
        self.counts[event] += count
        self.total += count

    def sample(self, dice=random):
        """Randomly sample one of the elements of `support` given the
        cumulative distribution function represented by this Categorical's
        observations
        """
        sample = dice.uniform(0, self.total)
        for event, count in self.counts.iteritems():
            if sample <= count:
                return event
            sample -= count

    def __getitem__(self, event):
        return self.counts[event] / self.total


class MarkovModel(object):
    """A higher-order Markov Model with Dirichlet Prior and Katz Back-off.
      
       A Markov model is a stochastic model used to model randomly changing systems where
       it is assumed that future states depend only on the current state.

       A Markov model of order `m` will consider the past `m` states when determining the
       value of the next state. When there is no history of order `m`, the model will
       attempt to find one of order `m-1`. This is refered to as Katz Back-off. This
       implementation assumes a Good-Turing weight of 1 and a threshold of 0, meaning they
       can be ignored.

       It is likely that the corpus used to train a Markov model will not be large enough
       to capture all of the relationships that exist, especially when using higher-order
       models. To correct for this, a Direchlet prior is used to apply additive smoothing
       to the ditribution of observations for any given prefix.
    """ 
    def __init__(self, support, order, prior, boundary_symbol=None):
        self.support = set(support)
        self.support.add(boundary_symbol)
        self.order = order
        self.prior = prior
        self.boundary = boundary_symbol
        self.prefix = [self.boundary] * self.order
        self.postfix = [self.boundary]
        self.counts = {}

    def _categorical(self, context):
        if context not in self.counts:
            self.counts[context] = Categorical(self.support, self.prior)
        return self.counts[context]

    def _backoff(self, context):
        """Katz Back-off. Attempt to find a history for this context,
        backing-off to smaller order histories if one cannot be found
        """
        context = tuple(context)
        if len(context) > self.order:
            context = context[-self.order:]
        elif len(context) < self.order:
            context = (self.boundary,) * (self.order - len(context)) + context

        while context not in self.counts and len(context) > 0:
            context = context[1:]
        return context

    def observe(self, sequence, count=1):
        sequence = self.prefix + list(sequence) + self.postfix
        for i in range(self.order, len(sequence)):
            context = tuple(sequence[i - self.order:i])
            event = sequence[i]
            for j in range(len(context) + 1):
                self._categorical(context[j:]).observe(event, count)

    def sample(self, context):
        context = self._backoff(context)
        return self._categorical(context).sample()

    def generate(self):
        sequence = [self.sample(self.prefix)]
        while sequence[-1] != self.boundary:
            sequence.append(self.sample(sequence))
        return sequence[:-1]

    def __getitem__(self, condition):
        event = condition.start
        context = self._backoff(condition.stop)
        return self._categorial(context)[event]

class NameGenerator(object):

    def __init__(self, name_file, order=3, prior=.001):
        names = set()
        support = set()
        for name in name_file:
            name = name.strip()
            if len(name) > 0:
                names.add(name)
                support.update(name)
        self.model = MarkovModel(support, order, prior)
        for name in names:
            self.model.observe(name)

    def generate(self):
        return ''.join(self.model.generate())
