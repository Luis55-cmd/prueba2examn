#Librerias:
"""
import math
import random
"""
#Modulos:
"Son archivos.py"
"import (nombre del archivo.py)"
"para llamarla: nombre del archivo.nombre de la funcion(parametros)"
import Lambda_function

print(Lambda_function.suma(2, 4))
"Cambiar nombre al archivo"

#Renombramiento con 'as'
import Lambda_function as l

print(l.suma(2, 4))

#También podemos importar únicamente los componentes que nos interesen como mostramos a continuación.

from Lambda_function import impar, suma

print(impar(6))
print(suma(10, 9))

#Podemos importar todo el módulo haciendo uso de *, sin necesidad de usar mimodulo.*.

from Lambda_function import *

print(impar(6))
print(suma(10, 9))
