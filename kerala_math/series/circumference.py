#! /usr/bin/env python
#
#  Various series for circumference derived by the kerala school
#
import numpy as np
from fractions import Fraction 

# The vyAse vAridhinihate series
def vyase(v, n=10, antya_samskara=None, calc_type="fraction"):
    '''
    Calculates the paridhi (circumference) from the vyAsa (diameter)

    Uses the famous Madhava series

    व्यासे वारिधिनिहते रूपहृते व्याससागराभिहते ।
    त्रिशरादिविषमसंख्याभक्तमृणं स्वं पृथक्क्रमात् कुर्यात् ॥

    Inputs:
                   v: diameter
                   n: number of terms
      antya_samskara: None (default) or
                      k for kth order end-correction
                      where k in (0, 1, 2, 3)
           calc_type: "fraction" (default): uses fractions
                      "float": uses numpy float128
    Returns:
                   p: circumference
    '''
    assert ((calc_type == "fraction") or (calc_type == "float")), \
        f"Unknown calc_type {calc_type}: pass 'float' or 'fraction'"
    if calc_type == "fraction":
        t = Fraction(4*v, 1) # First term
    else:
        t = np.float128(4*v)  # First term
    # Initialize the series to first term
    s = t     
    sg = -1   # Sign of next term
    # C = 4v - 4v/3 + 4v/5 - 4v/7 ...
    for i in range(2, n+1):   # Ends after the nth term
        s += sg*t/(2*i - 1)    # 4v/(2n-1) is the last term
        sg *= -1
    # Add end term
    # Last divisor
    if antya_samskara == 0:
        # Zeroth order correction
        # a_p = 4v/2p, where 4v/p is the last term
        p = 2*n - 1
        s += sg*t/(2*p)
    elif antya_samskara == 1:
        # First order
        # a_p = 4v/(2p+2) = 4v/4n 
        s += sg*t/(4*n)
    elif antya_samskara == 2:
        # Second Order
        # a_p = 4v/((2p+2) + 4/(2p+2))
        #     = 4v.n/(4n^2 + 1)
        s += sg*t*n/(4*n**2 + 1)
    elif antya_samskara == 3:
        # Third Order
        # a_p = 4v/((2p+2) + 4/((2p+2) + 16/(2p+2)))
        #     = 4v.(n^2 + 1)/(4n^3+5n)
        s += sg*t*(n**2 + 1)/(4*n**3 + 5*n)
    return s

# The vyAsavargAdravihatAt series
def vyasavargad(v, n=10, calc_type="fraction"):
    '''
    Calculates the paridhi (circumference) from the vyAsa (diameter)

    Uses the vyAsavargAdravihatAt series
    vyāsavargād ravihatāt padam syāt prathamam phalam |
    tadāditastrisamkhyāptam phalam syāduttarottaram ||
    rupādyayugmasamkhyābhirhr.tes.ves.u yathākramam |
    vis.amānāmyutestyaktvā samam hi paridhirbhavet ||

    Inputs:
                   v: diameter
                   n: number of terms
           calc_type: "fraction" (default): uses fractions
                      "float": uses numpy float128
    Returns:
                   p: circumference
    '''
    assert ((calc_type == "fraction") or (calc_type == "float")), \
        f"Unknown calc_type {calc_type}: pass 'float' or 'fraction'"
    if calc_type == "fraction":
        # Fixme implement Aryabhata square root algo
        t = Fraction(np.sqrt(12 * v**2)) # First term
    else:
        t = np.sqrt(np.float128(12 * v**2))  # First term
    p = t
    s = -1   # Sign of next term
    # C = sqrt(12d^2) (1 - 1/3.3 + 1/(3^2.5)+1/(3^3.7) ...) 
    for i in range(1,n):
        if calc_type == "fraction":
            p += Fraction(s*t, (3**i*(2*i+1)))
        else:
            p += s*t/np.float64(3**i*(2*i+1))

        s = s*-1
    return p


__all__ = ["vyase", "vyasavargad"]
