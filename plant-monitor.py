import gpiozero
import warnings
from time import sleep

warnings.filterwarnings('ignore')
moisture_sensor = gpiozero.MCP3008(channel=0)
sensor_power = gpiozero.DigitalOutputDevice(5)
water_pump = gpiozero.DigitalOutputDevice(4, active_high=False)

MOISTURE_THRESHOLD_LOW = 30.00
MOISTURE_THRESHOLD_HIGH = 80.00
SENSOR_DRY = 0.0004885197850512668
SENSOR_WET = 0.86


def take_moisture_measurement():
    sensor_power.on()
    sleep(0.02)
    value = moisture_sensor.value
    sensor_power.off()
    return value * 100


if __name__ == '__main__':
    while True:
        # Take sensor measurement
        measurement = take_moisture_measurement()
        # Compare against threshold
        if measurement < MOISTURE_THRESHOLD_LOW:
            # if value is lower
            while take_moisture_measurement() < MOISTURE_THRESHOLD_HIGH:
                # Turn pump on
                water_pump.on()
                # Wait for water to get to plant
                sleep(1)
                # Turn pump off
                water_pump.off()
                # Wait for permeation time
                sleep(10)
            pass
        sleep(300)
