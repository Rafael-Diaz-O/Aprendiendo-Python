 ## For ##
 
 # el for es como un recorredor: toma una lista de cosas y pasa por cada una, de principio a fin.
 
 # for variable in secuencia:  la secuencia es lo que quiero recorrer 
 
frutas = ["Manzana" , "Pera" , "Bannana", "Cereza"]

for fruta in frutas:
    print("Esta es una " + fruta)

colores = list()

colores = ["Azul" , "Verde " , "Rojo" , "Blanco"]

for color in colores:
    print(f"Pintado de {color}")
    
 
#imprimir numeros 

for i in range(10): # range es una clase 
    print(i)

for i in range(0,10,2): # el range tiene 3 opciones (inicio, final, condicion) en ese caso la consicion que colocamos es que fuera de dos en dos
    print(i)
    
# el range solo funciona para numeros enteros 

#imprime el valor y el indice en el que se encuentra con el metodo enumerate 

marcas_autos = ["Lamborgini","corvet","camaro", "ford"]
for indice, nombre  in enumerate(marcas_autos):# se hace un desmpaquetado y se alamcena en las dos variables ya que enumerate entrega dos valores 
    print(f"{indice}: {nombre}") # muestra el inidice y lo que hay guardado en el 
    
    
