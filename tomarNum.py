#!/usr/bin/env python

def obtenerNumValido(minimo, maximo):
    valido = False;
    numero = 0;

    while not valido:
        try:
            numero = input("¡Dame un número! ");
            if int(numero) in range(minimo, maximo):
                valido = True;
            else:
                print("Tu numero no está en el rango permitido...");
        except:
            print("Dato no válido, intentalo otra vez...");
    print("Tu numero es válido, ¡procede!");
    return numero;
