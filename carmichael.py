#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from arithmetic import my_expo_mod
from arithmetic import my_pgcd
from random import randint

premiers=[2 ,3 ,5 ,7 ,11 ,13 ,17 ,19 ,23 ,29 ,31 ,37 ,41 ,43 ,47 ,53 ,59 ,61 ,67 ,71 ,73 ,79 ,83 ,89 ,97,
          101,103,107,109,113,127 ,131 ,137 ,139 ,149 ,151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233 ,239 ,241 ,251 ,257 ,
          263 ,269 ,271 ,277 ,281 ,283 ,293 ,307 ,311 ,313 ,317 ,331 ,337 ,347 ,349 ,353 ,359 ,367 ,373 ,379 ,383 ,389 ,397 ,401 ,409 ,419 ,421 ,431 ,433 ,
          439 ,443 ,449 ,457 ,461 ,463 ,467 ,479 ,487 ,491 ,499 ,503 ,509 ,521 ,523 ,541 ,547 ,557 ,563 ,569 ,571 ,577 ,587 ,593 ,599 ,601 ,607 ,613 ,617 ,
          619 ,631 ,641 ,643 ,647 ,653 ,659 ,661 ,673 ,677 ,683 ,691 ,701 ,709 ,719 ,727 ,733 ,739 ,743 ,751 ,757 ,761 ,769 ,773 ,787 ,797 ,809 ,811 ,821 ,
          823 ,827 ,829 ,839 ,853 ,857 ,859 ,863 ,877 ,881 ,883 ,887 ,907 ,911 ,919 ,929 ,937 ,941 ,947 ,953 ,967 ,971 ,977 ,983 ,991 ,997]

def first_test(N) :
    for i in range(2, int(sqrt(N))+1):
        if (N%i==0): return False
    return True
    
def compt_first(N) :
    res=0
    for i in range(1, N) :
        if(first_test(i)) : res+=1
    return res

print('\nle nombres de nombres premiers < 10^5 est : ', compt_first(10**5), '\n')

def gen_carmichael(N):
    print('\nLes nombres de Carmichael < ', N, ' sont : ')
    #On sait que le premier nbre de Carmichael est 561
    for n in range(561, N) :
        if(not(first_test(n))) : # n est composé
            flag=True
            # on test si n est un nbre de Charmichael
            for a in range(1, n) :
                # on test si pour tout a appartient Z/nZ* 
                if(my_pgcd(n, a)==1) :
                    if(not(my_expo_mod(a, n-1, n)==1)) : # si a^n-1 = 1 mod n
                        flag=False # sinon n n'est pas un nbre de Carmichael
                        break
            if(flag) : print(n, ' ')
    print('\n')

gen_carmichael(10**5)


def gen_carmichael() :
    len_p=len(premiers)

    while(True) :
        p1=premiers[randint(1, len_p-1)]
        i=0
        while i<10 :
            p2=premiers[randint(1, len_p-1)]
            if p2!=p1 :
                j=0
                while j<10 :
                    p3=premiers[randint(1, len_p-1)]
                    if p3!=p2 and p3!=p1 :
                        N=p1*p2*p3
                        if ((N-1)%(p1-1)==0) and ((N-1)%(p2-1)==0) and ((N-1)%(p3-1)==0) :
                            print('Nombre de Carmichael à 3 facteurs premiers :', N, '=', p1, '*', p2, '*', p3)
                            return N
                        j+=1
                i+=1

gen_carmichael()
