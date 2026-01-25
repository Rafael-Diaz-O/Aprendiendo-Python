## Strings ##

my_String = "Mi String"
my_otherString = "Mi otro String"

print(my_String + " " + my_otherString)

my_new_line_string = "Este es un String \n con salto de linea "
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion "
print(my_tab_string)

my_space_string = "\\t Este es un String impreso \\n con un espaceado" #ahora podra imprimir en consola el \t y el \n
print(my_space_string)

# Formateo 

name,surname, age = "Derek","Diaz" , 19  

#metodos para mostrar info de variables de forma mas sencilla y organizada que en lugar de separar con + y nombre d evariables

print("Mi nombres es {} {} y mi edad es {}".format(name,surname,age)) #pasa tal cual al info de la variable al espacio donde esta el parentesis 
print("Mi nombres es %s %s y mi edad es %d " %(name,surname,age)) #En este hay que tener encuenta el tipo de dato para String es %s y para int %d
# la opcion dos es mas segura por que se asegura que solo funcione con los tipos de variables corretas no le puedes meter a un string donde deberia ir un int 

print(f"Mi nombre es {name} {surname} y mi edad es {age} ") #otra forma eficiente de mostrar info en consola 

# Desempaquetado de carateres 

lenguage = "Python" 
a, b, c,d,e,f = lenguage #Almaceno cada carater en una variable 

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

lenguaje_slice = lenguage [1:3] # cuenta desde cero y muestra las letras yt de la palara Python en consola 
print(lenguaje_slice)

lenguaje_slice = lenguage [1:]
print(lenguaje_slice)

lenguaje_slice = lenguage [0:6:2] # lo de dentro de corchetes funcion asi [incio : fin : instrucion] ejemplo ahi se ira moviendo y mostrando lo de dos posciones empezando desde cero y terminando en la posicion 6 que esta vacia 
print(lenguaje_slice)

lenguaje_slice = lenguage [-2]
print(lenguaje_slice)

# Invertir una palabra 

reversed_lenguage = lenguage[::-1] # invierto la palabra Python 
print(reversed_lenguage)

# Funciones 


print(lenguage.capitalize()) # coloca la primera letra en mayuscula 
print(lenguage.upper())# coloca toda la palabra en mayuscula 
print(lenguage.count("t")) # cuanta la cantidad de t que tiene la palabra 
print(lenguage.isnumeric()) # mira si la cadena de texto es un numero 
print("1".isnumeric()) # comprueba que en efecto tiene un numero que es el uno asi que mostrara en consola True
print(lenguage.lower()) # vuelve todo miuscula 
print(lenguage.upper().isupper()) # isupper es para comprobar si la palabra esta en minuscula o en mayuscula y devolvera True o False 

# Existen mas para descubirirlas leer la documentacion de python 

print(lenguage.startswith("Py")) # comprueba si empeiza con Py la palabra 



