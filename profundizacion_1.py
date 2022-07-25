# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

from __future__ import division


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input('Digite un número:'))
numero_2 = float(input('Digite un número:'))

print('numero 1 ingresado', numero_1)
print('numero 2 ingresado', numero_2)

suma = numero_1 + numero_2

print('El resultado de la suma entre:', numero_1, 'y' ,numero_2, 'es', suma)

resta = numero_1 - numero_2

print('Resultado de la resta entre', numero_1, 'y', numero_2,'es', resta)

multiplicacion = numero_1 * numero_2

print('el resultado de la multiplicacion entre:', numero_1, 'y', numero_2, 'es', multiplicacion)

division = numero_1 / numero_2
print('el resultado de la division entre:', numero_1, 'y', numero_2, 'es', division)

pontenciacion = numero_1 ** numero_2
print('El resultado de la potenciacion entre:',numero_1, 'y', numero_2, 'es', pontenciacion)
