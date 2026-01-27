### Listas ###

#Lista: Una forma de agrupar datos 

my_list = list()
my_other_list = []

print(len(my_list)) #saber la cantida de elementos usando el len 

my_list = [35,24,33,26,54]

print(my_list)
print(len(my_list)) #me dice la cantidad de datos que tiene la lista 

my_other_list = [ 19, 1.76,"Rafael", "Derek"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

# print(my_other_list[-5]) es un error por que no existe este elemento en nuestra lista 

print(my_other_list.count("Derek")) # me muesta la cantidad de veces que esta la palabra Derek en la lista 
#count para contar elementos dentro de la propia lista 

age, heigth, name, nickname = my_other_list # la posicion en la que estan las variables sera como se guarde la info de lista 

#para desempaquetar la lista debes tener las vairbles suficientes para la cantidad de datos de la lista 

print(age , heigth, name , nickname)

#El riesgo dle desempaquetado es que si le agregas mas datos a la lista arriba esto te dara fallos en ejecucion por las cantidades de variables 

print(my_list + my_other_list) # se pueden sumar listas lo que tiene dentro una y lo que tiene dentro pues la otra lista y se muestra en la terminal

#Al ser lenguaje dinamico pueden pasar cosas como estas reescribir mi variable y cambiarla de lista a un String 

my_list = "Hola Python"
print(my_list)
print(type(my_list))

#no se pueden creear constantes 

my_other_list.append("Python") #permite añadir elementos al final de la lista 
print(my_other_list)

my_other_list.insert(0,"Hola mundo") # insertamos en primero indicamos posicion luego lo que queremos guardar 
print(my_other_list)

my_other_list.remove("Hola mundo") #para elminar algun valor , aqui le digo que elimine hola mundo 
print(my_other_list)

my_list = [35,24,33,26,54]
print(my_list)


my_list.pop() #quita el ultimo dato de mi lista 
print(my_list)

print(my_list.pop(2)) # elimino el elemento del indice dos y imprimo el elemento borrado , tmabien se puede guardar este elemento en una variables 
print(my_list)

#guardar pop en una variable 

my_list_pop = my_list.pop(2)
print(my_list) 
my_list.append(my_list_pop) # agrego elelemenot que saque con pop(2) al final de la lista 
print(my_list)

del my_list[2] # si solo quiero borrar el elemnto puedo hacerlo con del 
print(my_list)

my_list.clear # borrar una lista 
print(my_list)



