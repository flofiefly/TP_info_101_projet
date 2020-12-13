'''valeur d'un mot '''
def valeur_mot(mot, dico, plateau, i, j, dir) :
    res = 0
    bonus = init_bonus()
    n = len(mot)
    l = list(mot)
    k_m = 1      #coefficient de mot
    longueur = 0
    if dir == 'droit' :
        k = 0
        while (k < n) :
            if plateau[i][j+k] == '' :
                if bonus[i][j+k] == 'LD' :
                    res += dico[l[k]]['valeur']*2
                elif bonus[i][j+k] == 'LT' :
                    res += dico[l[k]]['valeur']*2
                elif bonus[i][j+k] == 'MD' :
                    k_m *= 2
                elif bonus[i][j+k] == 'MT' :
                    k_m *= 3
                else :
                    res += dico[l[k]]['valeur']
                longueur += 1
            k += 1
        res *= k_m
    elif dir == 'bas' :
        k = 0
        while (k < n) :
            if plateau[i+k][j] == '' :
                if bonus[i+k][j] == 'LD' :
                    res += dico[l[k]]['valeur']*2
                elif bonus[i+k][j] == 'LT' :
                    res += dico[l[k]]['valeur']*2
                elif bonus[i+k][j] == 'MD' :
                    k_m *= 2
                elif bonus[i+k][j] == 'MT' :
                    k_m *= 3
                else :
                    res += dico[l[k]]['valeur']
                longueur += 1
            k += 1
        res *= k_m
            
    if longueur == 7 :
        res += 50
    return(res)
def meilleur_mot(motsfr, ll, dico, plateau, i, j, dir) :
    mj = mots_jouables(motsfr, ll)
    if mj == [] :
        return('')
    res = mj[0]
    for m in mj :
        if valeur_mot(m, dico, plateau, i, j, dir) > valeur_mot(res, dico, plateau, i, j, dir) :
            res = m
    return(res)
def meilleurs_mots(motsfr, ll, dico, plateau, i, j, dir) :
    mj = mots_jouables(motsfr, ll)
    if mj == [] :
        return([])
    res = ['']
    for m in mj :
        if valeur_mot(m, dico, plateau, i, j, dir) > valeur_mot(res[0], dico, plateau, i, j, dir) :
            res = [m]
        elif valeur_mot(m, dico, plateau, i, j, dir) == valeur_mot(res[0], dico, plateau, i, j, dir) :
            res.append(m)
    return(res)

#test :
dico = init_dico()
plateau = init_jetons()
i = 7
j = 7
dir = 'droit'
print(valeur_mot('ABACA',dico, plateau, i, j, dir))
print(meilleur_mot(['AA', 'AB', 'AC'], ['A', 'B', 'C'], dico, plateau, i, j, dir))
print(meilleurs_mots(['AA', 'AB', 'AC'], ['A', 'B','C'], dico, plateau, i, j, dir))
