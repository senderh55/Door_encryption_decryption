# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:05:13 2022

@author: Sender Hodik, Tal Levinzon
"""
import q1_encrypt as q1_en
import q1_decrypt as q1_de
import q2_iterativeAttack as q2_it

if __name__ == '__main__':
    print("*****Encryption****")
    msg = input("Enter message:")
    key = input("Enter key (4 letters):")
    res = q1_en.door_encryption(msg, key)
    if res != False:    
        print("encryption with key:", key, "message:", res)
        
    print("\n****Decryption****")    
    msg = input("Enter message:")
    key = input("Enter key (4 letters):")
    res = q1_de.door_decryption(msg, key)
    if res != False:    
        print("decryption with key:", key, "message:", res)    
    
    print("\n****Iterative attack****") 
    msg = input("Enter message:")
    key = input("Enter key (4 letters):")
    counter, plainText = q2_it.iterativeAttack(msg, key)
    if counter != 0:
        print("Iterative attack - Number of attempt:", counter)
        print("PlainText:", plainText, "Ciphertext:", msg, "Key:", key)
        
        