import main

print("Editor Axolotl ")
print("(c) Todos los derechos reservados.")
while True:
    
    command = (input(">>> "))
    if command.strip().lower() == 'scripts':
        print("Ingresa el archivo a ejecutar")
        file = (input())
        main.sintax(file)
        print("Ejecute el archivo c.py con su ruta en especifico")
        
        
    elif command.strip().lower() == 'salir':
        print("Cerrando Editor")
        break
    
    elif command.strip().lower() == 'ayuda':
        print("scripts: Ejecuta archivos escritos en axolotl \n salir: sales de el administrador")
    else:
        print("Comando no valido")