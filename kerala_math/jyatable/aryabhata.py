import numpy as np
from fractions import Fraction 

_k = [0 for i in range(24)]
_b = [0 for i in range(24)]

_k[0] = _b[0] = 225

# Aryabhata recurrence relations
for i in range(1,24):
    _k[i] = _k[i-1] - _b[i-1]/_b[0]
    _b[i] = _b[i-1] + _k[i]


def khandajya(k: int):
    """
    Return the kth khandajya computed by the aryabhata recurrence

    Inputs:
      k (int) : index from 0 to 23
    Outputs:
      int : kth khandajya
    """
    assert ((k>=0) & (k<24)), f"Input must be between 0 and 23 inclusive, got {k}"
    return float(_k[k])

def pindajya(k: int):
    """
    Return the kth pindajya computed by the aryabhata recurrence

    Inputs:
      k (int) : index from 0 to 23
    Outputs:
      int : kth pindajya
    """
    assert ((k>=0) & (k<24)), f"Input must be between 0 and 23 inclusive, got {k}"
    return float(_b[k])
