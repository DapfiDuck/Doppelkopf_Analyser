from math import erf
from math import sqrt
from math import log
from math import e

def pdf_area(d, sigma):
    return -0.5*erf(-sqrt(2)*d/(2*sigma))+0.5*erf(-sqrt(2)*(-d)/(2*sigma))

def radius(p, sigma):
    #Returns the radius around my that produces the Probability p
    #in a normal-distribution of sigma
    return erfinv(p)*2*sigma/sqrt(2)

def erf(x):
    return math.erf(x)

def erfinv(y):
    # this is a rough approximation of erfinv which diverges
    # from erfinv between -0.02 and +0.02
    # For a similar method refer to “An Ad hoc Approximation to the Gauss Error Function and a Correction Method” by Beong In Yun (Applied Mathematical Sciences, Vol. 8, 2014, no. 86)
    # http://www.m-hikari.com/ams/ams-2014/ams-85-88-2014/yunAMS85-88-2014.pdf
    b = 2.4095
    x = -log(2/(1+y)-1)/b
    return x

def sigma(p, n):
    return sqrt(n*p*(1-p))
