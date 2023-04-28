import cv2
import RPi.GPIO as GPIO
import time

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Inicializar el clasificador de vehículos
car_classifier = cv2.CascadeClassifier('cars.xml')

# Configurar los pines del semáforo
GREEN_LED = 17
YELLOW_LED = 27
RED_LED = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Función para cambiar el estado del semáforo
def change_lights(color, duration):
    GPIO.output(GREEN_LED, False)
    GPIO.output(YELLOW_LED, False)
    GPIO.output(RED_LED, False)
    GPIO.output(color, True)
    time.sleep(duration)

while True:
    # Capturar un frame de la cámara
    ret, frame = cap.read()

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar vehículos en el frame
    cars = car_classifier.detectMultiScale(gray, 1.1, 3)

    # Si se detecta algún vehículo, cambiar el semáforo a rojo
    if len(cars) > 0:
        change_lights(RED_LED, 5)
    # Si no se detecta ningún vehículo, cambiar el semáforo a verde
    else:
        change_lights(GREEN_LED, 5)

# Liberar la cámara y limpiar los pines del semáforo
cap.release()
GPIO.cleanup()

print('esta rico verdad')