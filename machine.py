import random, copy, math
class BigSet:
    def __init__(self):
        self.cardinality = 100
        self.elements = []
        for i in range(self.cardinality):
            self.elements.append(random.randrange(0,10))

class SubSet:
    def __init__(self, rango: int, bigsete: list):
        if not (isinstance(rango, int) or isinstance(bigsete, list)):
            raise NotImplementedError
        self.elements = []
        for i in range(rango):
            self.elements.append(bigsete.pop(random.randrange(0, len(bigsete) - 1)))


def variance(sampleSet, n):
    # Sum of squared difference between each element and the median divided by n 
    if not isinstance(sampleSet, list):
        raise NotImplementedError
    sampleSet.sort()
    if len(sampleSet) % 2 == 0:
        median = (sampleSet[int(len(sampleSet) / 2) - 1] + sampleSet[int(len(sampleSet) / 2)]) / 2
    else:
        median = sampleSet[int((len(sampleSet) - 1) / 2)]
    total = 0
    for e in sampleSet:
        total += math.pow(e - median, 2)
    return total / n


def Main():
    bigset = BigSet()
    # i would want another function to take rid of subsets

    subset = SubSet(9, copy.copy(bigset.elements))    
    print(f'Real variance: {variance(bigset.elements,len(bigset.elements)-1)}\nEstimated variance:{variance(subset.elements,len(subset.elements)-1)}')

Main()