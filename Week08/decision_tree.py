from typing import List
from typing import Any
import math
from collections import Counter

# pass in a list of probabilities
# compute entropy = sum(-pi * log2(pi))



def entropy(class_prop: list):
    return sum(-p * math.log(p, 2)for p in class_prop if p > 0)


# Data consist of pairs (input, labels)
# >>> compute class_prop
#
#
def class_prop(labels: List[Any]) -> List[float]:
    total = len(labels)
    return [count / total for count in Counter[labels].values()]

