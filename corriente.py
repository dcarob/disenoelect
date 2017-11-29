import spidev

spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)*5
  return volts
  
while True:
  current = 0
  for i in range (0, 100):  
    a=ReadChannel(2)
    v=ConvertVolts(a,2)
    current=current+ 10.134*v-16.7512

  current=current/100
  print("la corriente es "+str(current))
  print("volt es "+str(a))
