#!/usr/bin/env python
# -*- coding: utf-8 -*-

#exercises du chapitre 2
#déterminer les nombres premiers compris entre 50 et 100
for number in range(50, 101):
    for i in range(2,number):
        if (number % i) == 0:
            print(number, "n'est pas un nombre premier")
            break
    else:
        print(number, "est un nombre premier")
        


