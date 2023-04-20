import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Configuración de pines
red_pin = 18
yellow_pin = 23
green_pin = 24

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

# Función para encender la luz roja
def red_light_on():
    GPIO.output(red_pin, GPIO.HIGH)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)

# Función para encender la luz amarilla
def yellow_light_on():
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.HIGH)
    GPIO.output(green_pin, GPIO.LOW)

# Función para encender la luz verde
def green_light_on():
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.HIGH)

# Ciclo para el semáforo
while True:
    red_light_on()
    time.sleep(5)
    yellow_light_on()
    time.sleep(2)
    green_light_on()
    time.sleep(5)
    yellow_light_on()
    time.sleep(2)

# Limpiar pines al finalizar
GPIO.cleanup()
