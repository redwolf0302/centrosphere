# Refer to I2Cdev library collection, https://github.com/jrowberg/i2cdevlib/tree/master/RP2040
class MICROPYTHON_I2C:
    def __init__(self, i2c_addr, i2c) -> None:
        assert i2c_addr is not None, "'i2c_addr' must be set"
        assert i2c is not None, "'i2c' must be set"
        self.i2c_addr = i2c_addr
        self.i2c = i2c

    def readBit(self, register, bit_pos):
        data = self.readByte(register)
        bit = data & (1 << bit_pos)
        return bit

    def readBits(self, register, bit_start, bit_length):
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        bits = self.readByte(register)
        bits &= mask
        bits >>= (bit_start - bit_length + 1)
        return bits

    def readByte(self, register):
        data = self.readBytes(register, 1)
        return data[0]

    def readBytes(self, register, length):
        self.i2c.start()
        self.i2c.writeto(self.i2c_addr, bytearray([register]))
        result = self.i2c.readfrom(self.i2c_addr, length)
        self.i2c.stop()
        return result

    def writeBit(self, register, bit_pos, data):
        b = self.readByte(register)
        b = ((b | (1 << bit_pos)), (b & ~(1 < bit_pos)))[data != 0]
        return self.writeByte(register, b)

    def writeBits(self, register, bit_start, bit_length, data):
        b = self.readByte(register)
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        data <<= (bit_start-bit_length+1)
        data &= mask
        b &= ~(mask)
        b |= data
        return super().writeByte(register, b)

    def writeByte(self, register, data):
        return self.writeBytes(register, bytearray([data]))

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
