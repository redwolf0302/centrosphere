import utime
import sys
from machine import SoftI2C, Pin
from sensors.mpu_6050 import *
from sensors.micropython_i2c import MICROPYTHON_I2C
buzzer_pin = Pin(15, Pin.OUT)
i2c = SoftI2C(scl=Pin(21), sda=Pin(20))


def buzz(count, interval=50, duration=100):
    assert count is not None and count > 0, "Buzz Error"
    buzzer_pin.off()
    for i in range(count):
        buzzer_pin.on()
        utime.sleep_ms(duration)
        buzzer_pin.off()
        utime.sleep_ms(interval)


if __name__ == "__main__":
    sensor = MPU6050(driver=MICROPYTHON_I2C(MPU6050_DEFAULT_ADDRESS, i2c))
    sensor.initializeV2()
    # sensor.initialize()
    print("initialize ok")
    buzz(1)
#     sensor.dmpInitialize()
    utime.sleep_ms(100)
    if not sensor.testConnection():
        print("connection fail.")
        sys.exit(1)
    else:
        print("connection ok")

    count = 0
    while True:
        if count % 100 == 0:
            buzz(2, 50, 50)
        temp = sensor.getTemperature()/340+36.53
        (ax, ay, az, gx, gy, gz) = sensor.getMotion6()
        nax = ax*2.0 / 32768.0
        nay = ay*2.0 / 32768.0
        naz = az*2.0 / 32768.0
        ngx = gx*250.0 / 32768.0
        ngy = gy*250.0 / 32768.0
        ngz = gz*250.0 / 32768.0
        # print("ACCEL: x: %.2f, y: %.2f, z: %.2f, GYRO: x: %.2f, y: %.2f, z: %.2f" % (
        #     nax, nay, naz, ngx, ngy, ngz))
        print("ACCEL: x: %.2f, y: %.2f, z: %.2f" % (nax, nay, naz))
        # print("GYRO: x: %.2f, y: %.2f, z: %.2f" % (ngx, ngy, ngz))
        # print("Temperature: %.2f" % (temp))
        utime.sleep_ms(100)
        count += 1
