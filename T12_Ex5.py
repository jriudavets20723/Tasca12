import requests

def pex5():
    for id_pokemon in range(1, 181):# Per tots els pokemons
        url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}/"
        respuesta = requests.get(url) # Obtenir les dades del pokemon de la url

        if respuesta.status_code == 200: # Si la petició ha funcionat correctament
            datos_pokemon = respuesta.json() # Obtenir les dades del pokemon
            nombre_pokemon = datos_pokemon["name"].upper() # Obtenir el nom del pokemon
            tipos_pokemon = [tipo["type"]["name"].upper() for tipo in datos_pokemon["types"]] if datos_pokemon["types"] else ["ninguno"] # Obtenir els tipus del pokemon
            print(f"El Pokémon es diu--> {nombre_pokemon}, y el seu tipus es--> {tipos_pokemon}") # Mostrar les dades del pokemon
        else:
            print(f"No s'han trobat dades del ID: {id_pokemon}") # Mostrar un missatge d'error si la petició no ha funcionat correct

    print("Recopilacio acabada") # Mostrar un missatge per avisar que la recopilació ha acabat

