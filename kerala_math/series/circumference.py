#! /usr/bin/env python
#
#  Various series for circumference derived by the kerala school
#

# The vyAse vAridhinihate series
def vyase(v, n=10, antya_samskara=None):
    '''
    Calculates the paridhi (circumference) from the vyAsa (diameter)

    Uses the famous Madhava series

    व्यासे वारिधिनिहते रूपहृते व्याससागराभिहते ।
    त्रिशरादिविषमसंख्याभक्तमृणं स्वं पृथक्क्रमात् कुर्यात् ॥

    Inputs:
                   v: diameter
                   n: number of terms
      antya_samskara: end_term
    Returns:
                   p: circumference
    '''
    t = 4*v  # First term
    p = t
    s = -1   # Sign of next term
    # C = 4v - 4v/3 + 4v/5 - 4v/7 ...
    for i in range(n-1):
        p += s*t/(2*(i+1)+1)
        s = s*-1
    # Add end term
    if antya_samskara == 0:
        # Zeroth order correction
        pass
    return p


__all__ = ["vyase"]
