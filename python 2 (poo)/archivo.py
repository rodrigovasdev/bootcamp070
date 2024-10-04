from io import open

def crear_archivo():
    try:
        archivito = open('datos.csv','x')
        archivito.close()
    except FileExistsError:
        print('El archivo datos.csv ya existe !!')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)

def lectura_archivo():
    try:
        archivo = open('datos.csv', 'r')
        contenido = archivo.read()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__) 

lectura_archivo()

