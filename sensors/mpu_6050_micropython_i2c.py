# Refer to I2Cdev library collection, https://github.com/jrowberg/i2cdevlib/tree/master/RP2040
class MPU6050_I2C:
    def __init__(self, i2c_addr, i2c) -> None:
        assert i2c_addr is not None, "'i2c_addr' must be set"
        assert i2c is not None, "'i2c' must be set"
        self.i2c_addr = i2c_addr
        self.i2c = i2c

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
