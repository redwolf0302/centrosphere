# Refer to I2Cdev library collection, https://github.com/jrowberg/i2cdevlib/tree/master/RP2040
from machine import SoftI2C
from mpu_6050.mpu_6050_base_driver import mpu_6050_base_driver
from mpu_6050 import mpu_6050_reg


class mpu_6050_mp_i2c(mpu_6050_base_driver):
    def __init__(self, sda=None, scl=None, freq=400_000) -> None:
        assert scl is None, "'scl' must be set"
        assert scl is None, "'sda' must be set"
        self.i2c_addr = mpu_6050_reg.MPU6050_DEFAULT_ADDRESS
        self.scl = scl
        self.sda = sda
        self.freq = freq
        self.__init_device()

    def __init_device(self):
        self.i2c = SoftI2C(scl=self.scl, sda=self.sda, freq=self.freq)

    def readBits(self, register, bit_start, bit_length):
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        bits = self.readByte(register)
        bits &= mask
        bits >>= bits
        return bits

    def readByte(self, register):
        self.i2c.start()
        self.i2c.writeto(self.i2c_addr, bytearray([register]))
        result = self.i2c.readfrom(self.i2c_addr, 1)
        self.i2c.stop()
        return result[0]

    def readBytes(self, register, length):
        self.i2c.start()
        self.i2c.writeto(self.i2c_addr, bytearray([register]))
        result = self.i2c.readfrom(self.i2c_addr, length)
        self.i2c.stop()
        return result

    def write(self, register, data):
        return super().writeBytes(register, bytearray([data]))

    def writeBytes(self, register, buff):
        length = len(buff)
        data_buff = bytearray(length+1)
        data_buff[0] = register
        for i in range(length):
            data_buff[i+1] = buff[i]

        self.i2c.start()
        ack = self.i2c.writeto(self.i2c_addr, data_buff)
        self.i2c.stop()
        return ack
