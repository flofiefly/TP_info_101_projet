'''Construction de mots'''

def generer_dico(nf) :
    res = nf.read().splitlines()
    return(res)

def mot_jouable(mot, ll, en_table = {}) :
    #on verifie que mot ne derange pas le tableau
    for k in en_table :
        if (en_table[k] != list(mot)[k]) and(en_table[k] != '') :
            return(False)

    #on verifie que mot peut s'écrire avec les lettre dans le tableau et les jetons
    temp = []
    for i in ll :
        temp.append(i)
    for k in en_table :
        temp.append(en_table[k])
    for i in list(mot) :
        if i in temp :
            temp.remove(i)
        elif ('?' in temp) :
            temp.remove('?')
        else :
            return(False)
    return(True)

def mots_jouables(motsfr, ll, en_table = {}) :
    res = []
    for i in motsfr :
        if mot_jouable(i, ll, en_table) == True :
            res.append(i)
    return(res)

#test de la fonction 'generer_dico'
print('test_1 :')
with open('littre.txt', 'r') as nf :
    dico = generer_dico(nf)
    for i in range(10) :
        print(dico[i])
        
#test de la fonction 'mot_jouable'
print('test_2 :')
mot = 'INFORMATIQUE'
en_table = {0:'I', 3:'O', 11:'E'}
ll = ['?', '?', '?','?', '?', '?','Q', 'R', 'M']
print(mot_jouable(mot, ll, en_table))

ll = ['?', '?', '?','?', '?', '?','Q', 'R']
print(mot_jouable(mot, ll, en_table))

#test de la fonction 'mots_jouable'
print('test_3 :')
ll = ['A', 'A', 'B', 'C', 'A']
print(mots_jouables(dico, ll))
