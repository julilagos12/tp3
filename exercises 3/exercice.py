#!/usr/bin/env python
# -*- coding: utf-8 -*-
def transformer_case(char):
    if char.isupper():
        return char.lower()
    else:
        return char.upper()
    
print(transformer_case("a"))
print(transformer_case("A"))

#passer en majuscule avec ASCII
def transformer_lettre(lettre):
    if "a"<=lettre<="z":
        return (chr(ord(lettre)-32))
    else:
        return (chr(ord(lettre)+32))
print(transformer_lettre("a"))
print(transformer_lettre("A"))


print(int(-3.64))
    