import random

def gllistaaleatoris(): # Genera una llista de 3 numeros aleatoris entre 1 i 9
    l = []
    for i in range(3): # Fes el bucle 3 vegades
        l.append(random.randint(1, 9)) # Genera un numero aleatori entre 1 i 9
    return l 

def llegir_llista(): 
    l = [] 
    for i in range(3): # Fes el bucle 3 vegades
        l.append(int(input("Introdueix el numero: "))) # Llegeix un numero i l'afegeix a la llista
    return l 

def comparar(l,m):
    a = [0,0,0] # Inicia amb 0 a tots els elements de la llista
    for i in range(3):
        if l[i]==m[i]: # Si coincideixen els elements
            a[i] = 10 # Marca com a acertat el element
    if a[0] == 10 and a[1] == 10 and a[2] == 10: # Si tots els elements coincideixen mostra el missatge d'enhorabona
        print("Enhorabona, has encertat tot") 
        return 0 # Retorna 0 per indicar que s'ha encertat tot
    
    for i in range(3):
        if a[i]==0: # Si no coincideix el element
            if m[i] in l: # Si el element existeix a la llista
                a[i] = 5 # Marca com a encertat el element

    for i in range(3):
        if a[i]==10: # Si coincideix el element
            print("L'element {} es correcte".format(m[i])) 
        elif a[i]==5: # Si no coincideix el element i existeix a la llista
            print("L'element {} existeix, pero no esta en el lloc correcte ".format(m[i]))
        else: # Si no coincideix ni el element ni existeix a la llista
            print("L'element {} no existeix".format(m[i]))

def pex1():
    op  = 1
    l = gllistaaleatoris() # Genera una llista aleatoria
    while op != 0: 
        m = llegir_llista()
        op = comparar(l,m)
