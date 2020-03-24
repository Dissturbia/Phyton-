#Declarar las siguientes listas:

par = [2, 4, 6, 8]
impar = [1, 3, 5, 7]
resultado = 0

#En los próximos ejercicios debemos saber como acceder a las listas 
#(recordar que los índices comienzan en 0). Las operaciones deben asignarse a la variable resultado para luego imprimirla en pantalla.

#SUMAR (+) El primer elemento de la lista par + el último elemento de la lista impar
#RESTAR (-) El segundo elemento de la lista par - el segundo elemento de la lista impar
#MULTIPLICAR (*) El último elemento de la lista par * el tercer elemento de la lista impar
#DIVIDIR (/) El último elemento de la lista par / el prmer elemento de la lista par
#SUMAR (+) El segundo elemento de la lista impar + el tercer elemento de la lista par + el último elemento de la lista impar

resultado = par [0] +  impar [-1]
print('el resultado es ', resultado)

resultado = par [1] - impar [1]
print('el resultado es ', resultado)

resultado = par [-1] * impar [2]
print('el resultado es ', resultado)

resultado = par [-1] / par [0]
print('el resultado es ', resultado)

resultado = impar [1] + par [2] + impar [-1]
print('el resultado es ', resultado)