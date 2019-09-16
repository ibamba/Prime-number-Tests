#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_pgcd(a, b) :
    if(a%b==0) : return b
    else : return my_pgcd(b, a%b)
    

def my_inverse(a, N):
    r0, r1 = a, N
    u0, u1 = 1, 0 #u0=b
    v0, v1 = 0, 1
    while(not(r1==0)):
        q = int(r0/r1)
        r, u, v = r1, u1, v1
        r1 = r0 - q * r1
        u1 = u0 - q * u1
        v1 = v0 - q * v1
        r0, u0, v0= r, u, v
    if (r0 == 1): 
        return u0
    raise ValueError(a,' et ', N, ' ne sont pas premiers entre-eux')
       
        
def my_binary_decomposition(n):
    a=[]
    def my_binary_decomposition_aux(n, a):
        if(n>0) : 
            a.append(n%2)
            return my_binary_decomposition_aux(int(n/2), a)
        return a
    return my_binary_decomposition_aux(n, a)


def my_expo_mod(g,n,N):
    h=1
    a=my_binary_decomposition(n)
    for i in range (len(a)-1, -1, -1):
        h=(h**2)%N
        if (a[i]==1):
            h=(h*g)%N
    return h        