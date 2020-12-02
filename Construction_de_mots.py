#  - Construction de mots
def generer_dico(nf) :
    res = []
    for ligne in nf :
        res.append(ligne)
    return(res)


def mot_jouable(mot, ll, en_table) :
    temp = []
    for i in ll :
        temp.append(i)
    for i in en_table :
        temp.append(i)
    for i in list(mot) :
        if i in temp :
            temp.remove(i)
        elif ('?' in temp) :
            temp.remove('?')
        else :
            return(False)
    return(True)
def mots_jouable(motsfr, ll) :
    res = []
    for i in motsfr :
        if mot_jouable(i, ll) :
            res.append(i)
    return(res)
