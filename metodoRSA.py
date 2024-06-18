import sympy

def generar_claves(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = sympy.mod_inverse(e, phi)
    return ((e, n), (d, n))

def cifrar(clave_publica, mensaje, alfabeto):
    clave, n = clave_publica
    return [pow(alfabeto.index(char), clave, n) for char in mensaje]

def descifrar(clave_privada, mensaje_cifrado, alfabeto):
    clave, n = clave_privada
    return ''.join([alfabeto[pow(char, clave, n)] for char in mensaje_cifrado])

def encontrar_coprimos(phi):
    return [x for x in range(2, phi) if sympy.gcd(x, phi) == 1]

alfabeto = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) != 'ñ'])

p = int(input("Ingresa un número primo p: "))
q = int(input("Ingresa un número primo q: "))

if not (sympy.isprime(p) and sympy.isprime(q)):
    raise ValueError("Ambos números deben ser primos.")

n = p * q
phi = (p - 1) * (q - 1)

valores_posibles_e = encontrar_coprimos(phi)
print("Valores posibles para e son:", valores_posibles_e)

e = int(input("Elige un valor para e de la lista anterior: "))

if e not in valores_posibles_e:
    raise ValueError("El valor elegido para e no es válido.")

clave_publica, clave_privada = generar_claves(p, q, e)
print("Clave pública:", clave_publica)
print("Clave privada:", clave_privada)

mensaje = input("Ingresa un mensaje para cifrar: ").lower()

if not all(char in alfabeto for char in mensaje):
    raise ValueError("El mensaje debe contener solo letras del alfabeto sin 'ñ'.")

mensaje_cifrado = cifrar(clave_publica, mensaje, alfabeto)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar(clave_privada, mensaje_cifrado, alfabeto)
print("Mensaje descifrado:", mensaje_descifrado)
