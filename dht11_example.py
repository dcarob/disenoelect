import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=18)

while True:
    result = instance.read()
    if True:
      #  print("Last valid input: " + str(datetime.datetime.now()))
      #  print("Temperature: %d C" % result.temperature)
      #  print("Humidity: %d %%" % result.humidity)
      t = result.temperature
      h= result.humidity
      print("Temperatura:  "+str(t)+"C")
      print("Humedad: "+str(h)+"%")
    time.sleep(1)
