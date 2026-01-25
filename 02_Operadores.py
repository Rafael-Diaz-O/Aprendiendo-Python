## Operadores Aritmeticos ##

print(3+4)
print(4-3)
print(4/3)
print(4 % 2) #Es la opreacion de modulo y muestra el residuo de la divicion 
print(10//3) #Se hace una divisipn donde se aproxime a un numero entero 
print(2**3) #permite calcular un exponente 

print("Hola" + " Python") #Se puede concatenar unir lineas de texto con + o comas 
#No puedes concatenar tipos diferentes de variables 

print("Hola " + str(5) ) # vuelbo ese dato tipo string 

#Python es de tipado dinamico es decir los datos pueden variar con forme pasa el codigo 

print("Hola " * 5) #Hacemos que hola salga 5 veces 
print("Hola "  * (2**3))#primero se hace el 2 a la 3 y se multiplica por 10 

#No permite la multiplicacion de decimales 

int_multiplicacion = 2.5 *2 #Esto no meda un entero meda un flotante de 5.0

print("Hola " * int(int_multiplicacion)) #Para poder hacer la operacion lo paso a entero 

###Operadores Comparativos ###

print(3>4)
print(3<4)
print(4<= 4)
print(3>=4)
print(3 == 4)
print(3 != 4)

print("Pruebas de texto")

print("Hola" > "Python")
print("Hola" < "Python ")
print("Hola" >= "Zola") #lo que se comprueba es el orden alfabetico cual letra es mayor que los dos 
print("Hola " <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

print(len("Holaa") >= len("Zola") ) #cuenta carateres 

##Operadores Logicos ##

print(3 > 4 and "Hola" > "Python") # seria el equivalente en java a  &&
print(3 > 4 or "Hola" > "Python")# seria el equivalente en java a ||
#print(3 > 4 not "Hola" > "Python")#seria el equivalente en java a !=

print(not(3>4)) #El not se usa para negar la informacion basicamente 3 > 4 es = False pero como negamos imprimira True



