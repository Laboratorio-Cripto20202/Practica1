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
            self.A = random.randint(0,25)
            temp = not prime_relative(self.A, n)
            while(temp):
                self.A = random.randint(0,25)
                if(prime_relative(self.A, n)):
                    temp = False
        else: 
            self.A = A
        if(B==None):
            self.B = random.randint(0,25)
            temp = not prime_relative(n, self.B)
            while(temp):
                self.B = random.randint(0,25)
                if(prime_relative(n, self.B)):
                    temp = False
        else:
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
