import utime
import sys
from machine import SoftI2C, Pin
from sensors.mpu_6050 import *
from sensors.micropython_i2c import MICROPYTHON_I2C

i2c = SoftI2C(scl=Pin(21), sda=Pin(20))
if __name__ == "__main__":
    sensor = MPU6050(driver=MICROPYTHON_I2C(MPU6050_DEFAULT_ADDRESS, i2c))
    sensor.initializeV2()
    print("initialize ok")
#     sensor.initialize()
#     sensor.dmpInitialize()
    utime.sleep_ms(100)
    if not sensor.testConnection():
        print("connection fail.")
        sys.exit(1)
    else:
        print("connection ok")

    while True:
        temp = sensor.getTemperature()/340+36.53
        (ax, ay, az, gx, gy, gz) = sensor.getMotion6()
        nax = ax*2.0 / 32768.0
        nay = ay*2.0 / 32768.0
        naz = az*2.0 / 32768.0
        ngx = gx*250.0 / 32768.0
        ngy = gy*250.0 / 32768.0
        ngz = gz*250.0 / 32768.0
#         print("ACCEL: x: %.2f, y: %.2f, z: %.2f, GYRO: x: %.2f, y: %.2f, z: %.2f" % (nax, nay, naz,ngx,ngy,ngz))
#         print("ACCEL: x: %.2f, y: %.2f, z: %.2f" % (nax, nay, naz))
#         print("GYRO: x: %.2f, y: %.2f, z: %.2f" % (ngx,ngy,ngz))
        print("ACCEL: x: %.2f, y: %.2f, z: %.2f"%(nax, nay, naz))
#         print("Temperature: %.2f" % (temp))
        utime.sleep_ms(100)
