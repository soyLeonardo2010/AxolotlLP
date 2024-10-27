#Interprete de Ajolote | El primer lengujae en español
#(c) Todos los derechos reservados
#RaptorIndustries

#Errores en la Sintaxis de Python
class ErrorDeSintaxis:
    def __init__(self):
        self.message = "Syntax_Error: Al parecer hay un error en la sintaxis"
    
class ErrorVariable:
    def __init__(self):
        self.message = "Var_Error: Ooops, al parecer hay una variable no definida"
    
class ErrorDeAtributo:
    def __init__(self):
        self.message = "Atrib_Error: Un atributo en tu script no existe"
    
class ErrorDeTipado:
    def __init__(self):
        self.message = "Type_Error: Ooops, al parecer hay un error de tipado en algún dato"
    
class ErrorDeNombre:
    def __init__(self):
        self.message = "Name_Error: Ooops, al parecer hay un nombre no definido en el script"
    

# Estructuramos la Sintaxis de nuestro lenguaje
def sintax(file):
    try:
        with open(file, 'r') as disco:
            disco_b = disco.read()
        
        # Realizar reemplazos de sintaxis
        # Identación
        disco_b = disco_b.replace("{", ":")
        disco_b = disco_b.replace("}", "")
        
        # Funciones
        disco_b = disco_b.replace("fn", "def")
        
        # Operadores Booleanos
        disco_b = disco_b.replace("Cierto", "True")
        disco_b = disco_b.replace("Falso", "False")
        disco_b = disco_b.replace("nulo", "None")
        disco_b = disco_b.replace(" y ", "and")
        disco_b = disco_b.replace(" o ", "or")
        disco_b = disco_b.replace(" no ", "not")
        
        # Comentarios 
        disco_b = disco_b.replace("//", "#")
       
        # Importación de archivos y paradigmas de programación
        disco_b = disco_b.replace("importa ", "import ")
        disco_b = disco_b.replace("asincrono ", "async ")
        disco_b = disco_b.replace("clase ", "class ")
        disco_b = disco_b.replace("desde ", "from ")
        disco_b = disco_b.replace("eso", "self")
        
        # Bucles
        disco_b = disco_b.replace("por ", "for ")
        disco_b = disco_b.replace("Mientras ", "while ")
        
        # Condicionales
        disco_b = disco_b.replace("Si ", "if ")
        disco_b = disco_b.replace("viceversa ", "else ")
        disco_b = disco_b.replace("vicsi", "elif ")
        
        # Palabras reservadas
        disco_b = disco_b.replace("trata ", "try ")
        disco_b = disco_b.replace("exepto ", "except ")
        disco_b = disco_b.replace("continua ", "continue ")
        disco_b = disco_b.replace("rompete ", "break ")
        disco_b = disco_b.replace("alias ", "as ")
        disco_b = disco_b.replace("con ", "with ")
        disco_b = disco_b.replace("minus", "lower")
        disco_b = disco_b.replace("up", "upper")
        disco_b = disco_b.replace("mayus", "capitalize")
        
        # Tipos de Datos
        disco_b = disco_b.replace('ent', 'int')
        disco_b = disco_b.replace('flot', 'float')
        disco_b = disco_b.replace('bool', 'bool')
        disco_b = disco_b.replace('lista', 'list')
        
        # Guardar en un archivo de salida
        with open("c.py", 'w') as disco_a:
            disco_a.write(disco_b)
        
    except FileNotFoundError:
        print(f"ArchivoError: [Error 2] al parecer el archivo '{file}' no existe")


# En caso de que haya un error...
def Errors(error_message):
    if 'SyntaxError' in error_message:
        print(ErrorDeSintaxis().message)
        
    elif 'TypeError' in error_message:
        print(ErrorDeTipado().message)
        
    elif 'NameError' in error_message:
        print(ErrorDeNombre().message)
        
    elif 'ValueError' in error_message:
        print(ErrorVariable().message)
        
    elif 'AttributeError' in error_message:
        print(ErrorDeAtributo().message)
    
    else:
        print("Error no identificado:", error_message)