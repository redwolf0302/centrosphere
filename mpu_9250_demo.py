import utime
import sys
from machine import SoftI2C, Pin
from sensors.mpu_9250 import *
from sensors.micropython_i2c import MICROPYTHON_I2C
i2c = SoftI2C(scl=Pin(19), sda=Pin(18))
if __name__ == "__main__":
    sensor = MPU9250(driver=MICROPYTHON_I2C(MPU9250_DEFAULT_ADDRESS, i2c))
    sensor.initialize()
    print("initialize ok")
    utime.sleep_ms(100)
    if not sensor.testConnection():
        print("connection fail.")
        sys.exit(1)
    else:
        print("connection ok")

    # print(sensor.getXFineGain())
    print(sensor.getMotion9())
