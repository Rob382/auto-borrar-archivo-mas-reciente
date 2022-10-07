from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())            #imprime lista de las secciones que tiene mi config.ini
print(config['Borrar'])             #lo mismo de arriba pero como objeto
print(list(config['Borrar']))       #imprime una lista de las cosas que tiene adentro la seccion

print(config['Borrar']['ubicacion'])    #imprime el elemento seleccionado que esta dentro de la seccion