# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:49:01 2022

@author: Sender Hodik, Tal Levinzon
"""


import functions as func

def door_encryption(ptext, key):
    res = ''
    i = 0
    odd = 0
    A = func.createKey2DMatrix(key)
    print("text is:", ptext)
    print("Key matrix is:\n", A)
    if func.checkIfAdmissible(A) == False:
       print("Key not admissible!\n")
       return False
    print("Key is admissible!\n")
    if(len(ptext) % 2 == 1):
        ptext += 'a'
        odd = 1
    while(i < len(ptext)):
        # take each iteration 2 letters
        X0 = [func.letterToInt(ptext[i]), func.letterToInt(ptext[i+1])]
        resMatrix = func.calculateMatrixForEncrypt(X0, A)
        for number in func.np.nditer(resMatrix):
            res += str(func.intToLetter(number))
        i += 2
    if odd == 1:
        return res[:len(res) - 1]
    return res    



    
    
    
