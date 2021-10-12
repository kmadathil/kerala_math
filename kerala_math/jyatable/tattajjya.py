import numpy as np
from fractions import Fraction 
from kerala_math.jyatable import MST

_k = [0 for i in range(24)]
_b = [0 for i in range(24)]

# First two accurate jyas
_b[0] = MST(224, 50, 22) 
_b[1] = MST(448, 42, 58)

# tattajya recurrence
for i in range(2,24):
    _b[i] = ((_b[i-1])**2 - (_b[0])**2)/_b[i-2] 

# Pindajyas
_k[0] = _b[0]
for i in range(1,24):
    _k[i] = _b[i] - _b[i-1]

    
def khandajya(k: int):
    """
    Return the kth khandajya computed by the tattajya recurrence

    Inputs:
      k (int) : index from 0 to 23
    Outputs:
      int : kth khandajya
    """
    assert ((k>=0) & (k<24)), f"Input must be between 0 and 23 inclusive, got {k}"
    return _k[k]

def pindajya(k: int):
    """
    Return the kth pindajya computed by the tattajya recurrence

    Inputs:
      k (int) : index from 0 to 23
    Outputs:
      int : kth pindajya
    """
    assert ((k>=0) & (k<24)), f"Input must be between 0 and 23 inclusive, got {k}"
    return _b[k]
