#!/usr/bin/env python

def obtenerNumValido(numerito):
    while int(numerito) not in range(0, 101):
        print("Tu numero secreto no está en el rango permitido");
        numSecreto = input("Prueba con otro número ");
    return numerito;

def adivinarNum(numeroAAdivinar):
    numPrueba = 0;
    contador = 0;

    print("Tenemos un número secreto que debes adivinar")
    numPrueba = input("¿Cual es tu numero? ")
    while int(numPrueba) != int(numeroAAdivinar):
            print("Numero incorrecto, ¡inténtalo otra vez!")
            numPrueba = input("Prueba con otro número ");
            contador += 1;
    print("¡Acertaste en " + str(contador) + " intentos!")
