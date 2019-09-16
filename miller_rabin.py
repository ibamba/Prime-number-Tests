from carmichael import *

#4.a]

# renvoie h et m tel que N=1+(2**h)*m
def decomp(N):
    h=0
    m=N-1
    while(m%2==0):
        m=m//2
        h=h+1
    return h,m

# test de rabin miller
def test_miller_rabin(n):
    h,m= decomp(n)
    T=1
    for i in range(1, T) :
        #on choisit un a aletaoirment dans Z/nZ*
        a=n
        while(my_pgcd(n, a)!=1) : # a n'appartient pas à Z/nZ*
            a=randint(2, n-1)
        #on a trouvé un a dans Z/nZ*
        b=my_expo_mod(a, m, n)
        if not(b==1 or b==n-1) :
            for j in range(1, h) :
                if b!=1 and my_expo_mod(b, 2, n)==1 :
                    return False, 'COMPOSE'
                b=my_expo_mod(b, 2, n)
            if b!=n-1 :
                return False, 'COMPOSE'
    
    return True, 'PREMIER'



#4.b] Tests du test de rabin_miller
    
    #1) Nombres retournés par gen_carmichael
def miller_rabin_carmichael(nb)  :
    for i in range(nb) :
        n=gen_carmichael()
        print(n, ':', test_miller_rabin(n)[1])

print('\nTEST DE MILLER_RABIN AVEC DES NOMBRES RETOURNES PAR gen_carmichael :')
miller_rabin_carmichael(5)

    #2) Nombres composés
def miller_rabin_compose() :
    composes=[3272, 5, 10**5, 2**16, 2**32]
    for i in range(len(composes)) :
        print(composes[i], ':', test_miller_rabin(composes[i])[1])

print('\nTEST DE MILLER RABIN AVEC DES NOMBRES COMPOSES :')
miller_rabin_compose()

     #3) Nombres aléatoires
def miller_rabin_alea(nb) :
    for i in range(nb) :
        n=randint(2, 10**5)
        print(n, ':', test_miller_rabin(n)[1])

print('\nTEST DE MILLER RABIN AVEC DES NOMBRES ALEATOIRES :')
miller_rabin_alea(5)



#4.c] Probabilité d'erreur
def proba_erreur_miller_rabin(N):
    echec=0
    taberreur=[]
    for n in range (3,N) :
        if(test_miller_rabin(n)[0]) :
            if( not first_test(n)) : 
                echec+=1
                taberreur.append(n)
    
    return echec/N, taberreur

P=proba_erreur_miller_rabin(10**5)
print("\nLa probabilité d'erreur du test de Fermat pour des entiers < 10^5 est : ", P[0])
print('Il se goure pour les nombres suivants :', P[1])    



#4.d] générateur rsa
def gen_rsa(t) :
    if t<0 : return -1
    p=randint(2**(t-1), 2**t)
    q=randint(2**(t-1), 2**t)
    while not(test_miller_rabin(p)[0]) :
        p=randint(2**(t-1), 2**t)
    while not(test_miller_rabin(q)[0]) :
        q=randint(2**(t-1), 2**t)
    return p, q, p*q

print("\nNombres N=p*q pour rsa utilisant Miller-Rabin :")
N1=gen_rsa(7)
print(N1[0], '*', N1[1], '=', N1[2])
N2=gen_rsa(3)
print(N2[0], '*', N2[1], '=', N2[2])
