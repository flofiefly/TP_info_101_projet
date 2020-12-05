'''La pioche'''

import random as rd

def ini_dico() :
    res = {' A': {'occ': 9 ,'valeur': 1} , ' B': {'occ': 2 ,'valeur': 3} , ' C': {'occ': 2 ,'valeur': 3} , ' D': {'occ': 3 ,'valeur': 2} , ' E': {'occ': 15 ,'valeur': 1} , ' F': {'occ': 2 ,'valeur': 4} , ' G': {'occ': 2 ,'valeur': 2} , ' H': {'occ': 2 ,'valeur': 4} , ' I': {'occ': 8 ,'valeur': 1} , ' J': {'occ': 1 ,'valeur': 8} , ' K': {'occ': 1 ,'valeur': 10} , ' L': {'occ': 5 ,'valeur': 1} , ' M': {'occ': 3 ,'valeur': 2} , ' N': {'occ': 6 ,'valeur': 1} , ' O': {'occ': 6 ,'valeur': 1} , ' P': {'occ': 2 ,'valeur': 3} , ' Q': {'occ': 1 ,'valeur': 8} , ' R': {'occ': 6 ,'valeur': 1} , ' S': {'occ': 6 ,'valeur': 1} , ' T': {'occ': 6 ,'valeur': 1} , ' U': {'occ': 6 ,'valeur': 1} , ' V': {'occ': 2 ,'valeur': 4} , ' W': {'occ': 1 ,'valeur': 10} , ' X': {'occ': 1 ,'valeur': 10} , ' Y': {'occ': 1 ,'valeur': 10} , ' Z': {'occ': 1 ,'valeur': 10} , '?': {'occ': 2 ,'valeur': 0} } 
    return(res)
def init_pioche(dico) :
    res = []
    for lettre in dico :
        for k in range(dico[lettre]['occ']) :
            res.append(lettre)
    return(res)
def pioche(x, sac) :
    res = []
    for i in range(x) :
        n = rd.randint(len(sac))
        res.append(sac.pop(n))
    return(res)
def completer_main(main, sac) :
    x = 7 - len(main)
    if len(sac) < x :
        x = len(sac)
    temp = pioche(x, sac)
    for i in temp :
        main.append(i)
