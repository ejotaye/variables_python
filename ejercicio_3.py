# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

nombre_completo = nombre +' '+ apellido

print('nombre completo:', nombre_completo)

# Almacenar su nombre completo en una variable
# nombre_completo = .....



# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras = nombre + apellido
cantidad_letras_len = len(cantidad_letras)
print('cantidad de letras que posee su nombre completo es', cantidad_letras_len)