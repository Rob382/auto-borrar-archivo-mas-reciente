from configparser import ConfigParser
from tkinter.filedialog import askdirectory

from win10toast import ToastNotifier
toast = ToastNotifier()

file = 'config.ini'
config = ConfigParser()
config.read(file)

#ruta vieja C:/Users/miyav/videos/prueba-wdog
# path = askdirectory()
path = '{}'.format(askdirectory(title='Seleccionar carpeta',initialdir=r'C:/Users/miyav/Videos'))

if path == '':
    toast.show_toast(
    "Operación cancelada",
    "El folder a editar NO se modificó\n\nEl folder actual es:\n"+config['Borrar']['ubicacion'],   #imprime dirección del folder
    duration = 7,
    icon_path = "python.ico",
    threaded = True,
    )
else:
    # config.add_section('masnueva')     #
    config.set('Borrar', 'ubicacion', path)
    print(path)
    with open(file, 'w') as config_file:
        config.write(config_file)

    toast.show_toast(
    "Ubicación modificada",
    "Se ha cambiado el folder que será modificado\n\n"+path,   #imprime dirección del folder
    duration = 7,
    icon_path = "python.ico",
    threaded = True,
    )
