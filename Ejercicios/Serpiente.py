
import time 

ancho = 14
direccion = 1
largo = 9

for i in range(100): 
    if i % largo == 0:
        direccion += -1
        continue
    espacios = (i * direccion ) % largo 
    print( " " * espacios + ancho * "*")
    time.sleep(0.03)
 
        