#intento de comparacion de nombres para videos 1
import glob
import os
from win10toast import ToastNotifier
toast = ToastNotifier()

#para el config file
from configparser import ConfigParser
file = 'config.ini'
config = ConfigParser()
config.read(file)

vacio = 0

list_of_files = glob.glob(config['Borrar']['ubicacion']+'/*') # * means all if need specific format then *.csv

try:
    latest_file = max(list_of_files, key=os.path.getctime)
except:
    vacio = 1

if vacio == False:
    # print(latest_file)

    os.remove(latest_file)       #elimina el archivo

    list_of_files = glob.glob(config['Borrar']['ubicacion']+'/*') #volvemos a checar para ver si se borró
    # print(latest_file in list_of_files)                             #imprime la confirmación
    confirmed = latest_file.split("/")                          #divide el directorio dejando solo el archivo

    if latest_file not in list_of_files:                            #si se eliminó
        toast.show_toast(
        "Archivo eliminado",
        "El archivo mas reciente se ha ELIMINADO\n\n"+confirmed[len(confirmed)-1],   #imprime el nombre del archivo y el folder
        duration = 5,
        icon_path = "python.ico",
        threaded = True,
        )

    else:                                                           #no se eleiminó
        toast.show_toast(
        "Archivo EXISTENTE",
        "El archivo mas reciente NO fue eliminado\n\n"+confirmed[len(confirmed)-1],
        duration = 5,
        icon_path = "python.ico",
        threaded = True,
        )
elif vacio == 1:
    toast.show_toast(
        "El folder está vacío o no existe",
        "Parece que el folder está vacío y no hay nada que borrar o no existe\n\n"+config['Borrar']['ubicacion']+'/',
        duration = 7,
        icon_path = "python.ico",
        threaded = True,
        )