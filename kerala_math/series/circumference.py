#! /usr/bin/env python
#
#  Various series for circumference derived by the kerala school
#

# The vyAse vAridhinihate series
def vyase(v, n=10, antya_samskara=None):
    '''
    Calculates the paridhi (circumference) from the vyAsa (diameter)

    Uses the famous Madhava series
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
    for i in range(n-1):
        p += s*t/(2*(i+1)+1)
        s = s*-1
    # FIXME add end term
    return p


__all__ = ["vyase"]
