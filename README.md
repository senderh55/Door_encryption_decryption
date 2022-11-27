# door_encryption_decryption
Writing a cipher and decryption as part of an exercise in a cryptology course

The symmetric block cipher Door is given as follow: 
Plane space:		X = {0…25}
Cipher space:	Y = {0…25}
Key space values: 	The key is a mXm matrix A whose elements are integers in Z26.

The Encryption function defined by repeated encryption x1=ER(x0) is given by the following way: 
Initial case - the first encryption R=1 :  x1 = x0 *A%N 
And  for each R>=2 :  xR = (xR-1 *A+ xR-2)%N,.

a plaintext is a string of the  2 <= length <= 20 a key is a string given by a matrix 2X2.
For example: key = "road" = "r, o, a, d" =  17, 14, 0, 3; 

In addition to encryption and decryption, an iterative attack is also included in the implementation.
![image](https://user-images.githubusercontent.com/79198595/204138545-4b0127e7-82fd-403f-9ad7-bd5ee1f0af03.png)
