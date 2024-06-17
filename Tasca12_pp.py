import T12_Ex1 
import T12_Ex2
import T12_Ex3 
import T12_Ex4 
import T12_Ex5 
import T12_Ex6 
def menu_principal():
    op = 0
    while op<1 or op>7:
        print("""
        Menú Principal
            1.Llistes i numeros aleatoris
            2.Fitxers
            3.Joc
            4.Ojectes, Classes...
            5.Scrapping
            6.Web
            7.Exit
        """)
        op = int(input("Introdueix una opció: "))
        if op<1 or op>7:
            print("Error")
        else:
            return op

#PP
op = 0
while op!=7:
    op = menu_principal()
    match op:
        case 1:
            T12_Ex1.pex1()
        case 2:
            T12_Ex2.pex2()
        case 3:
            T12_Ex3.pex3()
        case 4:
            T12_Ex4.pex4()
        case 5:
            T12_Ex5.pex5()
        case 6:
            T12_Ex6.pex6()
        case 7:
            op = -1
            print("Has sortit del menú")
        case other:
            print("Opcio no valida")
