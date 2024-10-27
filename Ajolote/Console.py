def imprime(mensaje):
    print(mensaje, flush=True)  # flush=True forza la impresión inmediata
    
def entrada(prompt=''):
    # Mostrar el mensaje de entrada
    print(prompt, end=' ', flush=True)
    # Leer la entrada del usuario
    user_input = input()
    # Retornar la entrada del usuario
    return user_input

class CambiarDato:
    def __init__(self, var, tipo_dato):
        self.var = var
        self.tipo_dato = tipo_dato  # El tipo que queremos convertir, como int, float, etc.
        
    def procesar(self):
        # Tipo original de la variable
        tipo_var = type(self.var)
        
        # Transformación a diferentes tipos
        if self.tipo_dato == str:
            return str(self.var)  # Convertir a string
        
        elif self.tipo_dato == list:
            if tipo_var == str:
                return list(self.var)  # Convertir string a lista de caracteres
            else:
                return [self.var]  # Convertir a lista con un solo elemento
        
        elif self.tipo_dato == int:
            try:
                return int(self.var)  # Intentar convertir a entero
            except ValueError:
                return "No se puede convertir a int"
        
        elif self.tipo_dato == float:
            try:
                return float(self.var)  # Intentar convertir a float
            except ValueError:
                return "No se puede convertir a float"
        
        elif self.tipo_dato == bool:
            return bool(self.var)  # Convertir a booleano
        
        else:
            return "False"  # Si el tipo no es compatible


#Para evaluar operaciones aritmeticas independientemente del tipo de dato (integer, float o string)
def __eval__(text):
    c = eval(text)
    return c

#Para añadir un elemento a una lista en especifico
def añadir(element, lista = list):
    lista.append(element)
    
#para sumar todos los elemntos de una lista
def sumar(number=float):
    x = sum(number)
    return x

#para encontrar el numero minimo de una lista
def minimo(number=float):
    x = min(number)
    return x

#Para eliminar elementos de un lista
def eliminar(element, lista=list):
    lista.remove(element)
    
#para remover datos de un string
def quitarpor(old_str, new_str, text=str()):
    text.replace(old_str, new_str)
    
class const():
    def __init__(self, variable):
        self.variable = variable
      
#Para crear un secuencia  
def sec(var, limit):
    print(var)
    for i in range(limit):
        print(var + 1)
        var += 1
        if limit == var:
            break

#retorna un numero a base de un caracter 
def char(caracter):    
    return chr(caracter)

#retorna un caracter a base de un numero
def num_car(caracter):
    return ord(caracter)

#retorna un mensaje encriptado
def encriptar(text):
    lista_empty = []
    for i in text:
        x = ord(i)
        lista_empty.append(x)

    lista_empty2 = []
    for y in lista_empty:
        a = y - 3 + 5 - 7  #Algoritmo de codificacion;
        z = chr(a)
        lista_empty2.append(z)
    
    texto_encriptado = ' '.join(lista_empty2)
    texto_encriptado = texto_encriptado.replace(" ", "")
    return texto_encriptado
        
#retorna el mensaje desencriptado a base de la funcion encript
def desencriptar(text):
    lista_empty = []
    for i in text:
        x = ord(i)
        lista_empty.append(x)

    lista_empty2 = []
    for y in lista_empty:
        a = y + 3 - 5 + 7  #Algoritmo de decodificacion
        z = chr(a)
        lista_empty2.append(z)
    
    texto_encriptado = ' '.join(lista_empty2)
    texto_encriptado = texto_encriptado.replace(" ", "")
    return texto_encriptado


class const:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, nuevo_valor):
        raise AttributeError("No puedes cambiar el valor de una constante.")
    

class eleccion():
    def __init__(self, lista=list()):
        self.lista = lista
        import random
        a = random.choice(self.lista)
        return a
    
class imaginario():
    value = 'i'
        
def __max__(num):
    x = max(num)
    return x

def escribir_file(file, messaje):
    x = open(file, 'a')
    x.write(messaje)
    x.close()
    
def leer_archivo(file):
    x = open(file, 'r')
    c = x.read()
    print(c)
    
def crear_archivo(namefile, cont):
    x = open(namefile)
    x.write(cont)
    
