import gpiozero
import warnings
from time import sleep

warnings.filterwarnings('ignore')
sensor = gpiozero.MCP3008(channel=0)
sensor_power = gpiozero.DigitalOutputDevice(4)

while True:
    sensor_power.on()
    sleep(0.02)
    print(sensor.value)
    sensor_power.off()
    sleep(10)
