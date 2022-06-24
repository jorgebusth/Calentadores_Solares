# se abren las bibliotecas necesarias para los dispositivos
from gpiozero import MCP3008
from time import sleep
import sys
import datetime
from datetime import date

#inicia el método añadir archivo
def añadir_dato(i,a,b,c):
    
    f = open("registro.dat",'a')
    f.write('\n')
    f.write('{} {} {} {}'.format(i,a,b,c))
    f.close()
    
def añadir_fecha():
    f =open("registro.dat",'a')
    f.write('%\n')
    f.write('%\n')
    f.write('%{} {}'.format(date.today(),datetime.datetime.now().time()))	# Asigno la fecha y hora
    f.write('%\n')
    f.close()

def añadir_encabezado():
    f = open("registro.dat",'a')
    f.write('indice ambiente colector torre')
    f.close()

# inicia funci{on principal
añadir_fecha()
añadir_encabezado()
# Ajusta el número del canal y el chip SPI selecciona el dispositivo. / Set up channel number and SPI chip select device
ambiente = MCP3008(channel=0)
salida_colector = MCP3008(channel = 1)
salida_torre = MCP3008(channel = 2)
i=0
while (i < 300):
    # Covierte el voltaje analógico a digital y hace la conversión a celcius / Converts ACD voltage to temperature in Celsius
    a = round((ambiente.value * 3.3) * 100, 2)
    b = round((salida_colector.value * 3.3) * 100, 2)
    c = round((salida_torre.value * 3.3) * 100, 2)

    # se guarda en el archivo .dat
    añadir_dato(i,a,b,c)
    i+=1


    # Muestra en pantalla los valores obtenidos / Print both temperatures
    print('{} {} {} {}'.format(i,a, b, c))

    # Espera 60 segundos para la siguiente lectura. / Wait 60 seconds for the next read
    sleep(60)

añadir_fecha()
sys.exit("Se han registrado 300 minutos. Los ajos deben estar listos. Fin del programa.")
