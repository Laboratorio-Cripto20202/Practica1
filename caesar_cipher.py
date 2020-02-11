import random

class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        self.alphabet = alphabet
        if key is None:
            self.key = random.randint(1,len(alphabet))
        else:
            self.key = key


    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        #True : respetamos espacios
        criptotexto = ""

        if flag is None:
            flag = False
        for i in range(0,len(message)):
            if message[i].isspace() and message[i] not in self.alphabet:
                if flag:
                    criptotexto = criptotexto + message[i]
                else:
                    i = i + 1
            else:
                nuevoIndice = self.alphabet.index(message[i]) + self.key
                nuevoIndice = nuevoIndice % len(self.alphabet)
                criptotexto = criptotexto + self.alphabet[nuevoIndice]
        
        return criptotexto


    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        textoLimpio = ""

        if flag is None:
            flag = False
        for i in range(0,len(criptotext)):
            if criptotext[i].isspace() and criptotext[i] not in self.alphabet:
                if flag:
                    textoLimpio = textoLimpio + criptotext[i]
                else:
                    i = i + 1
            else:
                nuevoIndice = self.alphabet.index(criptotext[i]) - self.key
                nuevoIndice = nuevoIndice % len(self.alphabet)
                textoLimpio = textoLimpio + self.alphabet[nuevoIndice]
        
        return textoLimpio
