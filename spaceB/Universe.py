'''
google:
In astronomy, the Universe corresponds to the set of all existing matter and energy.
It gathers the stars: planets, comets, stars, galaxies, nebulae, satellites, among others.
It is an immense place and for many, infinite.
'''

class Universe():
    alfa = 0
    omega = 1

class Galaxies(Universe):
    galName = []
    format = []
'''
The Milky Way is a spiral galaxy, of which the Solar System is a part.
Seen from Earth, it appears as a bright and diffuse band that surrounds the entire celestial sphere, cut by molecular clouds that give it an intricate irregular and jagged appearance.
'''

class System(Galaxies):
    sysName = "a"
'''
The Solar System comprises the set constituted by the Sun and all the celestial bodies that are under its gravitational domain.
The central star, the largest component of the system, accounting for more than 99.85% of the total mass, generates its energy through the fusion of hydrogen into helium, two of its main constituents.
The four planets closest to the Sun have in common a solid and rocky crust, which is why they are classified in the group of terrestrial or rocky planets.
Further out, the four gas giants, Jupiter, Saturn, Uranus and Neptune, are the most massive components of the system just after the Sun itself.
Of the five dwarf planets, Ceres is closest to the center of the Solar System, while all the others, Pluto, Haumea, Makemake and Eris, lie beyond the orbit of Neptune.
'''
solar = System()
solar.sysName = "Solar"
solar.galName = "Milk Way"
