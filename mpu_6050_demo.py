from mpu_6050.micropython import *
from mpu_6050.mpu_6050 import mpu_6050
if __name__ == "__main__":
    sensor = mpu_6050(driver=mpu_6050_mp_i2c())
    # print(sensor.test_connection())
