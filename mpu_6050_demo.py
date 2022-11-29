import utime
from machine import SoftI2C, Pin
from sensors.mpu_6050 import *
from sensors.micropython_i2c import MICROPYTHON_I2C

i2c = SoftI2C(scl=Pin(21), sda=Pin(20))
if __name__ == "__main__":
    sensor = MPU6050(driver=MICROPYTHON_I2C(MPU6050_DEFAULT_ADDRESS, i2c))
    sensor.initialize()
    sensor.dmpInitialize()
    utime.sleep_ms(100)
    print("test connection....", sensor.testConnection())

    while True:
        print(sensor.getMotion6())
        utime.sleep_ms(100)
