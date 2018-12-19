#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import Tolk
Tolk.load()

def leer(texto, interrumpir=True):
    Tolk.output(texto, interrumpir)

print("en consola")

leer("este mensaje no se leera porque sera interrumpido")
leer("primer mensaje leído será este.", True)
leer("este es un mensaje a continuación", False)