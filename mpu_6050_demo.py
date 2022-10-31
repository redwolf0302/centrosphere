from machine import SoftI2C, Pin
from sensors.mpu_6050 import *
from sensors.mpu_6050_micropython_i2c import MPU6050_I2C

i2c = SoftI2C(scl=Pin(3), sda=Pin(2))
if __name__ == "__main__":
    sensor = MPU6050(driver=MPU6050_I2C(MPU6050_DEFAULT_ADDRESS, i2c))
    print(sensor.test_connection())
