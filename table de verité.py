def affichage(liste):
    for i in range(len(liste[0])):
        print('| ',end='')
        for j in range(len(liste)):
            print(str(liste[j][i])+' |',end='')
        print()

def tableV(entier):
    liste=[]
    deuxn=2**entier
    div=2
    nb=0
    boole=False
    for i in range(entier):
        boole=False
        nb=0
        liste.append([])
        alt=deuxn/div
        for j in range(deuxn):
            if boole:
                liste[i].append(0)
                nb-=1
            else:
                liste[i].append(1)
                nb+=1
            if nb==alt:
                boole=True
            elif nb==0:
                boole=False
        div*=2

    return liste


def xOr(entier):
    liste=tableV(entier)
    for i in range(len(liste[0])):
        som=0
        ligne='| '
        for j in range(len(liste)):
            ligne+=str(liste[j][i])+' |'
            som+=liste[j][i]
        if som==1:
            print(ligne+str(1)+' |')
    
def linetostr(liste):
    ligne='| '
    for i in range(len(liste)):
        ligne+=str(liste[i])+' |'
    return ligne
    
def nombrecase(nb,ncase=9,affich=False,FNCbool=False):
    liste=tableV(ncase)
    tab=[]
    for i in range(len(liste[0])):
        tab.append([])
        som=0
        ligne=[]
        for j in range(len(liste)):
            ligne.append(liste[j][i])
            som+=liste[j][i]
        if FNCbool==False:
            if som==nb:
                tab.append(ligne)
                if affich:
                    print(linetostr(ligne))
        else:
            if som!=nb:
                tab.append(ligne)
                if affich:
                    print(linetostr(ligne))
    i=len(tab)-1
    while i!=-1:
        if tab[i]==[]:
            tab.pop(i)
        i-=1
    return tab


def FND(liste):
    n=0
    for i in range(len(liste)):
        var=1
        n+=1
        for j in range(len(liste[i])):
            if liste[i][j]==1:
                print(' '+str(var),end=' ')
            else:
                print(' -'+str(var),end=' ')
            if j!=len(liste[i])-1:
                print(' ',end='')
            var+=1
            print(' 0 ')
    print()
    print(n)

def FNDXOR(nb,ncase=9):
    FND(nombrecase(nb,ncase))

def FNC(liste):
    n=0
    listetxt=''
    for i in range(len(liste)):
        var=1
        n+=1
        for j in range(len(liste[i])):
            if liste[i][j]==1:
                listetxt+=' -'+str(var)+' '
            else:
                listetxt+='  '+str(var)+' '
            var+=1
        listetxt+=' 0\n'
    print("p cnf "+str(len(liste[0]))+" "+str(len(liste))+"\n"+listetxt)

def FNCXOR(nb,ncase=9):
    FNC(nombrecase(nb,ncase,False,True))

def fncPourCase(liste,nCase):
    n=0
    listetxt=''
    for i in range(len(liste)):
        var=1
        n+=1
        for j in range(len(liste[i])):
            if liste[i][j]==1:
                listetxt+=' -'+str(var)+' '
            else:
                listetxt+='  '+str(var)+' '
            var+=1
        listetxt+=' 0\n'
    print("p cnf "+str(len(liste[0]))+" "+str(len(liste))+"\n"+listetxt)
    
