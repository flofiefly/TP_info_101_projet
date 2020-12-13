'''Le plateau de jeu'''
def vide_tableau() :
    res = []
    for i in range(15) :
        res.append([])
        for j in range(15) :
            res[i].append('')
    return (res)
def init_bonus() :
    #premièrement on remplit un quart de tableau du bonus, c'est tableau "temp"
    temp = vide_tableau()
    for k in [[3,0],[11,0],[6,2],[8,2],[7,3],[6,6]] :
        temp[k[0]][k[1]] = 'LD'
    for k in [[5,1], [9,1], [5,5]] :
        temp[k[0]][k[1]] = 'LT'
    temp[0][0] = 'MT'
    temp[0][7] = 'MT'
    for k in range(4) :
        temp[1+k][1+k] = 'MD'
    #et après on le tourne en pi/2 3 fois autoure l'indice [7][7] (centre de tableau)
    #j'ai pas vu qu'on avait un ficher soutenu pour cet exercice ;^)
    res = vide_tableau()
    for i in range(15) :
        for j in range (15) :
            if temp[i][j] != '' :
                res[i][j] = temp[i][j]
                res[j][-i+14] = temp[i][j]
                res[-i+14][-j+14] = temp[i][j]
                res[-j+14][i] = temp[i][j]
    return (res)
def init_jetons() :
    return (vide_tableau())
def affiche_jetons(tabl, jetons, init, d) :
    k = 0
    res = tabl.copy()
    bon = init_bonus()
    jet = list(jetons)
    while (k < len(jet)) :
        if (d == 'droit') :
            i = init[0]
            j = init[1] + k
        elif (d =='bas') :
            i = init[0] + k
            j = init[1]
        res[i][j] = jet[k] + '_'
        k += 1
    for i in range(15) :
        for j in range(15) :
            if res[i][j] == '' :
                print ('*_' + bon[i][j], end = '')
            else :
                print(res[i][j] + bon[i][j], end = '')
        print('')
    return(res)
#le programme principal
tableau = affiche_jetons(vide_tableau(), 'jetons', [7,7], 'droit')
print('')
for i in init_bonus() :
    for j in i :
        if j == '' :
            print ('__', end = '')
        else :
            print(j, end = '')
    print('')
