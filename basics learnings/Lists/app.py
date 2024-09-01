"""

names = ["Jone", "Fortunato", "Domingos", "Mateus"]

names[0] = "Bruno"

print(names) # ["Bruno", "Fortunato", "Domingos", "Mateus"]
print(names[0]) # Bruno
print(names[-1]) # Mateus   
# -1 represents the last element in the list

print(names[0:-1]) # ["Bruno", "Fortunato", "Domingos"]

"""

#Lists Méthods

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)

numbers.append(1)
print(numbers)

numbers.remove(1)
print(numbers, len(numbers))

