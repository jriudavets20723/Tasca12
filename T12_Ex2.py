class Agenda:
    def __init__(self):
        self.contactes = []

    def afegir_contacte(self, nom, telefon):# Afegir un contacte a l'agenda
        self.contactes.append({"nom": nom, "telefon": telefon}) # Afegim el contacte a la llista
        print(f"Contacte afegit com a {nom}") # Mostram el missatge de confirmacio

    def mostrar_contactes(self): 
        if not self.contactes: # Si la agenda esta buida, mostram un missatge
            print("L'agenda esta buida.")

        else: # Si la agenda no esta buida, mostram els contactes
            print("\n\nContactes:\n")
            for contacte in self.contactes:
                print(f"--> Nom: {contacte['nom']}, Telefon: {contacte['telefon']}")

def menu_agenda():
    print("\n\n   Agenda")
    print("1. Afegir contactes")
    print("2. Veurer contactes")
    print("3. Sortir")

def pex2():
    agenda = Agenda()
    while True:
        menu_agenda()
        opcio = input("Tria una opcio: ")

        if opcio == "1":
            nom = input("Introdueix el nom del contacte: ")
            telefon = input("Introdueix el telèfon del contacte: ")
            agenda.afegir_contacte(nom, telefon)
        elif opcio == "2":
            agenda.mostrar_contactes()
        elif opcio == "3":
            print("Sortint de l'agenda...")
            break # Sortim del bucle while
        else:
            print("Opció no vàlida(1, 2, 3)")
