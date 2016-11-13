#!/usr/bin/env python

import obtenerNum

print("Jugando a adivinar un número secreto, ¿preparado?");
input();
numSecreto = 0;

numSecreto = input("Dame un número ");
numSecreto = obtenerNum.obtenerNumValido(numSecreto);
print("Tu numero secreto es valido, ¡a jugar!");

numPrueba = 0;
obtenerNum.adivinarNum(numSecreto);
print("Fin del programa");
input();
