def cipher(message):
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.^^
       
       00110001^00100111
       00010110
    """
    criptotext=""
    for i in message:
        if((ord(i) % 2)==0):
            criptotext+=(chr(ord(i)+1))
        else:
            criptotext+=(chr(ord(i)-1))
    return criptotext
   
             
               
                  

def decipher(criptotext):
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
    message=""
    for i in criptotext:
        if((ord(i) % 2)==0):
            message+=(chr(ord(i)+1))
        else:
            message+=(chr(ord(i)-1))
    return message
