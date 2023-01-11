import utime
import sys
from machine import SoftI2C, Pin
from sensors.mpu_6050 import *
from sensors.micropython_i2c import MICROPYTHON_I2C
import math
i2c = SoftI2C(scl=Pin(21), sda=Pin(20))

RESTRICT_PITCH = False
dt = 4.0/1000
ZERO_OFFSET_COUNT = 1/dt

if __name__ == "__main__":
    sensor = MPU6050(driver=MICROPYTHON_I2C(MPU6050_DEFAULT_ADDRESS, i2c))
    sensor.initializeV2()
    # sensor.initialize()
    # sensor.dmpInitialize()
    print("initialize ok")
    utime.sleep_ms(100)
    if not sensor.testConnection():
        print("connection fail.")
        sys.exit(1)
    else:
        print("connection ok")

    ax_st = sensor.getAccelXSelfTestFactoryTrim()
    ay_st = sensor.getAccelYSelfTestFactoryTrim()
    az_st = sensor.getAccelZSelfTestFactoryTrim()
    print(ax_st, ay_st, az_st)

#     count = 0
#     g_zero_offset = 0
#     gx_offset = 0.0
#     gy_offset = 0.0
#     gz_offset = 0.0

#     # 陀螺仪积分清零
#     while g_zero_offset < ZERO_OFFSET_COUNT:
#         g_zero_offset += 1
#         (ax, ay, az, gx, gy, gz) = sensor.getMotion6()
#         gx_offset += gx*dt
#         gy_offset += gy*dt
#         gz_offset += gz*dt
#         gx -= gx_offset
#         gy -= gy_offset
#         gz -= gz_offset

#     print("Offset: x: %.2f, y: %.2f, z: %.2f" %
#           (gx_offset, gy_offset, gz_offset))
#     igx = 0.0
#     igy = 0.0
#     igz = 0.0
#     while True:
#         temp = sensor.getTemperature()/340+36.53
#         (ax, ay, az, gx, gy, gz) = sensor.getMotion6()
#         nax = ax / 16384.0
#         nay = ay / 16384.0
#         naz = az / 16384.0
#         ngx = (gx-gx_offset) / 131.0
#         ngy = (gy-gy_offset) / 131.0
#         ngz = (gz-gz_offset) / 131.0
#         igx += ngx*dt
#         igy += ngy*dt
#         igz += ngz*dt
#         if igx > 360:
#             igx -= 360
#         if igx < -360:
#             igx += 360

#         if igy > 360:
#             igy -= 360
#         if igy < -360:
#             igy += 360

#         if igz > 360:
#             igz -= 360
#         if igz < -360:
#             igz += 360

#         if RESTRICT_PITCH:
#             roll = math.degrees(math.atan2(ay, az))
#             pitch = math.degrees(math.atan(-ax/math.sqrt(ay*ay+az*az)))
#         else:
#             roll = math.degrees(math.atan(ay/math.sqrt(ax*ax+az*az)))
#             pitch = math.degrees(math.atan2(-ax, az))
#         print("ROLL: %.0f, PITCH: %.0f \n igx: %.0f, igy: %.0f, igz: %.0f" %
#               (roll, pitch, igx, igy, igz))
#         # print("ACCEL: x: %.2f, y: %.2f, z: %.2f, GYRO: x: %.2f, y: %.2f, z: %.2f" % (
#         #     nax, nay, naz, ngx, ngy, ngz))
# #         print("ACCEL: x: %.2f, y: %.2f, z: %.2f" % (nax, nay, naz))
# #        print("GYRO: x: %.2f, y: %.2f, z: %.2f" % (ngx, ngy, ngz))
#         # print("Temperature: %.2f" % (temp))
#         utime.sleep_ms(100)
#         count += 1
