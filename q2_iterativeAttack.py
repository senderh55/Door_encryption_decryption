# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:09:38 2022


"""
import q1_encrypt as q1_en

def iterativeAttack(ctext, key):
    counter = 0
    last = ctext
    TempEncryptedText = q1_en.door_encryption(ctext, key)
    if TempEncryptedText == False:
        return 0, False
    while ctext != TempEncryptedText:
        last = TempEncryptedText
        TempEncryptedText = q1_en.door_encryption(last, key)  
        counter += 1
    return counter, last
        