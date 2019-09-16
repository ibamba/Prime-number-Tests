#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
from pylab import *
from arithmetic import *
import time

def time_pgcd(a, b) :
    deb=time.time()
    my_pgcd(a, b)
    fin=time.time()
    return fin-deb

def trace_pgcd() :
    a, b=[], []
    x, y=[], []
    for i in range(1, 11) :
        a.append(randint(10**(i-1), 10**i))
        b.append(randint(10**(i-1), 10**i))
    for i in range(10) :
        x.append(10**i)
        y.append(time_pgcd(a[i], b[i]))
    
    plot(x,y)    
    show()

trace_pgcd()

def time_inverse(a, N) :
    # my_inverse renvoie une exception si a et N ne sont pas premier entre-eux
    # il faut donc la catcher
    try :
        deb=time.time()
        my_inverse(a, N)
        fin=time.time()
    except :
        fin=time.time()
        
    return fin-deb

def trace_inverse() :
    a, N=[], []
    x, y=[], []
    for i in range(1, 11) :
        a.append(randint(10**(i-1), 10**i))
        N.append(randint(10**(i-1), 10**i))
    for i in range(10) :
        x.append(10**i)
        y.append(time_inverse(a[i], N[i]))
    
    plot(x,y)    
    show()
    
trace_inverse()
