creatures1 = ["Phoenix","Trolls","Elves","Centaurs"]
creatures2 = ["Orcs","Dwarves"]

creatures1.append("Vampires")
creatures1.extend(creatures2)
creatures1.insert(6,"Golems")
creatures1.index("Orcs")
creatures1.sort()

print(creatures1)