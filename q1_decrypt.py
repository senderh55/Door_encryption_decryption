# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 18:06:58 2022

@author: Sender Hodik, Tal Levinzon
"""

import functions as func

def door_decryption(ctext, key):
    res = ''
    i = 0
    odd = 0
    A = func.createKey2DMatrix(key)
    print("Key matrix is:\n", A)
    if func.checkIfAdmissible(A) == False:
       print("Key not admissible!\n")
       return False
    print("Key is admissible!\n")
    if(len(ctext) % 2 == 1):
        ctext += 'a'
        odd = 1
    while(i < len(ctext)):
        Y0 = [func.letterToInt(ctext[i]), func.letterToInt(ctext[i+1])]
        resMatrix = func.calculateMatrixForDecrypt(Y0, A)
        for number in resMatrix:
            res += str(func.intToLetter(number))
        i += 2
    if odd == 1:
        return res[:len(res) - 1]
    return res



    
    
    
