from gpiozero import Button
import time
from signal import pause
import picamera

mygtukas = Button(2)
with picamera.PiCamera() as camera:
    camera.resolution = (200, 200)
    time.sleep(2)
	
	mygtukas.when_pressed = camera.capture('image.jpg')
