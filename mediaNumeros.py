#!/usr/bin/env python

# Modulos importados
import tomarNum

# Variables
suma = 0;
nNumeros = 0;
media = 0;
numeroIntroducido = 1;

#
print("Calculando media de numeros hasta introducir 0");
while int(numeroIntroducido) != 0:
    numeroIntroducido = tomarNum.obtenerNumValido(0, 100);
    if int(numeroIntroducido) != 0:
        suma += int(numeroIntroducido);
        nNumeros += 1;

print("Suma de numeros finalizada, calculando media...");
media = suma / nNumeros;
print("La media de los " + str(nNumeros) + " numeros introducidos es " + str(media));
input();
