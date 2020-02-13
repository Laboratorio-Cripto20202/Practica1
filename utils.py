import random

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#Lista con el alfabeto definido
ALPHABET = [char for char in alphabet]  

class CryptographyException(Exception):
    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

#Nos dice si nos numeros son primos relativos
def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)

def get_key_affine(n):
	"""
	Nos regresa un valor para formar la llave de un
	cifrado afin. Es decir, k y n seran primos relativos
    Parámetro:
	    n -- la longitud del alfabeto
	"""
	k = random.randint(0,25)
	temp = not prime_relative(k, n)

	while(temp):
		k = random.randint(0,25)
		if(prime_relative(k, n)):
			temp = False

	return k

def inverse(a, n):
    """
    Encuentra el inverso multiplicativo del numero dado. Esto 
    claro, tomando en cuenta que trabajamos con modulo n. 
    Parámetro:
        a -- el numero al cual se le quiere encontrar el
            inverso multiplicativo.
        n -- el tamanio del alfabeto

    Este algoritmo esta basado en un pseudocodigo de wikipedia:
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    
    t, newT = 0, 1
    r, newR = n, a

    while (newR != 0):
        q = r // newR
        t, newT = newT, t - q * newT 
        r, newR = newR, r - q * newR

    if (r != 1): 
        return None #No tiene inverso multiplicativo
    if (t < 0):
        t = t + n

    return t