# Refer to I2Cdev library collection, https://github.com/jrowberg/i2cdevlib/tree/master/RP2040
import ustruct


class MICROPYTHON_I2C:
    def __init__(self, i2c_addr, i2c) -> None:
        assert i2c_addr is not None, "'i2c_addr' must be set"
        assert i2c is not None, "'i2c' must be set"
        self.i2c_addr = i2c_addr
        self.i2c = i2c

    def readBit(self, register, bit_pos, i2c_address=None):
        """
        Read a single bit from an 8-bit device register
        @param register Register register to read from 
        @param bit_pos Bit position to read (0-7)
        @return a single 8-bit value
        """
        data = self.readByte(register, i2c_address=i2c_address)
        bit = data & (1 << bit_pos)
        return bit

    def readBitW(self, register, bit_pos, i2c_address=None):
        """
        Read a single bit from a 16-bit device register
        @param register Register register to read from 
        @param bit_pos Bit position to read (0-15)
        @return a single 16-bit
        """
        data = self.readWord(register, i2c_address=i2c_address)
        bit = data & (1 << bit_pos)
        return bit

    def readBits(self, register, bit_start, bit_length, i2c_address=None):
        """
        Read multiple bits from an 8-bit device register
        """
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        bits = self.readByte(register, i2c_address=i2c_address)
        bits &= mask
        bits >>= (bit_start - bit_length + 1)
        return bits

    def readBitsW(self, register, bit_start, bit_length, i2c_address=None):
        """
        Read multiple bits from a 16-bit device register
        """
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        w = self.readWord(register, i2c_address=i2c_address)
        w &= mask
        w >>= (bit_start - bit_length + 1)
        return w

    def readByte(self, register, i2c_address=None):
        """
        Read single byte from an 8-bit device register
        """
        data = self.readBytes(register, 1, i2c_address=i2c_address)
        return data[0]

    def readBytes(self, register, length, i2c_address=None):
        """
        Read multiple bytes from an 8-bit device register
        """
        addr = i2c_address if i2c_address is not None else self.i2c_addr
        self.i2c.start()
        self.i2c.writeto(addr, bytearray([register]))
        result = self.i2c.readfrom(addr, length)
        self.i2c.stop()
        return result

    def readWord(self, register, i2c_address=None):
        data = self.readWords(register, 1, i2c_address=i2c_address)
        return data[0]

    def readWords(self, register, length, i2c_address=None):
        buffer = self.readBytes(register, length*2, i2c_address=i2c_address)
        unpacked_buffer = ustruct.unpack('>'+('h'*length), buffer)
        return unpacked_buffer

    def writeBit(self, register, bit_pos, data, i2c_address=None):
        b = self.readByte(register, i2c_address=i2c_address)
        b = (b | (1 << bit_pos)) if data != 0 else (b & ~(1 < bit_pos))
        return self.writeByte(register, b, i2c_address=i2c_address)

    def writeBitW(self, register, bit_pos, data, i2c_address=None):
        w = self.readWord(register, i2c_address=i2c_address)
        w = (w | (1 << bit_pos)) if data != 0 else (w & ~(1 << bit_pos))
        self.writeWord(register, w, i2c_address=i2c_address)

    def writeBits(self, register, bit_start, bit_length, data, i2c_address=None):
        b = self.readByte(register, i2c_address=i2c_address)
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        data <<= (bit_start-bit_length+1)
        data &= mask
        b &= ~(mask)
        b |= data
        return self.writeByte(register, b, i2c_address=i2c_address)

    def writeBitsW(self, register, bit_start, bit_length, data, i2c_address=None):
        w = self.readWord(register, i2c_address=i2c_address)
        mask = ((1 << bit_length)-1) << (bit_start-bit_length+1)
        data <<= (bit_start-bit_length+1)
        data &= mask
        w &= ~(mask)
        w |= data
        return self.writeWord(register, w, i2c_address=i2c_address)

    def writeByte(self, register, data, i2c_address=None):
        return self.writeBytes(register, bytearray([data]), i2c_address=i2c_address)

    def writeWord(self, register, data, i2c_address=None):
        return self.writeWords(register, bytearray([data]), i2c_address=i2c_address)

    def writeBytes(self, register, buff, i2c_address=None):
        length = len(buff)
        data_buff = bytearray(length+1)
        data_buff[0] = register
        for i in range(length):
            data_buff[i+1] = buff[i]

        addr = i2c_address if i2c_address is not None else self.i2c_addr
        self.i2c.start()
        ack = self.i2c.writeto(addr, data_buff)
        self.i2c.stop()
        return ack

    def writeWords(self, register, buff, i2c_address=None):
        length = len(buff)
        data_buff = bytearray(length*2 + 1)
        data_buff[0] = register
        j = 1
        for i in range(length):
            data_buff[j] = buff[i] >> 8
            data_buff[j+1] = buff[i]
            j += 1
        addr = i2c_address if i2c_address is not None else self.i2c_addr
        self.i2c.start()
        ack = self.i2c.writeto(addr, data_buff)
        self.i2c.stop()
        return ack
