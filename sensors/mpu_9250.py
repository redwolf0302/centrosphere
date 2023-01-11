from micropython import const
from array import array
import utime
import ustruct
# //Magnetometer Registers
MPU9150_RA_MAG_ADDRESS = const(0x0C)
MPU9150_RA_MAG_XOUT_L = const(0x03)
MPU9150_RA_MAG_XOUT_H = const(0x04)
MPU9150_RA_MAG_YOUT_L = const(0x05)
MPU9150_RA_MAG_YOUT_H = const(0x06)
MPU9150_RA_MAG_ZOUT_L = const(0x07)
MPU9150_RA_MAG_ZOUT_H = const(0x08)

# // address pin low (GND), default for InvenSense evaluation board
MPU9250_ADDRESS_AD0_LOW = const(0x68)
MPU9250_ADDRESS_AD0_HIGH = const(0x69)  # // address pin high (VCC)
MPU9250_DEFAULT_ADDRESS = MPU9250_ADDRESS_AD0_LOW

# //[7] PWR_MODE, [6:1]=XG_OFFS_TC, [0] OTP_BNK_VLD
MPU9250_RA_XG_OFFS_TC = const(0x00)
# //[7] PWR_MODE, [6:1] YG_OFFS_TC, [0] OTP_BNK_VLD
MPU9250_RA_YG_OFFS_TC = const(0x01)
# //[7] PWR_MODE, [6:1] ZG_OFFS_TC, [0] OTP_BNK_VLD
MPU9250_RA_ZG_OFFS_TC = const(0x02)
MPU9250_RA_X_FINE_GAIN = const(0x03)  # //[7:0]=X_FINE_GAIN
MPU9250_RA_Y_FINE_GAIN = const(0x04)  # //[7:0] Y_FINE_GAIN
MPU9250_RA_Z_FINE_GAIN = const(0x05)  # //[7:0] Z_FINE_GAIN

MPU9250_RA_XA_OFFS_H = const(0x77)  # //[15:0]=XA_OFFS
MPU9250_RA_XA_OFFS_L_TC = const(0x78)
MPU9250_RA_YA_OFFS_H = const(0x7A)  # //[15:0] YA_OFFS
MPU9250_RA_YA_OFFS_L_TC = const(0x7B)
MPU9250_RA_ZA_OFFS_H = const(0x7D)  # //[15:0] ZA_OFFS
MPU9250_RA_ZA_OFFS_L_TC = const(0x7E)

# //MPU9250_RA_XA_OFFS_H=0x06 # //[15:0]=XA_OFFS
# //MPU9250_RA_XA_OFFS_L_TC=0x07
# //MPU9250_RA_YA_OFFS_H=0x08 # //[15:0] YA_OFFS
# //MPU9250_RA_YA_OFFS_L_TC=0x09
# //MPU9250_RA_ZA_OFFS_H=0x0A # //[15:0] ZA_OFFS
# //MPU9250_RA_ZA_OFFS_L_TC=0x0B

MPU9250_RA_XG_OFFS_USRH = const(0x13)  # //[15:0]=XG_OFFS_USR
MPU9250_RA_XG_OFFS_USRL = const(0x14)
MPU9250_RA_YG_OFFS_USRH = const(0x15)  # //[15:0] YG_OFFS_USR
MPU9250_RA_YG_OFFS_USRL = const(0x16)
MPU9250_RA_ZG_OFFS_USRH = const(0x17)  # //[15:0] ZG_OFFS_USR
MPU9250_RA_ZG_OFFS_USRL = const(0x18)

MPU9250_RA_SMPLRT_DIV = const(0x19)
MPU9250_RA_CONFIG = const(0x1A)
MPU9250_RA_GYRO_CONFIG = const(0x1B)
MPU9250_RA_ACCEL_CONFIG = const(0x1C)
MPU9250_RA_FF_THR = const(0x1D)
MPU9250_RA_FF_DUR = const(0x1E)
MPU9250_RA_MOT_THR = const(0x1F)
MPU9250_RA_MOT_DUR = const(0x20)
MPU9250_RA_ZRMOT_THR = const(0x21)
MPU9250_RA_ZRMOT_DUR = const(0x22)
MPU9250_RA_FIFO_EN = const(0x23)
MPU9250_RA_I2C_MST_CTRL = const(0x24)
MPU9250_RA_I2C_SLV0_ADDR = const(0x25)
MPU9250_RA_I2C_SLV0_REG = const(0x26)
MPU9250_RA_I2C_SLV0_CTRL = const(0x27)
MPU9250_RA_I2C_SLV1_ADDR = const(0x28)
MPU9250_RA_I2C_SLV1_REG = const(0x29)
MPU9250_RA_I2C_SLV1_CTRL = const(0x2A)
MPU9250_RA_I2C_SLV2_ADDR = const(0x2B)
MPU9250_RA_I2C_SLV2_REG = const(0x2C)
MPU9250_RA_I2C_SLV2_CTRL = const(0x2D)
MPU9250_RA_I2C_SLV3_ADDR = const(0x2E)
MPU9250_RA_I2C_SLV3_REG = const(0x2F)
MPU9250_RA_I2C_SLV3_CTRL = const(0x30)
MPU9250_RA_I2C_SLV4_ADDR = const(0x31)
MPU9250_RA_I2C_SLV4_REG = const(0x32)
MPU9250_RA_I2C_SLV4_DO = const(0x33)
MPU9250_RA_I2C_SLV4_CTRL = const(0x34)
MPU9250_RA_I2C_SLV4_DI = const(0x35)
MPU9250_RA_I2C_MST_STATUS = const(0x36)
MPU9250_RA_INT_PIN_CFG = const(0x37)
MPU9250_RA_INT_ENABLE = const(0x38)
MPU9250_RA_DMP_INT_STATUS = const(0x39)
MPU9250_RA_INT_STATUS = const(0x3A)
MPU9250_RA_ACCEL_XOUT_H = const(0x3B)
MPU9250_RA_ACCEL_XOUT_L = const(0x3C)
MPU9250_RA_ACCEL_YOUT_H = const(0x3D)
MPU9250_RA_ACCEL_YOUT_L = const(0x3E)
MPU9250_RA_ACCEL_ZOUT_H = const(0x3F)
MPU9250_RA_ACCEL_ZOUT_L = const(0x40)
MPU9250_RA_TEMP_OUT_H = const(0x41)
MPU9250_RA_TEMP_OUT_L = const(0x42)
MPU9250_RA_GYRO_XOUT_H = const(0x43)
MPU9250_RA_GYRO_XOUT_L = const(0x44)
MPU9250_RA_GYRO_YOUT_H = const(0x45)
MPU9250_RA_GYRO_YOUT_L = const(0x46)
MPU9250_RA_GYRO_ZOUT_H = const(0x47)
MPU9250_RA_GYRO_ZOUT_L = const(0x48)
MPU9250_RA_EXT_SENS_DATA_00 = const(0x49)
MPU9250_RA_EXT_SENS_DATA_01 = const(0x4A)
MPU9250_RA_EXT_SENS_DATA_02 = const(0x4B)
MPU9250_RA_EXT_SENS_DATA_03 = const(0x4C)
MPU9250_RA_EXT_SENS_DATA_04 = const(0x4D)
MPU9250_RA_EXT_SENS_DATA_05 = const(0x4E)
MPU9250_RA_EXT_SENS_DATA_06 = const(0x4F)
MPU9250_RA_EXT_SENS_DATA_07 = const(0x50)
MPU9250_RA_EXT_SENS_DATA_08 = const(0x51)
MPU9250_RA_EXT_SENS_DATA_09 = const(0x52)
MPU9250_RA_EXT_SENS_DATA_10 = const(0x53)
MPU9250_RA_EXT_SENS_DATA_11 = const(0x54)
MPU9250_RA_EXT_SENS_DATA_12 = const(0x55)
MPU9250_RA_EXT_SENS_DATA_13 = const(0x56)
MPU9250_RA_EXT_SENS_DATA_14 = const(0x57)
MPU9250_RA_EXT_SENS_DATA_15 = const(0x58)
MPU9250_RA_EXT_SENS_DATA_16 = const(0x59)
MPU9250_RA_EXT_SENS_DATA_17 = const(0x5A)
MPU9250_RA_EXT_SENS_DATA_18 = const(0x5B)
MPU9250_RA_EXT_SENS_DATA_19 = const(0x5C)
MPU9250_RA_EXT_SENS_DATA_20 = const(0x5D)
MPU9250_RA_EXT_SENS_DATA_21 = const(0x5E)
MPU9250_RA_EXT_SENS_DATA_22 = const(0x5F)
MPU9250_RA_EXT_SENS_DATA_23 = const(0x60)
MPU9250_RA_MOT_DETECT_STATUS = const(0x61)
MPU9250_RA_I2C_SLV0_DO = const(0x63)
MPU9250_RA_I2C_SLV1_DO = const(0x64)
MPU9250_RA_I2C_SLV2_DO = const(0x65)
MPU9250_RA_I2C_SLV3_DO = const(0x66)
MPU9250_RA_I2C_MST_DELAY_CTRL = const(0x67)
MPU9250_RA_SIGNAL_PATH_RESET = const(0x68)
MPU9250_RA_MOT_DETECT_CTRL = const(0x69)
MPU9250_RA_USER_CTRL = const(0x6A)
MPU9250_RA_PWR_MGMT_1 = const(0x6B)
MPU9250_RA_PWR_MGMT_2 = const(0x6C)
MPU9250_RA_BANK_SEL = const(0x6D)
MPU9250_RA_MEM_START_ADDR = const(0x6E)
MPU9250_RA_MEM_R_W = const(0x6F)
MPU9250_RA_DMP_CFG_1 = const(0x70)
MPU9250_RA_DMP_CFG_2 = const(0x71)
MPU9250_RA_FIFO_COUNTH = const(0x72)
MPU9250_RA_FIFO_COUNTL = const(0x73)
MPU9250_RA_FIFO_R_W = const(0x74)
MPU9250_RA_WHO_AM_I = const(0x75)

MPU9250_TC_PWR_MODE_BIT = const(7)
MPU9250_TC_OFFSET_BIT = const(6)
MPU9250_TC_OFFSET_LENGTH = const(6)
MPU9250_TC_OTP_BNK_VLD_BIT = const(0)

MPU9250_VDDIO_LEVEL_VLOGIC = const(0)
MPU9250_VDDIO_LEVEL_VDD = const(1)

MPU9250_CFG_EXT_SYNC_SET_BIT = const(5)
MPU9250_CFG_EXT_SYNC_SET_LENGTH = const(3)
MPU9250_CFG_DLPF_CFG_BIT = const(2)
MPU9250_CFG_DLPF_CFG_LENGTH = const(3)

MPU9250_EXT_SYNC_DISABLED = const(0x0)
MPU9250_EXT_SYNC_TEMP_OUT_L = const(0x1)
MPU9250_EXT_SYNC_GYRO_XOUT_L = const(0x2)
MPU9250_EXT_SYNC_GYRO_YOUT_L = const(0x3)
MPU9250_EXT_SYNC_GYRO_ZOUT_L = const(0x4)
MPU9250_EXT_SYNC_ACCEL_XOUT_L = const(0x5)
MPU9250_EXT_SYNC_ACCEL_YOUT_L = const(0x6)
MPU9250_EXT_SYNC_ACCEL_ZOUT_L = const(0x7)

MPU9250_DLPF_BW_256 = const(0x00)
MPU9250_DLPF_BW_188 = const(0x01)
MPU9250_DLPF_BW_98 = const(0x02)
MPU9250_DLPF_BW_42 = const(0x03)
MPU9250_DLPF_BW_20 = const(0x04)
MPU9250_DLPF_BW_10 = const(0x05)
MPU9250_DLPF_BW_5 = const(0x06)

MPU9250_GCONFIG_FS_SEL_BIT = const(4)
MPU9250_GCONFIG_FS_SEL_LENGTH = const(2)

MPU9250_GYRO_FS_250 = const(0x00)
MPU9250_GYRO_FS_500 = const(0x01)
MPU9250_GYRO_FS_1000 = const(0x02)
MPU9250_GYRO_FS_2000 = const(0x03)

MPU9250_ACONFIG_XA_ST_BIT = const(7)
MPU9250_ACONFIG_YA_ST_BIT = const(6)
MPU9250_ACONFIG_ZA_ST_BIT = const(5)
MPU9250_ACONFIG_AFS_SEL_BIT = const(4)
MPU9250_ACONFIG_AFS_SEL_LENGTH = const(2)
MPU9250_ACONFIG_ACCEL_HPF_BIT = const(2)
MPU9250_ACONFIG_ACCEL_HPF_LENGTH = const(3)

MPU9250_ACCEL_FS_2 = const(0x00)
MPU9250_ACCEL_FS_4 = const(0x01)
MPU9250_ACCEL_FS_8 = const(0x02)
MPU9250_ACCEL_FS_16 = const(0x03)

MPU9250_DHPF_RESET = const(0x00)
MPU9250_DHPF_5 = const(0x01)
MPU9250_DHPF_2P5 = const(0x02)
MPU9250_DHPF_1P25 = const(0x03)
MPU9250_DHPF_0P63 = const(0x04)
MPU9250_DHPF_HOLD = const(0x07)

MPU9250_TEMP_FIFO_EN_BIT = const(7)
MPU9250_XG_FIFO_EN_BIT = const(6)
MPU9250_YG_FIFO_EN_BIT = const(5)
MPU9250_ZG_FIFO_EN_BIT = const(4)
MPU9250_ACCEL_FIFO_EN_BIT = const(3)
MPU9250_SLV2_FIFO_EN_BIT = const(2)
MPU9250_SLV1_FIFO_EN_BIT = const(1)
MPU9250_SLV0_FIFO_EN_BIT = const(0)

MPU9250_MULT_MST_EN_BIT = const(7)
MPU9250_WAIT_FOR_ES_BIT = const(6)
MPU9250_SLV_3_FIFO_EN_BIT = const(5)
MPU9250_I2C_MST_P_NSR_BIT = const(4)
MPU9250_I2C_MST_CLK_BIT = const(3)
MPU9250_I2C_MST_CLK_LENGTH = const(4)

MPU9250_CLOCK_DIV_348 = const(0x0)
MPU9250_CLOCK_DIV_333 = const(0x1)
MPU9250_CLOCK_DIV_320 = const(0x2)
MPU9250_CLOCK_DIV_308 = const(0x3)
MPU9250_CLOCK_DIV_296 = const(0x4)
MPU9250_CLOCK_DIV_286 = const(0x5)
MPU9250_CLOCK_DIV_276 = const(0x6)
MPU9250_CLOCK_DIV_267 = const(0x7)
MPU9250_CLOCK_DIV_258 = const(0x8)
MPU9250_CLOCK_DIV_500 = const(0x9)
MPU9250_CLOCK_DIV_471 = const(0xA)
MPU9250_CLOCK_DIV_444 = const(0xB)
MPU9250_CLOCK_DIV_421 = const(0xC)
MPU9250_CLOCK_DIV_400 = const(0xD)
MPU9250_CLOCK_DIV_381 = const(0xE)
MPU9250_CLOCK_DIV_364 = const(0xF)

MPU9250_I2C_SLV_RW_BIT = const(7)
MPU9250_I2C_SLV_ADDR_BIT = const(6)
MPU9250_I2C_SLV_ADDR_LENGTH = const(7)
MPU9250_I2C_SLV_EN_BIT = const(7)
MPU9250_I2C_SLV_BYTE_SW_BIT = const(6)
MPU9250_I2C_SLV_REG_DIS_BIT = const(5)
MPU9250_I2C_SLV_GRP_BIT = const(4)
MPU9250_I2C_SLV_LEN_BIT = const(3)
MPU9250_I2C_SLV_LEN_LENGTH = const(4)

MPU9250_I2C_SLV4_RW_BIT = const(7)
MPU9250_I2C_SLV4_ADDR_BIT = const(6)
MPU9250_I2C_SLV4_ADDR_LENGTH = const(7)
MPU9250_I2C_SLV4_EN_BIT = const(7)
MPU9250_I2C_SLV4_INT_EN_BIT = const(6)
MPU9250_I2C_SLV4_REG_DIS_BIT = const(5)
MPU9250_I2C_SLV4_MST_DLY_BIT = const(4)
MPU9250_I2C_SLV4_MST_DLY_LENGTH = const(5)

MPU9250_MST_PASS_THROUGH_BIT = const(7)
MPU9250_MST_I2C_SLV4_DONE_BIT = const(6)
MPU9250_MST_I2C_LOST_ARB_BIT = const(5)
MPU9250_MST_I2C_SLV4_NACK_BIT = const(4)
MPU9250_MST_I2C_SLV3_NACK_BIT = const(3)
MPU9250_MST_I2C_SLV2_NACK_BIT = const(2)
MPU9250_MST_I2C_SLV1_NACK_BIT = const(1)
MPU9250_MST_I2C_SLV0_NACK_BIT = const(0)

MPU9250_INTCFG_INT_LEVEL_BIT = const(7)
MPU9250_INTCFG_INT_OPEN_BIT = const(6)
MPU9250_INTCFG_LATCH_INT_EN_BIT = const(5)
MPU9250_INTCFG_INT_RD_CLEAR_BIT = const(4)
MPU9250_INTCFG_FSYNC_INT_LEVEL_BIT = const(3)
MPU9250_INTCFG_FSYNC_INT_EN_BIT = const(2)
MPU9250_INTCFG_I2C_BYPASS_EN_BIT = const(1)
MPU9250_INTCFG_CLKOUT_EN_BIT = const(0)

MPU9250_INTMODE_ACTIVEHIGH = const(0x00)
MPU9250_INTMODE_ACTIVELOW = const(0x01)

MPU9250_INTDRV_PUSHPULL = const(0x00)
MPU9250_INTDRV_OPENDRAIN = const(0x01)

MPU9250_INTLATCH_50USPULSE = const(0x00)
MPU9250_INTLATCH_WAITCLEAR = const(0x01)

MPU9250_INTCLEAR_STATUSREAD = const(0x00)
MPU9250_INTCLEAR_ANYREAD = const(0x01)

MPU9250_INTERRUPT_FF_BIT = const(7)
MPU9250_INTERRUPT_MOT_BIT = const(6)
MPU9250_INTERRUPT_ZMOT_BIT = const(5)
MPU9250_INTERRUPT_FIFO_OFLOW_BIT = const(4)
MPU9250_INTERRUPT_I2C_MST_INT_BIT = const(3)
MPU9250_INTERRUPT_PLL_RDY_INT_BIT = const(2)
MPU9250_INTERRUPT_DMP_INT_BIT = const(1)
MPU9250_INTERRUPT_DATA_RDY_BIT = const(0)

# // TODO: figure out what these actually do
# // UMPL source code is not very obivous
MPU9250_DMPINT_5_BIT = const(5)
MPU9250_DMPINT_4_BIT = const(4)
MPU9250_DMPINT_3_BIT = const(3)
MPU9250_DMPINT_2_BIT = const(2)
MPU9250_DMPINT_1_BIT = const(1)
MPU9250_DMPINT_0_BIT = const(0)

MPU9250_MOTION_MOT_XNEG_BIT = const(7)
MPU9250_MOTION_MOT_XPOS_BIT = const(6)
MPU9250_MOTION_MOT_YNEG_BIT = const(5)
MPU9250_MOTION_MOT_YPOS_BIT = const(4)
MPU9250_MOTION_MOT_ZNEG_BIT = const(3)
MPU9250_MOTION_MOT_ZPOS_BIT = const(2)
MPU9250_MOTION_MOT_ZRMOT_BIT = const(0)

MPU9250_DELAYCTRL_DELAY_ES_SHADOW_BIT = const(7)
MPU9250_DELAYCTRL_I2C_SLV4_DLY_EN_BIT = const(4)
MPU9250_DELAYCTRL_I2C_SLV3_DLY_EN_BIT = const(3)
MPU9250_DELAYCTRL_I2C_SLV2_DLY_EN_BIT = const(2)
MPU9250_DELAYCTRL_I2C_SLV1_DLY_EN_BIT = const(1)
MPU9250_DELAYCTRL_I2C_SLV0_DLY_EN_BIT = const(0)

MPU9250_PATHRESET_GYRO_RESET_BIT = const(2)
MPU9250_PATHRESET_ACCEL_RESET_BIT = const(1)
MPU9250_PATHRESET_TEMP_RESET_BIT = const(0)

MPU9250_DETECT_ACCEL_ON_DELAY_BIT = const(5)
MPU9250_DETECT_ACCEL_ON_DELAY_LENGTH = const(2)
MPU9250_DETECT_FF_COUNT_BIT = const(3)
MPU9250_DETECT_FF_COUNT_LENGTH = const(2)
MPU9250_DETECT_MOT_COUNT_BIT = const(1)
MPU9250_DETECT_MOT_COUNT_LENGTH = const(2)

MPU9250_DETECT_DECREMENT_RESET = const(0x0)
MPU9250_DETECT_DECREMENT_1 = const(0x1)
MPU9250_DETECT_DECREMENT_2 = const(0x2)
MPU9250_DETECT_DECREMENT_4 = const(0x3)

MPU9250_USERCTRL_DMP_EN_BIT = const(7)
MPU9250_USERCTRL_FIFO_EN_BIT = const(6)
MPU9250_USERCTRL_I2C_MST_EN_BIT = const(5)
MPU9250_USERCTRL_I2C_IF_DIS_BIT = const(4)
MPU9250_USERCTRL_DMP_RESET_BIT = const(3)
MPU9250_USERCTRL_FIFO_RESET_BIT = const(2)
MPU9250_USERCTRL_I2C_MST_RESET_BIT = const(1)
MPU9250_USERCTRL_SIG_COND_RESET_BIT = const(0)

MPU9250_PWR1_DEVICE_RESET_BIT = const(7)
MPU9250_PWR1_SLEEP_BIT = const(6)
MPU9250_PWR1_CYCLE_BIT = const(5)
MPU9250_PWR1_TEMP_DIS_BIT = const(3)
MPU9250_PWR1_CLKSEL_BIT = const(2)
MPU9250_PWR1_CLKSEL_LENGTH = const(3)

MPU9250_CLOCK_INTERNAL = const(0x00)
MPU9250_CLOCK_PLL_XGYRO = const(0x01)
MPU9250_CLOCK_PLL_YGYRO = const(0x02)
MPU9250_CLOCK_PLL_ZGYRO = const(0x03)
MPU9250_CLOCK_PLL_EXT32K = const(0x04)
MPU9250_CLOCK_PLL_EXT19M = const(0x05)
MPU9250_CLOCK_KEEP_RESET = const(0x07)

MPU9250_PWR2_LP_WAKE_CTRL_BIT = const(7)
MPU9250_PWR2_LP_WAKE_CTRL_LENGTH = const(2)
MPU9250_PWR2_STBY_XA_BIT = const(5)
MPU9250_PWR2_STBY_YA_BIT = const(4)
MPU9250_PWR2_STBY_ZA_BIT = const(3)
MPU9250_PWR2_STBY_XG_BIT = const(2)
MPU9250_PWR2_STBY_YG_BIT = const(1)
MPU9250_PWR2_STBY_ZG_BIT = const(0)

MPU9250_WAKE_FREQ_1P25 = const(0x0)
MPU9250_WAKE_FREQ_2P5 = const(0x1)
MPU9250_WAKE_FREQ_5 = const(0x2)
MPU9250_WAKE_FREQ_10 = const(0x3)

MPU9250_BANKSEL_PRFTCH_EN_BIT = const(6)
MPU9250_BANKSEL_CFG_USER_BANK_BIT = const(5)
MPU9250_BANKSEL_MEM_SEL_BIT = const(4)
MPU9250_BANKSEL_MEM_SEL_LENGTH = const(5)

MPU9250_WHO_AM_I_BIT = const(8)
MPU9250_WHO_AM_I_LENGTH = const(8)

MPU9250_DMP_MEMORY_BANKS = const(8)
MPU9250_DMP_MEMORY_BANK_SIZE = const(256)
MPU9250_DMP_MEMORY_CHUNK_SIZE = const(16)


class MPU9250:
    def __init__(self, driver=None) -> None:
        assert driver is not None, "No found driver class"
        self.driver = driver

    def testConnection(self):
        return self.getDeviceID() == 0x71

    def initialize(self):
        # self.driver.writeByte(MPU9250_RA_PWR_MGMT_1, 0x00)
        # utime.sleep_ms(100)
        # self.driver.writeByte(MPU9250_RA_PWR_MGMT_1, 0x01)
        self.setSleelpEnabled(False)
        self.setClockSource(MPU9250_CLOCK_PLL_XGYRO)
        self.setFullScaleGyroRange(MPU9250_GYRO_FS_250)
        self.setFullScaleAccelRange(MPU9250_ACCEL_FS_2)

    def getAuxVDDIOLevel(self):
        """
        Get the auxiliary I2C supply voltage level.
        @return I2C supply voltage level (0=VLOGIC, 1=VDD)
        """
        data = self.driver.readBit(
            MPU9250_RA_YG_OFFS_TC, MPU9250_TC_PWR_MODE_BIT)
        return data

    def setAuxVDDIOLevel(self, level):
        """
        Set the auxiliary I2C supply voltage level.
        @param level I2C supply voltage level (0=VLOGIC, 1=VDD)
        """
        self.driver.writeBit(MPU9250_RA_YG_OFFS_TC,
                             MPU9250_TC_PWR_MODE_BIT, level)

    def getRate(self):
        """
        Get gyroscope output rate divider.
        @return Current sample rate
        """
        return self.driver.readByte(MPU9250_RA_SMPLRT_DIV)

    def setRate(self, rate):
        """
        Set gyroscope sample rate divider.
        @param rate New sample rate divider
        """
        self.driver.writeByte(MPU9250_RA_SMPLRT_DIV, rate)

    def getExternalFrameSync(self):
        """
        Get external FSYNC configuration.
        @return FSYNC configuration value
        """
        return self.driver.readBits(
            MPU9250_RA_CONFIG, MPU9250_CFG_EXT_SYNC_SET_BIT, MPU9250_CFG_EXT_SYNC_SET_LENGTH)

    def setExternalFrameSync(self, sync):
        """
        Set external FSYNC configuration.
        @param sync New FSYNC configuration value
        """
        self.driver.writeBits(
            MPU9250_RA_CONFIG, MPU9250_CFG_EXT_SYNC_SET_BIT, MPU9250_CFG_EXT_SYNC_SET_LENGTH, sync)

    def getDLPFMode(self):
        """
        Get digital low-pass filter configuration.
        @return DLPF configuration
        """
        return self.driver.readBits(MPU9250_RA_CONFIG, MPU9250_CFG_DLPF_CFG_BIT, MPU9250_CFG_DLPF_CFG_LENGTH)

    def setDLPFMode(self, mode):
        """
        Set digital low-pass filter configuration.
        @param mode New DLPF configuration setting
        """
        self.driver.writeBits(
            MPU9250_RA_CONFIG, MPU9250_CFG_DLPF_CFG_BIT, MPU9250_CFG_DLPF_CFG_LENGTH, mode)

    def getFullScaleGyroRange(self):
        """
        Get full-scale gyroscope range.
        @return Current full-scale gyroscope range setting
        """
        return self.driver.readBits(MPU9250_RA_GYRO_CONFIG, MPU9250_GCONFIG_FS_SEL_BIT, MPU9250_GCONFIG_FS_SEL_LENGTH)

    def setFullScaleGyroRange(self, range):
        """
        Set full-scale gyroscope range.
        @param range New full-scale gyroscope range value
        """
        self.driver.writeBits(
            MPU9250_RA_GYRO_CONFIG, MPU9250_GCONFIG_FS_SEL_BIT, MPU9250_GCONFIG_FS_SEL_LENGTH, range)

    def getAccelXSelfTest(self):
        """
        Get self-test enabled setting for accelerometer X axis.
        @return Self-test enabled value
        """
        return self.driver.readBit(MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_XA_ST_BIT)

    def setAccelXSelfTest(self, enabled):
        """
        Get self-test enabled setting for accelerometer X axis.
        @param enabled Self-test enabled value
        """
        self.driver.writeBit(MPU9250_RA_ACCEL_CONFIG,
                             MPU9250_ACONFIG_XA_ST_BIT, enabled)

    def getAccelYSelfTest(self):
        """
        Get self-test enabled setting for accelerometer Y axis.
        @return Self-test enabled value
        """
        return self.driver.readBit(MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_YA_ST_BIT)

    def setAccelYSelfTest(self, enabled):
        """
        Get self-test enabled setting for accelerometer Y axis.
        @param enabled Self-test enabled value
        """
        self.driver.writeBit(MPU9250_RA_ACCEL_CONFIG,
                             MPU9250_ACONFIG_YA_ST_BIT, enabled)

    def getAccelZSelfTest(self):
        """
        Get self-test enabled setting for accelerometer Z axis.
        @return Self-test enabled value
        """
        return self.driver.readBit(MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_ZA_ST_BIT)

    def setAccelZSelfTest(self, enabled):
        """
        Get self-test enabled setting for accelerometer Z axis.
        @param enabled Self-test enabled value
        """
        self.driver.writeBit(MPU9250_RA_ACCEL_CONFIG,
                             MPU9250_ACONFIG_ZA_ST_BIT, enabled)

    def getFullScaleAccelRange(self):
        """
        Get full-scale accelerometer range.
        @return Current full-scale accelerometer range setting
        """
        return self.driver.readBits(MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_AFS_SEL_BIT, MPU9250_ACONFIG_AFS_SEL_LENGTH)

    def setFullScaleAccelRange(self, range):
        """
        Set full-scale accelerometer range.
        @param range New full-scale accelerometer range setting
        """
        self.driver.writeBits(
            MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_AFS_SEL_BIT, MPU9250_ACONFIG_AFS_SEL_LENGTH, range)

    def getDHPFMode(self):
        """
        Get the high-pass filter configuration.
        @return Current high-pass filter configuration
        """
        return self.driver.readBits(MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_ACCEL_HPF_BIT, MPU9250_ACONFIG_ACCEL_HPF_LENGTH)

    def setDHPFMode(self, bandwidth):
        """
        Set the high-pass filter configuration.
        @param bandwidth New high-pass filter configuration
        """
        self.driver.writeBits(MPU9250_RA_ACCEL_CONFIG, MPU9250_ACONFIG_ACCEL_HPF_BIT,
                              MPU9250_ACONFIG_ACCEL_HPF_LENGTH, bandwidth)

    def getFreefallDetectionThreshold(self):
        """
        Get free-fall event acceleration threshold.
        @return Current free-fall acceleration threshold value (LSB = 2mg)
        """
        return self.driver.readByte(MPU9250_RA_FF_THR)

    def setFreefallDetectionThreshold(self, threshold):
        """
        Set free-fall event acceleration threshold.
        @param threshold New free-fall acceleration threshold value (LSB = 2mg)
        """
        self.driver.writeByte(MPU9250_RA_FF_THR, threshold)

    def getFreefallDetectionDuration(self):
        """
        Get free-fall event duration threshold.
        @return Current free-fall duration threshold value (LSB = 1ms)
        """
        return self.driver.readByte(MPU9250_RA_FF_DUR)

    def setFreefallDetectionDuration(self, duration):
        """
        Set free-fall event duration threshold.
        @param duration New free-fall duration threshold value (LSB = 1ms)
        """
        self.driver.writeByte(MPU9250_RA_FF_DUR, duration)

    def getMotionDetectionThreshold(self):
        """
        Get motion detection event acceleration threshold.
        @return Current motion detection acceleration threshold value (LSB = 2mg)
        """
        return self.driver.readByte(MPU9250_RA_MOT_THR)

    def setMotionDetectionThreshold(self, threshold):
        """
        Set motion detection event acceleration threshold.
        @param threshold New motion detection acceleration threshold value (LSB = 2mg)
        """
        self.driver.writeByte(MPU9250_RA_MOT_THR, threshold)

    def getMotionDetectionDuration(self):
        """
        Get motion detection event duration threshold.
        @return Current motion detection duration threshold value (LSB = 1ms)
        """
        return self.driver.readByte(MPU9250_RA_MOT_DUR)

    def setMotionDetectionDuration(self, duration):
        """
        Set motion detection event duration threshold.
        @param duration New motion detection duration threshold value (LSB = 1ms)
        """
        self.driver.writeByte(MPU9250_RA_MOT_DUR, duration)

    def getZeroMotionDetectionThreshold(self):
        """
        Get zero motion detection event acceleration threshold.
        @return Current zero motion detection acceleration threshold value (LSB = 2mg)
        """
        return self.driver.readByte(MPU9250_RA_ZRMOT_THR)

    def setZeroMotionDetectionThreshold(self, threshold):
        """
        Set zero motion detection event acceleration threshold.
        @param threshold New zero motion detection acceleration threshold value (LSB = 2mg)
        """
        self.driver.writeByte(MPU9250_RA_ZRMOT_THR, threshold)

    def getZeroMotionDetectionDuration(self):
        """
        Get zero motion detection event duration threshold.
        @return Current zero motion detection duration threshold value (LSB = 64ms)
        """
        return self.driver.readByte(MPU9250_RA_ZRMOT_DUR)

    def setZeroMotionDetectionDuration(self, duration):
        """
        Set zero motion detection event duration threshold.
        @param duration New zero motion detection duration threshold value (LSB = 1ms)
        """
        self.driver.writeByte(MPU9250_RA_ZRMOT_DUR, duration)

    def getTemperatureFIFOEnabled(self):
        """
        Get temperature FIFO enabled value.
        @return Current temperature FIFO enabled value
        """
        return self.driver.readBit(MPU9250_RA_FIFO_EN, MPU9250_TEMP_FIFO_EN_BIT)

    def setTemperatureFIFOEnabled(self, enabled):
        """
        Set temperature FIFO enabled value.
        @param enabled New temperature FIFO enabled value
        """
        self.driver.writeBit(MPU9250_RA_FIFO_EN,
                             MPU9250_TEMP_FIFO_EN_BIT, enabled)

    def getXGyroFIFOEnabled(self):
        """
        Get gyroscope X-axis FIFO enabled value.
        @return Current gyroscope X-axis FIFO enabled value
        """
        return self.driver.readBit(MPU9250_RA_FIFO_EN, MPU9250_XG_FIFO_EN_BIT)

    def setXGyroFIFOEnabled(self, enabled):
        """
        Set gyroscope X-axis FIFO enabled value.
        @param enabled New gyroscope X-axis FIFO enabled value
        """
        self.driver.writeBit(MPU9250_RA_FIFO_EN,
                             MPU9250_XG_FIFO_EN_BIT, enabled)

    def getYGyroFIFOEnabled(self):
        """
        Get gyroscope Y-axis FIFO enabled value.
        @return Current gyroscope Y-axis FIFO enabled value
        """
        return self.driver.readBit(MPU9250_RA_FIFO_EN, MPU9250_YG_FIFO_EN_BIT)

    def setYGyroFIFOEnabled(self, enabled):
        """
        Set gyroscope Y-axis FIFO enabled value.
        @param enabled New gyroscope Y-axis FIFO enabled value
        """
        self.driver.writeBit(MPU9250_RA_FIFO_EN,
                             MPU9250_YG_FIFO_EN_BIT, enabled)

    def getZGyroFIFOEnabled(self):
        """
        Get gyroscope Z-axis FIFO enabled value.
        @return Current gyroscope Z-axis FIFO enabled value
        """
        return self.driver.readBit(MPU9250_RA_FIFO_EN, MPU9250_ZG_FIFO_EN_BIT)

    def setZGyroFIFOEnabled(self, enabled):
        """
        Set gyroscope Z-axis FIFO enabled value.
        @param enabled New gyroscope Z-axis FIFO enabled value
        """
        self.driver.writeBit(MPU9250_RA_FIFO_EN,
                             MPU9250_ZG_FIFO_EN_BIT, enabled)

    def getAccelFIFOEnabled(self):
        """
        Get accelerometer FIFO enabled value.
        @return Current accelerometer FIFO enabled value
        """
        return self.driver.readBit(MPU9250_RA_FIFO_EN, MPU9250_ACCEL_FIFO_EN_BIT)

    def setAccelFIFOEnabled(self, enabled):
        """
        Set accelerometer FIFO enabled value.
        @param enabled New accelerometer FIFO enabled value
        """
        self.driver.writeBit(MPU9250_RA_FIFO_EN,
                             MPU9250_ACCEL_FIFO_EN_BIT, enabled)

    def getInterruptMode(self):
        """
        Get interrupt logic level mode.
        @return Current interrupt mode (0=active-high, 1=active-low)
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_INT_LEVEL_BIT)

    def setInterruptMode(self, mode):
        """
        Set interrupt logic level mode.
        @param mode New interrupt mode (0=active-high, 1=active-low)
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_INT_LEVEL_BIT, mode)

    def getInterruptDrive(self):
        """
        Get interrupt drive mode.
        @return Current interrupt drive mode (0=push-pull, 1=open-drain)
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_INT_OPEN_BIT)

    def setInterruptDrive(self, drive):
        """
        Set interrupt drive mode.
        @param drive New interrupt drive mode (0=push-pull, 1=open-drain)
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_INT_OPEN_BIT, drive)

    def getInterruptLatch(self):
        """
        Get interrupt latch mode.
        @return Current latch mode (0=50us-pulse, 1=latch-until-int-cleared)
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_LATCH_INT_EN_BIT)

    def setInterruptLatch(self, latch):
        """
        Set interrupt latch mode.
        @param latch New latch mode (0=50us-pulse, 1=latch-until-int-cleared)
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_LATCH_INT_EN_BIT, latch)

    def getInterruptLatchClear(self):
        """
        Get interrupt latch clear mode.
        @return Current latch clear mode (0=status-read-only, 1=any-register-read)
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_INT_RD_CLEAR_BIT)

    def setInterruptLatchClear(self, clear):
        """
        Set interrupt latch clear mode.
        @param clear New latch clear mode (0=status-read-only, 1=any-register-read)
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_INT_RD_CLEAR_BIT, clear)

    def getFSyncInterruptLevel(self):
        """
        Get FSYNC interrupt logic level mode.
        @return Current FSYNC interrupt mode (0=active-high, 1=active-low)
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_FSYNC_INT_LEVEL_BIT)

    def setFSyncInterruptLevel(self, level):
        """
        Set FSYNC interrupt logic level mode.
        @param mode New FSYNC interrupt mode (0=active-high, 1=active-low)
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_FSYNC_INT_LEVEL_BIT, level)

    def getFSyncInterruptEnabled(self):
        """
        Get FSYNC pin interrupt enabled setting.
        @return Current interrupt enabled setting
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_FSYNC_INT_EN_BIT)

    def setFSyncInterruptEnabled(self, enabled):
        """
        Set FSYNC pin interrupt enabled setting.
        @param enabled New FSYNC pin interrupt enabled setting
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_FSYNC_INT_EN_BIT, enabled)

    def getI2CBypassEnabled(self):
        """
        Get I2C bypass enabled status.
        @return Current I2C bypass enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_I2C_BYPASS_EN_BIT)

    def setI2CBypassEnabled(self, enabled):
        """
        Set I2C bypass enabled status.
        @param enabled New I2C bypass enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_I2C_BYPASS_EN_BIT, enabled)

    def getClockOutputEnabled(self):
        """
        Get reference clock output enabled status.
        @return Current reference clock output enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_PIN_CFG, MPU9250_INTCFG_CLKOUT_EN_BIT)

    def setClockOutputEnabled(self, enabled):
        """
        Set reference clock output enabled status.
        @param enabled New reference clock output enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_PIN_CFG,
                             MPU9250_INTCFG_CLKOUT_EN_BIT, enabled)

    def getIntEnabled(self):
        """
        Get full interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readByte(MPU9250_RA_INT_ENABLE)

    def setIntEnabled(self, enabled):
        """
        Set full interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeByte(MPU9250_RA_INT_ENABLE, enabled)

    def getIntFreefallEnabled(self):
        """
        Get Free Fall interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_ENABLE, MPU9250_INTERRUPT_FF_BIT)

    def setIntFreefallEnabled(self, enabled):
        """
        Set Free Fall interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_ENABLE,
                             MPU9250_INTERRUPT_FF_BIT, enabled)

    def getIntMotionEnabled(self):
        """
        Get Motion Detection interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_ENABLE, MPU9250_INTERRUPT_MOT_BIT)

    def setIntMotionEnabled(self, enabled):
        """
        Set Motion Detection interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_ENABLE,
                             MPU9250_INTERRUPT_MOT_BIT, enabled)

    def getIntZeroMotionEnabled(self):
        """
        Get Zero Motion Detection interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_ENABLE, MPU9250_INTERRUPT_ZMOT_BIT)

    def setIntZeroMotionEnabled(self, enabled):
        """
        Set Zero Motion Detection interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_ENABLE,
                             MPU9250_INTERRUPT_ZMOT_BIT, enabled)

    def getIntFIFOBufferOverflowEnabled(self):
        """
        Get FIFO Buffer Overflow interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_ENABLE, MPU9250_INTERRUPT_FIFO_OFLOW_BIT)

    def setIntFIFOBufferOverflowEnabled(self, enabled):
        """
        Set FIFO Buffer Overflow interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_ENABLE,
                             MPU9250_INTERRUPT_FIFO_OFLOW_BIT, enabled)

    def getIntDataReadyEnabled(self):
        """
        Get Data Ready interrupt enabled setting.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU9250_RA_INT_ENABLE, MPU9250_INTERRUPT_DATA_RDY_BIT)

    def setIntDataReadyEnabled(self, enabled):
        """
        Set Data Ready interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU9250_RA_INT_ENABLE,
                             MPU9250_INTERRUPT_DATA_RDY_BIT, enabled)

    def getIntStatus(self):
        """
        Get full set of interrupt status bits.
        @return Current interrupt status
        """
        return self.driver.readByte(MPU9250_RA_INT_STATUS)

    def getIntFreefallStatus(self):
        """
        Get Free Fall interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU9250_RA_INT_STATUS, MPU9250_INTERRUPT_FF_BIT)

    def getIntMotionStatus(self):
        """
        Get Motion Detection interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU9250_RA_INT_STATUS, MPU9250_INTERRUPT_MOT_BIT)

    def getIntZeroMotionStatus(self):
        """
        Get Zero Motion Detection interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU9250_RA_INT_STATUS, MPU9250_INTERRUPT_ZMOT_BIT)

    def getIntFIFOBufferOverflowStatus(self):
        """
        Get FIFO Buffer Overflow interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU9250_RA_INT_STATUS, MPU9250_INTERRUPT_FIFO_OFLOW_BIT)

    def getIntDataReadyStatus(self):
        """
        Get Data Ready interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU9250_RA_INT_STATUS, MPU9250_INTERRUPT_DATA_RDY_BIT)

    def getMotion9(self):
        (ax, ay, az, gx, gy, gz) = self.getMotion6()
        self.driver.writeByte(MPU9250_RA_INT_PIN_CFG, 0x02)
        utime.sleep_ms(10)
        self.driver.writeByte(0x0A, 0x01, i2c_address=MPU9150_RA_MAG_ADDRESS)
        utime.sleep_ms(10)
        buffer = self.driver.readBytes(MPU9150_RA_MAG_XOUT_L, 6,
                                       i2c_address=MPU9150_RA_MAG_ADDRESS)
        unpacked_buffer = ustruct.unpack("<hhh", buffer)
        (mx, my, mz) = unpacked_buffer
        return (ax, ay, az, gx, gy, gz)+(mx, my, mz)

    def getMotion6(self):
        """
        Get raw 6-axis motion sensor readings (accel/gyro).
        @return A new tuple, include: ax, ay, az, gx, gy, gz
        """
        data = self.driver.readWords(MPU9250_RA_ACCEL_XOUT_H, 7)
        ax = data[0]
        ay = data[1]
        az = data[2]
        # skip temperature
        gx = data[4]
        gy = data[5]
        gz = data[6]
        return (ax, ay, az, gx, gy, gz)

    def getAccelerationX(self):
        """
        Get X-axis accelerometer reading.
        @return X-axis acceleration measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_ACCEL_XOUT_H)
        return buffer

    def getAccelerationY(self):
        """
        Get Y-axis accelerometer reading.
        @return Y-axis acceleration measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_ACCEL_YOUT_H)
        return buffer

    def getAccelerationZ(self):
        """
        Get Z-axis accelerometer reading.
        @return Z-axis acceleration measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_ACCEL_ZOUT_H)
        return buffer

    def getTemperature(self):
        """
        Get current internal temperature.
        @return Temperature reading in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_TEMP_OUT_H)
        return buffer

    def getRotation(self):
        """
        Get 3-axis gyroscope readings.
        @return A new tuple, include: x, y, z
        """
        buffer = self.driver.readWords(MPU9250_RA_GYRO_XOUT_H, 3)
        x = buffer[0]
        y = buffer[1]
        z = buffer[2]
        return (x, y, z)

    def getRotationX(self):
        """
        Get X-axis gyroscope reading.
        @return X-axis rotation measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_GYRO_XOUT_H)
        return buffer

    def getRotationY(self):
        """
        Get Y-axis gyroscope reading.
        @return Y-axis rotation measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_GYRO_YOUT_H)
        return buffer

    def getRotationZ(self):
        """
        Get Z-axis gyroscope reading.
        @return Z-axis rotation measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readWord(MPU9250_RA_GYRO_ZOUT_H)
        return buffer

    def getExternalSensorByte(self, position):
        return self.driver.readByte(MPU9250_RA_EXT_SENS_DATA_00 + position)

    def getExternalSensorWord(self, position):
        return self.driver.readWord(MPU9250_RA_EXT_SENS_DATA_00 + position)

    def getExternalSensorDWord(self, position):
        buffer = self.driver.readBytes(
            MPU9250_RA_EXT_SENS_DATA_00 + position, 4)
        unpacked_buffer = ustruct.unpack('>l', buffer)
        return unpacked_buffer[0]

    def getXNegMotionDetected(self):
        """
        Get X-axis negative motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_XNEG_BIT)

    def getXPosMotionDetected(self):
        """
        Get X-axis positive motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_XPOS_BIT)

    def getYNegMotionDetected(self):
        """
        Get Y-axis negative motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_YNEG_BIT)

    def getYPosMotionDetected(self):
        """
        Get Y-axis positive motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_YPOS_BIT)

    def getZNegMotionDetected(self):
        """
        Get Z-axis negative motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_ZNEG_BIT)

    def getZPosMotionDetected(self):
        """
        Get Z-axis positive motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_ZPOS_BIT)

    def getZeroMotionDetected(self):
        """
        Get zero motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU9250_RA_MOT_DETECT_STATUS, MPU9250_MOTION_MOT_ZRMOT_BIT)

    def setSlaveOutputByte(self, num, data):
        if num > 3:
            return None
        self.driver.writeByte(MPU9250_RA_I2C_SLV0_DO+num, data)

    def getExternalShadowDelayEnabled(self):
        return self.driver.readBit(MPU9250_RA_I2C_MST_DELAY_CTRL, MPU9250_DELAYCTRL_DELAY_ES_SHADOW_BIT)

    def setExternalShadowDelayEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_I2C_MST_DELAY_CTRL,
                             MPU9250_DELAYCTRL_DELAY_ES_SHADOW_BIT, enabled)

    def getSlaveDelayEnabled(self, num):
        if num > 4:
            return 0
        return self.driver.readBit(MPU9250_RA_I2C_MST_DELAY_CTRL, num)

    def setSlaveDelayEnabled(self, num, enabled):
        self.driver.writeBit(MPU9250_RA_I2C_MST_DELAY_CTRL, num, enabled)

    def resetGyroscopePath(self):
        self.driver.writeBit(MPU9250_RA_SIGNAL_PATH_RESET,
                             MPU9250_PATHRESET_GYRO_RESET_BIT, True)

    def resetAccelerometerPath(self):
        self.driver.writeBit(MPU9250_RA_SIGNAL_PATH_RESET,
                             MPU9250_PATHRESET_ACCEL_RESET_BIT, True)

    def resetTemperaturePath(self):
        self.driver.writeBit(MPU9250_RA_SIGNAL_PATH_RESET,
                             MPU9250_PATHRESET_TEMP_RESET_BIT, True)

    def getAccelerometerPowerOnDelay(self):
        return self.driver.readBits(MPU9250_RA_MOT_DETECT_CTRL,
                                    MPU9250_DETECT_ACCEL_ON_DELAY_BIT, MPU9250_DETECT_ACCEL_ON_DELAY_LENGTH)

    def setAccelerometerPowerOnDelay(self, delay):
        self.driver.writeBits(MPU9250_RA_MOT_DETECT_CTRL,
                              MPU9250_DETECT_ACCEL_ON_DELAY_BIT, MPU9250_DETECT_ACCEL_ON_DELAY_LENGTH, delay)

    def getFreefallDetectionCounterDecrement(self):
        return self.driver.readBits(MPU9250_RA_MOT_DETECT_CTRL, MPU9250_DETECT_FF_COUNT_BIT, MPU9250_DETECT_FF_COUNT_LENGTH)

    def setFreefallDetectionCounterDecrement(self, decrement):
        self.driver.writeBits(MPU9250_RA_MOT_DETECT_CTRL, MPU9250_DETECT_FF_COUNT_BIT,
                              MPU9250_DETECT_FF_COUNT_LENGTH, decrement)

    def getMotionDetectionCounterDecrement(self):
        return self.driver.readBits(MPU9250_RA_MOT_DETECT_CTRL, MPU9250_DETECT_MOT_COUNT_BIT, MPU9250_DETECT_MOT_COUNT_LENGTH)

    def setMotionDetectionCounterDecrement(self, decrement):
        self.driver.writeBits(MPU9250_RA_MOT_DETECT_CTRL, MPU9250_DETECT_MOT_COUNT_BIT,
                              MPU9250_DETECT_MOT_COUNT_LENGTH, decrement)

    def getFIFOEnabled(self):
        return self.driver.readBit(MPU9250_RA_USER_CTRL, MPU9250_USERCTRL_FIFO_EN_BIT)

    def setFIFOEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_USER_CTRL,
                             MPU9250_USERCTRL_FIFO_EN_BIT, enabled)

    def getI2CMasterModeEnabled(self):
        return self.driver.readBit(MPU9250_RA_USER_CTRL, MPU9250_USERCTRL_I2C_MST_EN_BIT)

    def setI2CMasterModeEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_USER_CTRL,
                             MPU9250_USERCTRL_I2C_MST_EN_BIT, enabled)

    def switchSPIEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_USER_CTRL,
                             MPU9250_USERCTRL_I2C_IF_DIS_BIT, enabled)

    def resetFIFO(self):
        self.driver.writeBit(MPU9250_RA_USER_CTRL,
                             MPU9250_USERCTRL_FIFO_RESET_BIT, True)

    def resetI2CMaster(self):
        self.driver.writeBit(MPU9250_RA_USER_CTRL,
                             MPU9250_USERCTRL_I2C_MST_RESET_BIT, True)

    def resetSensors(self):
        self.driver.writeBit(MPU9250_RA_USER_CTRL,
                             MPU9250_USERCTRL_SIG_COND_RESET_BIT, True)

    def reset(self):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_1,
                             MPU9250_PWR1_DEVICE_RESET_BIT, True)

    def getSleepEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_1, MPU9250_PWR1_SLEEP_BIT)

    def setSleelpEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_1,
                             MPU9250_PWR1_SLEEP_BIT, enabled)

    def getWakeCycleEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_1, MPU9250_PWR1_CYCLE_BIT)

    def setWakeCycleEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_1,
                             MPU9250_PWR1_CYCLE_BIT, enabled)

    def getTemperatureSensorEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_1, MPU9250_PWR1_TEMP_DIS_BIT)

    def setTemperatureSensorEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_1,
                             MPU9250_PWR1_TEMP_DIS_BIT, not enabled)

    def getClockSource(self):
        return self.driver.readBits(MPU9250_RA_PWR_MGMT_1, MPU9250_PWR1_CLKSEL_BIT, MPU9250_PWR1_CLKSEL_LENGTH)

    def setClockSource(self, source):
        self.driver.writeBits(
            MPU9250_RA_PWR_MGMT_1, MPU9250_PWR1_CLKSEL_BIT, MPU9250_PWR1_CLKSEL_LENGTH, source)

    def getWakeFrequency(self):
        return self.driver.readBits(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_LP_WAKE_CTRL_BIT, MPU9250_PWR2_LP_WAKE_CTRL_LENGTH)

    def setWakeFrequency(self, frequency):
        self.driver.writeBits(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_LP_WAKE_CTRL_BIT,
                              MPU9250_PWR2_LP_WAKE_CTRL_LENGTH, frequency)

    def getStandbyXAccelEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_STBY_XA_BIT)

    def setStandbyXAccelEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_2,
                             MPU9250_PWR2_STBY_XA_BIT, enabled)

    def getStandbyYAccelEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_STBY_YA_BIT)

    def setStandbyYAccelEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_2,
                             MPU9250_PWR2_STBY_YA_BIT, enabled)

    def getStandbyZAccelEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_STBY_ZA_BIT)

    def setStandbyZAccelEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_2,
                             MPU9250_PWR2_STBY_ZA_BIT, enabled)

    def getStandbyXGyroEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_STBY_XG_BIT)

    def getStandbyXGyroEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_2,
                             MPU9250_PWR2_STBY_XG_BIT, enabled)

    def getStandbyYGyroEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_STBY_YG_BIT)

    def getStandbyYGyroEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_2,
                             MPU9250_PWR2_STBY_YG_BIT, enabled)

    def getStandbyZGyroEnabled(self):
        return self.driver.readBit(MPU9250_RA_PWR_MGMT_2, MPU9250_PWR2_STBY_ZG_BIT)

    def getStandbyZGyroEnabled(self, enabled):
        self.driver.writeBit(MPU9250_RA_PWR_MGMT_2,
                             MPU9250_PWR2_STBY_ZG_BIT, enabled)

    def getFIFOCount(self):
        return self.driver.readWord(MPU9250_RA_FIFO_COUNTH)

    def getFIFOByte(self):
        return self.driver.readByte(MPU9250_RA_FIFO_R_W)

    def getFIFOBytes(self, length):
        return self.driver.readBytes(MPU9250_RA_FIFO_R_W, length)

    def setFIFOByte(self, data):
        self.driver.writeByte(MPU9250_RA_FIFO_R_W, data)

    def getDeviceID(self):
        return self.driver.readByte(MPU9250_RA_WHO_AM_I)

    def setDeviceID(self, id):
        self.driver.readBits(MPU9250_RA_WHO_AM_I,
                             MPU9250_WHO_AM_I_BIT, MPU9250_WHO_AM_I_LENGTH, id)
