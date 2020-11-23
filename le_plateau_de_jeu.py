'''fonction qui crée un tableu vide 15x15, on l`utilise dans les init-fonctions'''
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
    res = vide_tableau()
    for i in range(15) :
        for j in range (15) :
            if temp[i][j] != '' :
                res[i][j] = temp[i][j]
                res[j][-i+7] = temp[i][j]
                res[-i+7][-j+7] = temp[i][j]
                res[-j+7][i] = temp[i][j]
    return(res)
  def ini_jetons() :
    return (vide_tableau()) 
