class mpu_6050_base_driver:
    def readBits(self, register, bit_start, bit_length):
        raise NotImplemented("Not Implemented")

    def readByte(self, register):
        raise NotImplemented("Not Implemented")

    def readBytes(self, register, length):
        raise NotImplemented("Not Implemented")

    def write(self, register, data):
        raise NotImplemented("Not Implemented")

    def writeBytes(self, register, buff):
        raise NotImplemented("Not Implemented")
