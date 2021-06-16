#! /usr/bin/env python
#
#  Various series for jya / sara etc derived by the kerala school
#


import numpy as np
from kerala_math.jyatable import MST

# srIrudraH sRIDaraH shresTho devo vishvasthalI bhrguH
R = MST(3437, 44, 48, 22, 29, 22, 22)
#  devo vishvasthalI bhrguH
#R = MST(3437, 44, 48, 42)
_Rf = float(R)

# Nihatya cApavargeNa ... 
def jya_nihatya(s, terms=10, mst_out=False):
    j = s # Zeroth Approximation
    t = j # Previous Term 
    sg = -1 # Next sign
    m = s**2 / (_Rf**2) # Multiplier
    for i in range(1, terms):
        t *= m / (2*i + (2*i)**2)
        j += sg*t
        sg *= -1
    if mst_out:
        return MST(j)
    else:
        return j


# Nihatya cApavargeNa ... 
def sara_nihatya(s, terms=10, mst_out=False):
    j = s**2/(2*_Rf) # Zeroth Approximation
    t = j # Previous Term 
    sg = -1 # Next sign
    m = s**2 / (_Rf**2) # Multiplier
    for i in range(1, terms):
        t *= m/((2*(i+1))**2-2*(i+1))
        j += sg*t
        sg *= -1
    if mst_out:
        return MST(j)
    else:
        return j

# vidvAnstunnabalaH
def jya_vidvan(s, mst_out=False):
    vt = [
        MST(0,0,44), MST(0, 33, 6), MST(16,5,41),
        MST(273, 57, 47), MST(2220, 39, 40)
    ]
    # Square of 5400 = नानाज्ञानतपोधरः
    q2 = 29160000
    # cube of 5400 = अज्ञाननुन्ने नवतत्त्वसंशयः
    q3 = 157464000000
    s2 = s**2
    s3 = s**3
    m2 = s2/q2
    m3 = s3/q3
    t = 0
    for v in vt:
        t = float(v) - m2*t
    j = s - m3*t
    if mst_out:
        return MST(j)
    else:
        return j
   

# stenastrI
def sara_stena(s, mst_out=False):
    vt = [
        MST(0,0,6), MST(0, 5, 12), MST(3, 9, 37), MST(71, 43, 24),
        MST(872, 3, 5), MST(4241, 9, 0)
    ]
    # Square of 5400 = नानाज्ञानतपोधरः
    q2 = 29160000
    s2 = s**2
    m2 = s2/q2
    t = 0
    for v in vt:
        t = m2*(float(v) - t)
    j = t
    if mst_out:
        return MST(j)
    else:
        return j
    
