## Sets ##



my_set = set() # se define un set 
my_other_set = {}

print(type(my_set))
print(type(my_other_set) ) # esto incialmente es un diccionario un dict

my_other_set = {"Rafael","Derek",35 }

print(type(my_other_set)) #ahora ya me dice que es un set 

print(len(my_other_set))
#print(my_other_set[1]) no se puede acceder por indice a los elementos de los sets 

my_other_set.add("Azul")
print(my_other_set) # tambien los sets no tienen un orden al momento de guardar la informacion 

my_other_set.add("Azul") # no lo va aguardar por que no prmite guardar datos repetidos 
print(my_other_set)

print("Derek" in my_other_set) # le preguntalos al set si derek existe dentro de ese set 
print("Dereck" in my_other_set)        

my_other_set.clear() #borra todos los elementos dentro del clear 
print(len(my_other_set) )

