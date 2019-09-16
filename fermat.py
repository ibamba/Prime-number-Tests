from random import randint
from arithmetic import *
from carmichael import *

def test_fermat(N) :
    #si N premier alors a premier avec N et par le test de Fermat, a^n=a mod N => a^n-1 = 1 mod N puisque a inversible dans Z/NZ
    #le test a^n=a mod N revient donc à tester si a^n-1 = 1 mod N
    # b=a^N-1 mod N( par exponentation rapide)
    a=randint(2, 16)
    b=my_expo_mod(a,N-1,N)
    if b==1 :
        return True, 'PROBABLEMENT PREMIER'
    else:
        return False, 'COMPOSE'

test_fermat(561)


#3.b] Tests de Fermat
     
    #1) Nombres retournés par gen_carmichael
def fermat_carmichael(nb)  :
    for i in range(nb) :
        n=gen_carmichael()
        print(n, ':', test_fermat(n)[1])

print('\nTEST DE FERMAT AVEC DES NOMBRES RETOURNES PAR gen_carmichael :')
fermat_carmichael(5)

    #2 Nombres composés
def fermat_compose() :
    composes=[3272, 5, 10**5, 2**16, 2**32]
    for i in range(len(composes)) :
        print(composes[i], ':', test_fermat(composes[i])[1])

print('\nTEST DE FERMAT AVEC DES NOMBRES COMPOSES :')
fermat_compose()

    #3 Nombres aléatoires
def fermat_alea(nb) :
    for i in range(nb) :
        n=randint(2, 10**5)
        print(n, ':', test_fermat(n)[1])

print('\nTEST DE FERMAT AVEC DES NOMBRES ALEATOIRES :')
fermat_alea(5)

#3c] Probabilité d'erreur
def proba_erreur_fermat(N):
    echec=0
    taberreur=[]
    for n in range (2,N) :
        if(test_fermat(n)[0]) :
            if( not first_test(n)) : 
                echec+=1
                taberreur.append(n)
    
    return echec/N, taberreur

P=proba_erreur_fermat(10**5)
print("\nLa probabilité d'erreur du test de Fermat pour des entiers < 10^5 est : ", P[0])
print('Il se goure pour les nombres suivants :', P[1])     
