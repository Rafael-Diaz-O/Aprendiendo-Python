 ##Tuples ##
 
"""Una tupla es una estructura de datos en Python que 
almacena una colección ordenada e inmutable de elementos. """

#con inmutable se refiere a que no podra cambiar la info que sele coloque al inicio 
 
my_tuple = tuple()
my_other_turple = ()

my_tuple = (19,1.76, "Rafael" , "Derek")
my_other_turple = (35,60,30) 

print(my_tuple)
print(type(my_tuple))

print(my_tuple [0])
print(my_tuple [-1])

print(my_tuple.count("Derek")) # cuenta la cantidad de elementos Derek que hay en la tupla 
print(my_tuple.index("Rafael") ) # muestra el indice o posicion  del obejecto que tiene la lista 
print(my_tuple)

#my_tuple[1] = 1.80 esto no se puede hacer en las tuplas ya que no se pueden cambiar los daots de la tupla 

print(my_tuple + my_other_turple) # se pueden sumar las tuplas 

my_sum_tuple = my_tuple + my_other_turple # esta seria una nueva tupla que es la suma de las otras dos tuplas 
print(my_sum_tuple)

print(my_sum_tuple [3:6]) # imprime los datos que esten entre la posicion 3 y la 6 

my_tuple = list(my_tuple) # paso de tupla a lista para agregar datos 

# lo mejor es que sea una tupla de inicio a fin 

print(my_tuple) 
print(type(my_tuple))

my_tuple[2] = "Linux"
my_tuple.insert(1,91)

print(my_tuple)
my_tuple = tuple(my_tuple) # paso de lista a una tupla de nuevo 
print(type(my_tuple))

del my_tuple # su funcion es eleminar la informacion que exista dentro de cualquier variable sea esta una tupla o no
print(type(my_tuple) ) # como borra la info python no podra interpretar o definir el tipo de dato que es my_tuple 



