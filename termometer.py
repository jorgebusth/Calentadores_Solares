# se abren las bibliotecas necesarias para los dispositivos
from gpiozero import MCP3008
from time import sleep

#inicia el método añadir archivo
def añadir_archivo(a,b,c):
    f = open("registro.dat",'a')
    f.write('{} {} {}'.format(a,b,c))
    f.write('\n')
    f.write(str(a))
    f.write(' ')
    f.write(str(b))
    f.write(' ')
    f.write(str(c))
    f.close()


# Ajusta el número del canal y el chip SPI selecciona el dispositivo. / Set up channel number and SPI chip select device
ambiente = MCP3008(channel=0)
salida_colector = MCP3008(channel = 1)
salida_torre = MCP3008(channel = 2)
while True:
    # Covierte el voltaje analógico a digital y hace la conversión a celcius / Converts ACD voltage to temperature in Celsius
    a = round((ambiente.value * 3.3) * 100, 2)
    b = round((salida_colector.value * 3.3) * 100, 2)
    c = round((salida_torre.value * 3.3) * 100, 2)

    # se guarda en el archivo .dat
    añadir_archivo(a,b,c)


    # Muestra en pantalla los valores obtenidos / Print both temperatures
    print('{} {} {}'.format(a, b, c))

    # Espera 60 segundos para la siguiente lectura. / Wait 60 seconds for the next read
    sleep(60)  
