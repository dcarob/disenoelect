import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout
def ConvertVolts(data,places):
  volts = (data * 3.4) / float(1023)
  volts = round(volts,places)
  return volts 
while True:
    volt2 = readadc(5)*5
    volt1 = readadc(6)*5
    corr = readadc(7)
    rad1 = readadc(0)
    rad2 = readadc(1)
    tempp = readadc(2)
    volt22=ConvertVolts(volt2,2)
    volt11=ConvertVolts(volt1,2)
    corrr=ConvertVolts(corr,2)
    rad11=ConvertVolts(rad1,2)
    rad22=ConvertVolts(rad2,2)
    temppp=ConvertVolts(tempp,2)
    temperature = temppp / (10.0 / 1000)
    rad111= 454.5454*rad11+0.018
    rad222= 454.5454*rad22+0.018
    print("Voltage 1: "+str(volt11))
    print("Voltage 2: "+str(volt22))
    print("Current: "+str(corrr))
    print("Rad 1: "+str(rad111))
    print("Rad 2:"+str(rad222))
    print("Temp sensor voltage "+str(temppp))
    print("temperature: "+str(temperature))
    #    print ("%4d/1023 => %5.3f V => %4.1f °C" % (value, volts,
    #        temperature))
    time.sleep(5)
