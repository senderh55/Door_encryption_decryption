# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:02:51 2022

@author: Sender Hodik, Tal Levinzon
"""
import math 
import numpy as np
from sympy import Matrix

def letterToInt(letter):
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A')
    return ord(letter) - ord('a')

def intToLetter(number):
    return chr(number + ord('a'));

def createKey2DMatrix(key):
    m = [[letterToInt(key[0]), letterToInt(key[1])], [letterToInt(key[2]),letterToInt(key[3])]]      
    return np.matrix(m) 

def calculateMatrixForEncrypt(X0, A):
     X1 = np.dot(X0,A) % 26
     X2 = (X1 * A + X0) % 26
     X3 = (X2 * A + X1) % 26
     return X3 

def createInverseMatrix(m):
    arr = np.asarray(m).flatten()
    matrix2DArr = [[arr[0],arr[1]], [arr[2], arr[3]]]
    a = Matrix(matrix2DArr)
    return np.array(a.inv_mod(26))


 # X1 = X0 * A
 # X2 = X1 * A + X0 = (X0 * A) * A + X0
 # X3 = X2 * A + X1 = ((X0 * A) * A + X0) * A + X0 * A
 # ((X0 * A^2) + X0) * A + X0 * A
 #  X0 * A^3 + 2X0 * A
 #  X0 (2A + A ^ 3) % N = X3 
 #  D3(X0) = Y0 * (2A + A ^ 3)^-1 % N
def calculateMatrixForDecrypt(Y0, A):
     A3 = np.dot(A,np.dot(A,A)) # A^3
     twoA = np.dot(2,A) # 2A
     matrix = twoA + A3 # A^3 + 2A
     inverseMat = createInverseMatrix(matrix); # (2A + A ^ 3)^-1 
     return np.mod(np.dot(Y0,inverseMat), 26) # Y0 * (2A + A ^ 3)^-1 % N



def checkIfAdmissible(key):
    det = math.floor(np.linalg.det(key)) 
    gcd = computeGCD(det,26)
    if gcd == 1:
        return True
    return False

def computeGCD(a,b):
    if(b==0):
        return a
    else:
        return computeGCD(b,a%b) 

