planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}


moons = planet_moons.values()

planets = len(planet_moons.keys())

print(planet_moons.values)

lunas = []
for i in planet_moons.values():
   lunas  += [i]
print(f"Hay {sum(lunas)} en el sistema solar")