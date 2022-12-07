import requests

nombre_poke = input("Ingrese nombre de pokemon: ").lower()

def f_poke(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    resp = requests.get(url)
    
    if resp.status_code != 200:
        print("No se encontró el pokemon.")
        exit()
    
    data_poke = resp.json()

    peso_poke = data_poke["weight"]
    
    hab_poke = []
    for hab in data_poke["abilities"]:
        hab_poke.append(hab["ability"]["name"])
    
    stats_poke = {}
    for stat in data_poke["stats"]:
        stats_poke[stat["stat"]["name"]] = stat["base_stat"]
    
    return peso_poke, hab_poke, stats_poke

peso,hab,stats = f_poke(nombre_poke)

print(f'El peso de {nombre_poke.capitalize()} es: {peso}.')
print(f'Las habilidades de {nombre_poke.capitalize()} son: {hab}.')
print(f'Las estadísticas de {nombre_poke.capitalize()} son: {stats}.')