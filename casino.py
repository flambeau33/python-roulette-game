import random
from math import ceil
import time

pf=-1
while(1) and pf!=0:
    while(pf<0):
        pf=input("Somme initiale: ")
        try:
            pf=int(pf)
            if pf<=0:
                raise ValueError
        except ValueError:
            print("Montant invalide ")
            print(f"{pf}")
            pf=-1 #tant que la valeur est mauvaise je met pf à -1
    print(f"le joueur s'installe sur la table avec {pf} Euros")
    time.sleep(1)
    num_mise=-1
    while num_mise<0:
        num_mise=input('\nEntrez le numéro de la mise: ')
        try:
            num_mise=int(num_mise)
            if num_mise < 0 or num_mise > 49:
                raise ValueError
        except ValueError:
            print("Nombre saisi invalide")
            print(f"{num_mise}")
            num_mise=-1
    
    gain=-1
    while gain<0 :
        try:
            gain=int(input('\nEntrez le montant de la mise: '))
            if gain>pf or gain<0:
                raise ValueError
        except ValueError:
            print("Montant invalide (entrez un montant superieur ou egal au momtant deposé)")
            gain=-1

    if pf==gain:
        print('...Ouhh vous etes tres audacieux ')
        time.sleep(1)
    
        
    print("le jeu va bientot commencer...")
    time.sleep(2)
    print("\n######### LANCEMENT DE LA ROULETTE ###############\n")
    for i in range(1,6):
        print('La roulette tourne...')
        flash= " " * random.randint(0,20) + "🎰"
        print(flash)
        time.sleep(1)
    x=random.randint(0,49)
    time.sleep(2)
    print("la roulette tourne et s'arrete sur le numéro ... ")
    time.sleep(2)
    print(f"\t!! {x} !!")
    if x==num_mise:#si le numéro misé est identique au numero de la roulette on triple son gain
        gain*=3
        print(f"\nGagnez!! ;) vous remportez {gain} Euro(s)")
        pf+=gain
    elif (x%2 == num_mise % 2): #sinon si les 2 numeros sont pairs ou les 2 sont impairs
        gain=ceil(gain/2)
        pf+=gain
        print(f"\npas mal :\ vous remportez {gain} Euro(s)")
    else:
        pf-=gain
        print("Perdu :(")
    if(pf==0):
        print("\nVous etes fauchés :( aurevoir...")
        break
    num_mise=-1
    match input(f"il vous reste {pf} Euro(s) voulez vous conntinuer ? (O/N)").lower():
        case  'o'|'y':
            continue
        case _:
            print('\nAurevoir :) ...')
            time.sleep(1)#ou bien j'indente break dans 'match'
            #break
    break
    