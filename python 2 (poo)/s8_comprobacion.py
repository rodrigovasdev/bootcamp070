def crear_archivo():
    try:
        archivo = open('informacion.dat','x')
        archivo.close()
    except FileExistsError:
        print('El archivo ya existe!')

def lectura_archivo():
    try:
        archivo = open('informacion.dat','r')
        contenido = archivo.read()
        print(contenido)
        archivo.close()
        
    except FileNotFoundError:
        print('No se encontro el archivo, se esta creando uno....')
        crear_archivo()
    except:
        print('Se a generado un error')

def escritura_archivo():
    try:
        archivo = open('informacion.dat','a')
        archivo.write("\nEste en una nueva línea en el archivo\n")
        archivo.write("agregando la segunda línea del archivo\n")
        archivo.write("finalizando la linea agregada\n")
        archivo.close()
        
    except FileNotFoundError:
        print('No se encontro el archivo, se esta creando uno....')
        crear_archivo()
    except:
        print('Se a generado un error')

def remplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        archivo = open('informacion.dat', 'r')
        remplazo = ""
        for linea in archivo:
            linea = linea.strip()
            cambios = linea.replace(texto_viejo, texto_nuevo)
            remplazo = remplazo + cambios + "\n"
        archivo.close()

        archivo_remplazo = open('informacion.dat', 'w')       
        archivo_remplazo.write(remplazo)
        archivo_remplazo.close()

    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)
    finally:
        print("Se ha remplazado satisfactoriamente")

def eliminar_datos_archivo():
    try:
        archivo = open('informacion.dat', 'w')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)
    finally:
        print("Se ha eliminado todos los datos del archivo exitosamente")




#Llamar funciones segun corresponda!






