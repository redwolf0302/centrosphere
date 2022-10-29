# Refer to I2Cdev library collection, https://github.com/jrowberg/i2cdevlib/tree/master/RP2040
import mpu_6050_reg


class mpu_6050:
    def __init__(self, driver=None) -> None:
        assert driver is None, "No found driver class"
        self.driver = driver

    def test_connection(self):
        return self.get_device_id() == 0x34

    def get_device_id(self):
        device_id = self.driver.readBits(
            mpu_6050_reg.MPU6050_RA_WHO_AM_I, mpu_6050_reg.MPU6050_WHO_AM_I_BIT, mpu_6050_reg.MPU6050_WHO_AM_I_LENGTH)
        print("device id: ", device_id)
        return device_id
