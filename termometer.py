# se abren las bibliotecas necesarias para los dispositivos
from gpiozero import MCP3008
from time import sleep
import sys
import datetime
from datetime import date

#inicia el método añadir archivo
def añadir_dato(a,b,c):
    
    f = open("registro.dat",'a')
    f.write('\n')
    f.write('{} {} {} {}'.format(datetime.datetime.now().time(),a,b,c))
    f.close()
    
def añadir_fecha():
    f =open("registro.dat",'a')
    f.write('\n')
    f.write('\n')
    f.write('{}'.format(date.today()))	# Asigno la fecha a hoy
    f.write('\n')
    f.close()

# inicia funci{on principal
añadir_fecha()
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
    añadir_dato(a,b,c)


    # Muestra en pantalla los valores obtenidos / Print both temperatures
    print('{} {} {}'.format(a, b, c))

    # Espera 60 segundos para la siguiente lectura. / Wait 60 seconds for the next read
    sleep(60)




