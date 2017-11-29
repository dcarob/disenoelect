import time
import spidev
#import ReadChannel
spi= spidev.SpiDev()
spi.open(0,0)
#readadc=ReadChannel.ReadChannel
def readadc(adcnum):
  if adcnum > 7 or adcnum < 0:
    return -1
  r = spi.xfer2([1, 8 + adcnum << 4, 0])
  adcout = ((r[1] & 3) << 8) + r[2]
  return adcout


while True:
  value= readadc(5)
  volts = (value*3.4)/1024
  temperature = volts/(10.0/1000)
  value2=readadc(6)
  volts2=(value2*3.4*5)/1024
  print("5"+str(volts))
  print("6"+str(volts2)) 
  time.sleep(2) 
  


