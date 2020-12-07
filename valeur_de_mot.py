'''valeur d'un mot '''
def valeur_mot(mot, dico) :
    res = 0
    for l in list(mot) :
        res += dico[l]['valeur']
    if len(mot) == 7 :
        res += 50
    return(res)
def meilleur_mot(motsfr, ll, dico) :
    mj = mots_jouables(motsfr, ll)
    if mj == [] :
        return('')
    res = mj[0]
    for m in mj :
        if valeur_mot(m, dico) > valeur_mot(res, dico) :
            res = m
    return(res)
def meilleurs_mots(motsfr, ll, dico) :
    mj = mots_jouables(motsfr, ll)
    if mj == [] :
        return([])
    res = [mj[0]]
    for m in mj :
        if valeur_mot(m, dico) > valeur_mot(res, dico) :
            res = [m]
        elif valeur_mot(m, dico) == valeur_mot(res, dico) :
            res.append(m)
    return(res)
