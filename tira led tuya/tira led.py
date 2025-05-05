import tinytuya
import time

def negro():
    device.set_colour(0,0,0)

def rojo():
    negro()  
    device.set_colour(255,0,0)

def verde():
    negro()
    device.set_colour(0,255,0)

def azul():
    negro()
    device.set_colour(0,0,255)

def blanco():
    negro()
    device.set_colour(255,255,255)

device = tinytuya.BulbDevice(
    dev_id="eb8ede9d76e23e3c160wp2",   # Device ID
    address="192.168.0.36",           # IP del dispositivo
    local_key="f+.z1#WH;aIZ>Zw?",    # Local Key
    version=3.5
)
device.set_socketPersistent(True) 
#print(device.status())       # Ver estado actual
device.set_mode('colour')

device.set_brightness_percentage(10)
while True:
    device.turn_on()
    rojo()
    time.sleep(2)
    verde()
    time.sleep(2)
    azul()
    time.sleep(2)
    blanco()
    time.sleep(2)
    negro()
    device.turn_off()