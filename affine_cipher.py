import random
from utils import *

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        self.alphabet = alphabet
        n = len(self.alphabet)

        if(A==None):
            self.A = get_key_affine(n)
        else: 
            if(not prime_relative(A,n)):
                raise CryptographyException()
            self.A = A
        if(B==None):
            self.B = get_key_affine(n)
        else:
            if(not prime_relative(B,n) and B!=0):
                raise CryptographyException()
            self.B = B


    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        cipher_msg = ""

        for c in message:
            new_pos = (self.A*ALPHABET.index(c) + self.B) % len(self.alphabet)
            cipher_msg += ALPHABET[new_pos]

        return cipher_msg


    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        modulo = len(self.alphabet)
        decipher_text = ""

        for c in criptotext:
            new_pos = (inverse(self.A,modulo)*(ALPHABET.index(c) - self.B)) % modulo
            decipher_text += ALPHABET[new_pos]

        return decipher_text
