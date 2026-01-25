#Variables 

my_string_variable = "My String variable" #forma correcta de nombrear variables o todo en minuscula o todo minucula con "_"
print(my_string_variable)

my_int_variable = 4
print(my_int_variable)

my_bool_variable = True #Python no compila si no que interpreta el tipo de dato que le estamos dando a la variable
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable) #pasmos de teer ese entero 4 a un string o texto que imprimira 4 
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) # con type comprobamos el typo de dato y ahora ese variable no se puede usar para cuentas matematicas ya que es solo un texto 

#Concatenacion de variables en un print 
#Concatenacion: unir dos o mas cadenas de info en una sola liena nueva 
print(my_string_variable, ",",my_int_variable,",",my_bool_variable,",","hola mundo")
print("Este es el valor de: " , my_bool_variable)

#Funciones del sistema 
print(len(my_string_variable)) #cuenta la cantidad de carateres de una varaible incuido espacios en blanco la funcion len

#Variables en una sola linea 
name , surname,alias,age = "Rafael","Diaz","Derek",19 #Se pueden llenar varias variables en una sola linea 
print("Me llamo: ",name,surname,"Mi edad es:",age,"Mi alias es: ",alias) 

#Inputs
"""
first_name = input("Whats your name: ") #Para pedir info en la terminal se hace con input 
age = input("How old are you?")

"""
print(name)
print(age)

#Cambio de tipo de dato 
#python puede cambiar el valor de tipo de dato de forma automatica 
name = 123
age = "Derek"

print(name)
print(age)

#Podemos indicar que esta variable la trabajaremos ocmo un String aunque si le pasas un int python le cambia el tipo a int 
addres: str = "Mi direccion" #Es mas como ayuda visual 
#Python es debilmente tipado 








