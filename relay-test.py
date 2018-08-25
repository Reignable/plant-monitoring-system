import gpiozero
from time import sleep

relay = gpiozero.DigitalOutputDevice(4, active_high=False)

while True:
    relay.on()
    print('on')
    sleep(2)
    relay.off()
    print('off')
    sleep(5)

