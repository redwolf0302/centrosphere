# Refer to I2Cdev library collection, https://github.com/jrowberg/i2cdevlib/tree/master/RP2040
from micropython import const

# address pin low (GND), default for InvenSense evaluation board
MPU6050_ADDRESS_AD0_LOW = const(0x68)
MPU6050_ADDRESS_AD0_HIGH = const(0x69)  # address pin high (VCC)
MPU6050_DEFAULT_ADDRESS = const(MPU6050_ADDRESS_AD0_LOW)

# [7] PWR_MODE, [6:1] XG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_XG_OFFS_TC = const(0x00)
# [7] PWR_MODE, [6:1] YG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_YG_OFFS_TC = const(0x01)
# [7] PWR_MODE, [6:1] ZG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_ZG_OFFS_TC = const(0x02)
MPU6050_RA_X_FINE_GAIN = const(0x03)  # [7:0] X_FINE_GAIN
MPU6050_RA_Y_FINE_GAIN = const(0x04)  # [7:0] Y_FINE_GAIN
MPU6050_RA_Z_FINE_GAIN = const(0x05)  # [7:0] Z_FINE_GAIN
MPU6050_RA_XA_OFFS_H = const(0x06)  # [15:0] XA_OFFS
MPU6050_RA_XA_OFFS_L_TC = const(0x07)
MPU6050_RA_YA_OFFS_H = const(0x08)  # [15:0] YA_OFFS
MPU6050_RA_YA_OFFS_L_TC = const(0x09)
MPU6050_RA_ZA_OFFS_H = const(0x0A)  # [15:0] ZA_OFFS
MPU6050_RA_ZA_OFFS_L_TC = const(0x0B)
MPU6050_RA_SELF_TEST_X = const(0x0D)  # [7:5] XA_TEST[4-2], [4:0] XG_TEST[4-0]
MPU6050_RA_SELF_TEST_Y = const(0x0E)  # [7:5] YA_TEST[4-2], [4:0] YG_TEST[4-0]
MPU6050_RA_SELF_TEST_Z = const(0x0F)  # [7:5] ZA_TEST[4-2], [4:0] ZG_TEST[4-0]
# [5:4] XA_TEST[1-0], [3:2] YA_TEST[1-0], [1:0] ZA_TEST[1-0]
MPU6050_RA_SELF_TEST_A = const(0x10)
MPU6050_RA_XG_OFFS_USRH = const(0x13)  # [15:0] XG_OFFS_USR
MPU6050_RA_XG_OFFS_USRL = const(0x14)
MPU6050_RA_YG_OFFS_USRH = const(0x15)  # [15:0] YG_OFFS_USR
MPU6050_RA_YG_OFFS_USRL = const(0x16)
MPU6050_RA_ZG_OFFS_USRH = const(0x17)  # [15:0] ZG_OFFS_USR
MPU6050_RA_ZG_OFFS_USRL = const(0x18)
MPU6050_RA_SMPLRT_DIV = const(0x19)
MPU6050_RA_CONFIG = const(0x1A)
MPU6050_RA_GYRO_CONFIG = const(0x1B)
MPU6050_RA_ACCEL_CONFIG = const(0x1C)
MPU6050_RA_FF_THR = const(0x1D)
MPU6050_RA_FF_DUR = const(0x1E)
MPU6050_RA_MOT_THR = const(0x1F)
MPU6050_RA_MOT_DUR = const(0x20)
MPU6050_RA_ZRMOT_THR = const(0x21)
MPU6050_RA_ZRMOT_DUR = const(0x22)
MPU6050_RA_FIFO_EN = const(0x23)
MPU6050_RA_I2C_MST_CTRL = const(0x24)
MPU6050_RA_I2C_SLV0_ADDR = const(0x25)
MPU6050_RA_I2C_SLV0_REG = const(0x26)
MPU6050_RA_I2C_SLV0_CTRL = const(0x27)
MPU6050_RA_I2C_SLV1_ADDR = const(0x28)
MPU6050_RA_I2C_SLV1_REG = const(0x29)
MPU6050_RA_I2C_SLV1_CTRL = const(0x2A)
MPU6050_RA_I2C_SLV2_ADDR = const(0x2B)
MPU6050_RA_I2C_SLV2_REG = const(0x2C)
MPU6050_RA_I2C_SLV2_CTRL = const(0x2D)
MPU6050_RA_I2C_SLV3_ADDR = const(0x2E)
MPU6050_RA_I2C_SLV3_REG = const(0x2F)
MPU6050_RA_I2C_SLV3_CTRL = const(0x30)
MPU6050_RA_I2C_SLV4_ADDR = const(0x31)
MPU6050_RA_I2C_SLV4_REG = const(0x32)
MPU6050_RA_I2C_SLV4_DO = const(0x33)
MPU6050_RA_I2C_SLV4_CTRL = const(0x34)
MPU6050_RA_I2C_SLV4_DI = const(0x35)
MPU6050_RA_I2C_MST_STATUS = const(0x36)
MPU6050_RA_INT_PIN_CFG = const(0x37)
MPU6050_RA_INT_ENABLE = const(0x38)
MPU6050_RA_DMP_INT_STATUS = const(0x39)
MPU6050_RA_INT_STATUS = const(0x3A)
MPU6050_RA_ACCEL_XOUT_H = const(0x3B)
MPU6050_RA_ACCEL_XOUT_L = const(0x3C)
MPU6050_RA_ACCEL_YOUT_H = const(0x3D)
MPU6050_RA_ACCEL_YOUT_L = const(0x3E)
MPU6050_RA_ACCEL_ZOUT_H = const(0x3F)
MPU6050_RA_ACCEL_ZOUT_L = const(0x40)
MPU6050_RA_TEMP_OUT_H = const(0x41)
MPU6050_RA_TEMP_OUT_L = const(0x42)
MPU6050_RA_GYRO_XOUT_H = const(0x43)
MPU6050_RA_GYRO_XOUT_L = const(0x44)
MPU6050_RA_GYRO_YOUT_H = const(0x45)
MPU6050_RA_GYRO_YOUT_L = const(0x46)
MPU6050_RA_GYRO_ZOUT_H = const(0x47)
MPU6050_RA_GYRO_ZOUT_L = const(0x48)
MPU6050_RA_EXT_SENS_DATA_00 = const(0x49)
MPU6050_RA_EXT_SENS_DATA_01 = const(0x4A)
MPU6050_RA_EXT_SENS_DATA_02 = const(0x4B)
MPU6050_RA_EXT_SENS_DATA_03 = const(0x4C)
MPU6050_RA_EXT_SENS_DATA_04 = const(0x4D)
MPU6050_RA_EXT_SENS_DATA_05 = const(0x4E)
MPU6050_RA_EXT_SENS_DATA_06 = const(0x4F)
MPU6050_RA_EXT_SENS_DATA_07 = const(0x50)
MPU6050_RA_EXT_SENS_DATA_08 = const(0x51)
MPU6050_RA_EXT_SENS_DATA_09 = const(0x52)
MPU6050_RA_EXT_SENS_DATA_10 = const(0x53)
MPU6050_RA_EXT_SENS_DATA_11 = const(0x54)
MPU6050_RA_EXT_SENS_DATA_12 = const(0x55)
MPU6050_RA_EXT_SENS_DATA_13 = const(0x56)
MPU6050_RA_EXT_SENS_DATA_14 = const(0x57)
MPU6050_RA_EXT_SENS_DATA_15 = const(0x58)
MPU6050_RA_EXT_SENS_DATA_16 = const(0x59)
MPU6050_RA_EXT_SENS_DATA_17 = const(0x5A)
MPU6050_RA_EXT_SENS_DATA_18 = const(0x5B)
MPU6050_RA_EXT_SENS_DATA_19 = const(0x5C)
MPU6050_RA_EXT_SENS_DATA_20 = const(0x5D)
MPU6050_RA_EXT_SENS_DATA_21 = const(0x5E)
MPU6050_RA_EXT_SENS_DATA_22 = const(0x5F)
MPU6050_RA_EXT_SENS_DATA_23 = const(0x60)
MPU6050_RA_MOT_DETECT_STATUS = const(0x61)
MPU6050_RA_I2C_SLV0_DO = const(0x63)
MPU6050_RA_I2C_SLV1_DO = const(0x64)
MPU6050_RA_I2C_SLV2_DO = const(0x65)
MPU6050_RA_I2C_SLV3_DO = const(0x66)
MPU6050_RA_I2C_MST_DELAY_CTRL = const(0x67)
MPU6050_RA_SIGNAL_PATH_RESET = const(0x68)
MPU6050_RA_MOT_DETECT_CTRL = const(0x69)
MPU6050_RA_USER_CTRL = const(0x6A)
MPU6050_RA_PWR_MGMT_1 = const(0x6B)
MPU6050_RA_PWR_MGMT_2 = const(0x6C)
MPU6050_RA_BANK_SEL = const(0x6D)
MPU6050_RA_MEM_START_ADDR = const(0x6E)
MPU6050_RA_MEM_R_W = const(0x6F)
MPU6050_RA_DMP_CFG_1 = const(0x70)
MPU6050_RA_DMP_CFG_2 = const(0x71)
MPU6050_RA_FIFO_COUNTH = const(0x72)
MPU6050_RA_FIFO_COUNTL = const(0x73)
MPU6050_RA_FIFO_R_W = const(0x74)
MPU6050_RA_WHO_AM_I = const(0x75)

MPU6050_SELF_TEST_XA_1_BIT = const(0x07)
MPU6050_SELF_TEST_XA_1_LENGTH = const(0x03)
MPU6050_SELF_TEST_XA_2_BIT = const(0x05)
MPU6050_SELF_TEST_XA_2_LENGTH = const(0x02)
MPU6050_SELF_TEST_YA_1_BIT = const(0x07)
MPU6050_SELF_TEST_YA_1_LENGTH = const(0x03)
MPU6050_SELF_TEST_YA_2_BIT = const(0x03)
MPU6050_SELF_TEST_YA_2_LENGTH = const(0x02)
MPU6050_SELF_TEST_ZA_1_BIT = const(0x07)
MPU6050_SELF_TEST_ZA_1_LENGTH = const(0x03)
MPU6050_SELF_TEST_ZA_2_BIT = const(0x01)
MPU6050_SELF_TEST_ZA_2_LENGTH = const(0x02)

MPU6050_SELF_TEST_XG_1_BIT = const(0x04)
MPU6050_SELF_TEST_XG_1_LENGTH = const(0x05)
MPU6050_SELF_TEST_YG_1_BIT = const(0x04)
MPU6050_SELF_TEST_YG_1_LENGTH = const(0x05)
MPU6050_SELF_TEST_ZG_1_BIT = const(0x04)
MPU6050_SELF_TEST_ZG_1_LENGTH = const(0x05)

MPU6050_TC_PWR_MODE_BIT = const(7)
MPU6050_TC_OFFSET_BIT = const(6)
MPU6050_TC_OFFSET_LENGTH = const(6)
MPU6050_TC_OTP_BNK_VLD_BIT = const(0)

MPU6050_VDDIO_LEVEL_VLOGIC = const(0)
MPU6050_VDDIO_LEVEL_VDD = const(1)

MPU6050_CFG_EXT_SYNC_SET_BIT = const(5)
MPU6050_CFG_EXT_SYNC_SET_LENGTH = const(3)
MPU6050_CFG_DLPF_CFG_BIT = const(2)
MPU6050_CFG_DLPF_CFG_LENGTH = const(3)

MPU6050_EXT_SYNC_DISABLED = const(0x0)
MPU6050_EXT_SYNC_TEMP_OUT_L = const(0x1)
MPU6050_EXT_SYNC_GYRO_XOUT_L = const(0x2)
MPU6050_EXT_SYNC_GYRO_YOUT_L = const(0x3)
MPU6050_EXT_SYNC_GYRO_ZOUT_L = const(0x4)
MPU6050_EXT_SYNC_ACCEL_XOUT_L = const(0x5)
MPU6050_EXT_SYNC_ACCEL_YOUT_L = const(0x6)
MPU6050_EXT_SYNC_ACCEL_ZOUT_L = const(0x7)

MPU6050_DLPF_BW_256 = const(0x00)
MPU6050_DLPF_BW_188 = const(0x01)
MPU6050_DLPF_BW_98 = const(0x02)
MPU6050_DLPF_BW_42 = const(0x03)
MPU6050_DLPF_BW_20 = const(0x04)
MPU6050_DLPF_BW_10 = const(0x05)
MPU6050_DLPF_BW_5 = const(0x06)

MPU6050_GCONFIG_FS_SEL_BIT = const(4)
MPU6050_GCONFIG_FS_SEL_LENGTH = const(2)

MPU6050_GYRO_FS_250 = const(0x00)
MPU6050_GYRO_FS_500 = const(0x01)
MPU6050_GYRO_FS_1000 = const(0x02)
MPU6050_GYRO_FS_2000 = const(0x03)

MPU6050_ACONFIG_XA_ST_BIT = const(7)
MPU6050_ACONFIG_YA_ST_BIT = const(6)
MPU6050_ACONFIG_ZA_ST_BIT = const(5)
MPU6050_ACONFIG_AFS_SEL_BIT = const(4)
MPU6050_ACONFIG_AFS_SEL_LENGTH = const(2)
MPU6050_ACONFIG_ACCEL_HPF_BIT = const(2)
MPU6050_ACONFIG_ACCEL_HPF_LENGTH = const(3)

MPU6050_ACCEL_FS_2 = const(0x00)
MPU6050_ACCEL_FS_4 = const(0x01)
MPU6050_ACCEL_FS_8 = const(0x02)
MPU6050_ACCEL_FS_16 = const(0x03)

MPU6050_DHPF_RESET = const(0x00)
MPU6050_DHPF_5 = const(0x01)
MPU6050_DHPF_2P5 = const(0x02)
MPU6050_DHPF_1P25 = const(0x03)
MPU6050_DHPF_0P63 = const(0x04)
MPU6050_DHPF_HOLD = const(0x07)

MPU6050_TEMP_FIFO_EN_BIT = const(7)
MPU6050_XG_FIFO_EN_BIT = const(6)
MPU6050_YG_FIFO_EN_BIT = const(5)
MPU6050_ZG_FIFO_EN_BIT = const(4)
MPU6050_ACCEL_FIFO_EN_BIT = const(3)
MPU6050_SLV2_FIFO_EN_BIT = const(2)
MPU6050_SLV1_FIFO_EN_BIT = const(1)
MPU6050_SLV0_FIFO_EN_BIT = const(0)

MPU6050_MULT_MST_EN_BIT = const(7)
MPU6050_WAIT_FOR_ES_BIT = const(6)
MPU6050_SLV_3_FIFO_EN_BIT = const(5)
MPU6050_I2C_MST_P_NSR_BIT = const(4)
MPU6050_I2C_MST_CLK_BIT = const(3)
MPU6050_I2C_MST_CLK_LENGTH = const(4)

MPU6050_CLOCK_DIV_348 = const(0x0)
MPU6050_CLOCK_DIV_333 = const(0x1)
MPU6050_CLOCK_DIV_320 = const(0x2)
MPU6050_CLOCK_DIV_308 = const(0x3)
MPU6050_CLOCK_DIV_296 = const(0x4)
MPU6050_CLOCK_DIV_286 = const(0x5)
MPU6050_CLOCK_DIV_276 = const(0x6)
MPU6050_CLOCK_DIV_267 = const(0x7)
MPU6050_CLOCK_DIV_258 = const(0x8)
MPU6050_CLOCK_DIV_500 = const(0x9)
MPU6050_CLOCK_DIV_471 = const(0xA)
MPU6050_CLOCK_DIV_444 = const(0xB)
MPU6050_CLOCK_DIV_421 = const(0xC)
MPU6050_CLOCK_DIV_400 = const(0xD)
MPU6050_CLOCK_DIV_381 = const(0xE)
MPU6050_CLOCK_DIV_364 = const(0xF)

MPU6050_I2C_SLV_RW_BIT = const(7)
MPU6050_I2C_SLV_ADDR_BIT = const(6)
MPU6050_I2C_SLV_ADDR_LENGTH = const(7)
MPU6050_I2C_SLV_EN_BIT = const(7)
MPU6050_I2C_SLV_BYTE_SW_BIT = const(6)
MPU6050_I2C_SLV_REG_DIS_BIT = const(5)
MPU6050_I2C_SLV_GRP_BIT = const(4)
MPU6050_I2C_SLV_LEN_BIT = const(3)
MPU6050_I2C_SLV_LEN_LENGTH = const(4)

MPU6050_I2C_SLV4_RW_BIT = const(7)
MPU6050_I2C_SLV4_ADDR_BIT = const(6)
MPU6050_I2C_SLV4_ADDR_LENGTH = const(7)
MPU6050_I2C_SLV4_EN_BIT = const(7)
MPU6050_I2C_SLV4_INT_EN_BIT = const(6)
MPU6050_I2C_SLV4_REG_DIS_BIT = const(5)
MPU6050_I2C_SLV4_MST_DLY_BIT = const(4)
MPU6050_I2C_SLV4_MST_DLY_LENGTH = const(5)

MPU6050_MST_PASS_THROUGH_BIT = const(7)
MPU6050_MST_I2C_SLV4_DONE_BIT = const(6)
MPU6050_MST_I2C_LOST_ARB_BIT = const(5)
MPU6050_MST_I2C_SLV4_NACK_BIT = const(4)
MPU6050_MST_I2C_SLV3_NACK_BIT = const(3)
MPU6050_MST_I2C_SLV2_NACK_BIT = const(2)
MPU6050_MST_I2C_SLV1_NACK_BIT = const(1)
MPU6050_MST_I2C_SLV0_NACK_BIT = const(0)

MPU6050_INTCFG_INT_LEVEL_BIT = const(7)
MPU6050_INTCFG_INT_OPEN_BIT = const(6)
MPU6050_INTCFG_LATCH_INT_EN_BIT = const(5)
MPU6050_INTCFG_INT_RD_CLEAR_BIT = const(4)
MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT = const(3)
MPU6050_INTCFG_FSYNC_INT_EN_BIT = const(2)
MPU6050_INTCFG_I2C_BYPASS_EN_BIT = const(1)
MPU6050_INTCFG_CLKOUT_EN_BIT = const(0)

MPU6050_INTMODE_ACTIVEHIGH = const(0x00)
MPU6050_INTMODE_ACTIVELOW = const(0x01)

MPU6050_INTDRV_PUSHPULL = const(0x00)
MPU6050_INTDRV_OPENDRAIN = const(0x01)

MPU6050_INTLATCH_50USPULSE = const(0x00)
MPU6050_INTLATCH_WAITCLEAR = const(0x01)

MPU6050_INTCLEAR_STATUSREAD = const(0x00)
MPU6050_INTCLEAR_ANYREAD = const(0x01)

MPU6050_INTERRUPT_FF_BIT = const(7)
MPU6050_INTERRUPT_MOT_BIT = const(6)
MPU6050_INTERRUPT_ZMOT_BIT = const(5)
MPU6050_INTERRUPT_FIFO_OFLOW_BIT = const(4)
MPU6050_INTERRUPT_I2C_MST_INT_BIT = const(3)
MPU6050_INTERRUPT_PLL_RDY_INT_BIT = const(2)
MPU6050_INTERRUPT_DMP_INT_BIT = const(1)
MPU6050_INTERRUPT_DATA_RDY_BIT = const(0)

# TODO: figure out what these actually do
# UMPL source code is not very obivous
MPU6050_DMPINT_5_BIT = const(5)
MPU6050_DMPINT_4_BIT = const(4)
MPU6050_DMPINT_3_BIT = const(3)
MPU6050_DMPINT_2_BIT = const(2)
MPU6050_DMPINT_1_BIT = const(1)
MPU6050_DMPINT_0_BIT = const(0)

MPU6050_MOTION_MOT_XNEG_BIT = const(7)
MPU6050_MOTION_MOT_XPOS_BIT = const(6)
MPU6050_MOTION_MOT_YNEG_BIT = const(5)
MPU6050_MOTION_MOT_YPOS_BIT = const(4)
MPU6050_MOTION_MOT_ZNEG_BIT = const(3)
MPU6050_MOTION_MOT_ZPOS_BIT = const(2)
MPU6050_MOTION_MOT_ZRMOT_BIT = const(0)

MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT = const(7)
MPU6050_DELAYCTRL_I2C_SLV4_DLY_EN_BIT = const(4)
MPU6050_DELAYCTRL_I2C_SLV3_DLY_EN_BIT = const(3)
MPU6050_DELAYCTRL_I2C_SLV2_DLY_EN_BIT = const(2)
MPU6050_DELAYCTRL_I2C_SLV1_DLY_EN_BIT = const(1)
MPU6050_DELAYCTRL_I2C_SLV0_DLY_EN_BIT = const(0)

MPU6050_PATHRESET_GYRO_RESET_BIT = const(2)
MPU6050_PATHRESET_ACCEL_RESET_BIT = const(1)
MPU6050_PATHRESET_TEMP_RESET_BIT = const(0)

MPU6050_DETECT_ACCEL_ON_DELAY_BIT = const(5)
MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH = const(2)
MPU6050_DETECT_FF_COUNT_BIT = const(3)
MPU6050_DETECT_FF_COUNT_LENGTH = const(2)
MPU6050_DETECT_MOT_COUNT_BIT = const(1)
MPU6050_DETECT_MOT_COUNT_LENGTH = const(2)

MPU6050_DETECT_DECREMENT_RESET = const(0x0)
MPU6050_DETECT_DECREMENT_1 = const(0x1)
MPU6050_DETECT_DECREMENT_2 = const(0x2)
MPU6050_DETECT_DECREMENT_4 = const(0x3)

MPU6050_USERCTRL_DMP_EN_BIT = const(7)
MPU6050_USERCTRL_FIFO_EN_BIT = const(6)
MPU6050_USERCTRL_I2C_MST_EN_BIT = const(5)
MPU6050_USERCTRL_I2C_IF_DIS_BIT = const(4)
MPU6050_USERCTRL_DMP_RESET_BIT = const(3)
MPU6050_USERCTRL_FIFO_RESET_BIT = const(2)
MPU6050_USERCTRL_I2C_MST_RESET_BIT = const(1)
MPU6050_USERCTRL_SIG_COND_RESET_BIT = const(0)

MPU6050_PWR1_DEVICE_RESET_BIT = const(7)
MPU6050_PWR1_SLEEP_BIT = const(6)
MPU6050_PWR1_CYCLE_BIT = const(5)
MPU6050_PWR1_TEMP_DIS_BIT = const(3)
MPU6050_PWR1_CLKSEL_BIT = const(2)
MPU6050_PWR1_CLKSEL_LENGTH = const(3)

MPU6050_CLOCK_INTERNAL = const(0x00)
MPU6050_CLOCK_PLL_XGYRO = const(0x01)
MPU6050_CLOCK_PLL_YGYRO = const(0x02)
MPU6050_CLOCK_PLL_ZGYRO = const(0x03)
MPU6050_CLOCK_PLL_EXT32K = const(0x04)
MPU6050_CLOCK_PLL_EXT19M = const(0x05)
MPU6050_CLOCK_KEEP_RESET = const(0x07)

MPU6050_PWR2_LP_WAKE_CTRL_BIT = const(7)
MPU6050_PWR2_LP_WAKE_CTRL_LENGTH = const(2)
MPU6050_PWR2_STBY_XA_BIT = const(5)
MPU6050_PWR2_STBY_YA_BIT = const(4)
MPU6050_PWR2_STBY_ZA_BIT = const(3)
MPU6050_PWR2_STBY_XG_BIT = const(2)
MPU6050_PWR2_STBY_YG_BIT = const(1)
MPU6050_PWR2_STBY_ZG_BIT = const(0)

MPU6050_WAKE_FREQ_1P25 = const(0x0)
MPU6050_WAKE_FREQ_2P5 = const(0x1)
MPU6050_WAKE_FREQ_5 = const(0x2)
MPU6050_WAKE_FREQ_10 = const(0x3)

MPU6050_BANKSEL_PRFTCH_EN_BIT = const(6)
MPU6050_BANKSEL_CFG_USER_BANK_BIT = const(5)
MPU6050_BANKSEL_MEM_SEL_BIT = const(4)
MPU6050_BANKSEL_MEM_SEL_LENGTH = const(5)

MPU6050_WHO_AM_I_BIT = const(6)
MPU6050_WHO_AM_I_LENGTH = const(6)

MPU6050_DMP_MEMORY_BANKS = const(8)
MPU6050_DMP_MEMORY_BANK_SIZE = const(256)
MPU6050_DMP_MEMORY_CHUNK_SIZE = const(16)


class MPU6050:
    def __init__(self, driver=None) -> None:
        assert driver is not None, "No found driver class"
        self.driver = driver

    def testConnection(self):
        return self.getDeviceId() == 0x34

    def initialize(self):
        pass

    def getAuxVDDIOLevel(self):
        """
        Get the auxiliary I2C supply voltage level.
        @return I2C supply voltage level (0=VLOGIC, 1=VDD)
        """
        data = self.driver.readBit(
            MPU6050_RA_YG_OFFS_TC, MPU6050_TC_PWR_MODE_BIT)
        return data

    def setAuxVDDIOLevel(self, level):
        """
        Set the auxiliary I2C supply voltage level.
        @param level I2C supply voltage level (0=VLOGIC, 1=VDD)
        """
        self.driver.writeBit(MPU6050_RA_YG_OFFS_TC,
                             MPU6050_TC_PWR_MODE_BIT, level)

    def getRate(self):
        """
        Get gyroscope output rate divider.
        @return Current sample rate
        """
        return self.driver.readByte(MPU6050_RA_SMPLRT_DIV)

    def setRate(self, rate):
        """
        Set gyroscope sample rate divider.
        @param rate New sample rate divider
        """
        self.driver.writeByte(MPU6050_RA_SMPLRT_DIV, rate)

    def getExternalFrameSync(self):
        """
        Get external FSYNC configuration.
        @return FSYNC configuration value
        """
        return self.driver.readBits(
            MPU6050_RA_CONFIG, MPU6050_CFG_EXT_SYNC_SET_BIT, MPU6050_CFG_EXT_SYNC_SET_LENGTH)

    def setExternalFrameSync(self, sync):
        """
        Set external FSYNC configuration.
        @param sync New FSYNC configuration value
        """
        self.driver.writeBits(
            MPU6050_RA_CONFIG, MPU6050_CFG_EXT_SYNC_SET_BIT, MPU6050_CFG_EXT_SYNC_SET_LENGTH, sync)

    def getDLPFMode(self):
        """
        Get digital low-pass filter configuration.
        @return DLFP configuration
        """
        return self.driver.readBits(MPU6050_RA_CONFIG, MPU6050_CFG_DLPF_CFG_BIT, MPU6050_CFG_DLPF_CFG_LENGTH)

    def setDLPFMode(self, mode):
        """
        Set digital low-pass filter configuration.
        @param mode New DLFP configuration setting
        """
        self.driver.writeBits(
            MPU6050_RA_CONFIG, MPU6050_CFG_DLPF_CFG_BIT, MPU6050_CFG_DLPF_CFG_LENGTH, mode)

    def getFullScaleGyroRange(self):
        """
        Get full-scale gyroscope range.
        @return Current full-scale gyroscope range setting
        """
        return self.driver.readBits(MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH)

    def setFullScaleGyroRange(self, range):
        """
        Set full-scale gyroscope range.
        @param range New full-scale gyroscope range value
        """
        self.driver.writeBits(
            MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, range)

    def getAccelXSelfTestFactoryTrim(self):
        """
        Get self-test factory trim value for accelerometer X axis.
        @return factory trim value
        """
        buffer = bytearray(2)
        buffer[0] = self.driver.readByte(MPU6050_RA_SELF_TEST_X)
        buffer[1] = self.driver.readByte(MPU6050_RA_SELF_TEST_A)
        return (buffer[0] >> 3) | ((buffer[1] >> 4) & 0x03)

    def getAccelYSelfTestFactoryTrim(self):
        """
        Get self-test factory trim value for accelerometer Y axis.
        @return factory trim value
        """
        buffer = bytearray(2)
        buffer[0] = self.driver.readByte(MPU6050_RA_SELF_TEST_Y)
        buffer[1] = self.driver.readByte(MPU6050_RA_SELF_TEST_A)
        return (buffer[0] >> 3) | ((buffer[1] >> 2) & 0x03)

    def getAccelYSelfTestFactoryTrim(self):
        """
        Get self-test factory trim value for accelerometer Z axis.
        @return factory trim value
        """
        buffer = self.driver.readBytes(MPU6050_RA_SELF_TEST_Z, 2)
        return (buffer[0] >> 3) | ((buffer[1]) & 0x03)

    def getGyroXSelfTestFactoryTrim(self):
        """
        Get self-test factory trim value for gyro X axis.
        @return factory trim value
        """
        b = self.driver.readByte(MPU6050_RA_SELF_TEST_X)
        return b & 0x1F

    def getGyroYSelfTestFactoryTrim(self):
        """
        Get self-test factory trim value for gyro Y axis.
        @return factory trim value
        """
        b = self.driver.readByte(MPU6050_RA_SELF_TEST_Y)
        return b & 0x1F

    def getGyroZSelfTestFactoryTrim(self):
        """
        Get self-test factory trim value for gyro Z axis.
        @return factory trim value
        """
        b = self.driver.readByte(MPU6050_RA_SELF_TEST_Z)
        return b & 0x1F

    def getAccelXSelfTest(self):
        return self.driver.readBit(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_XA_ST_BIT)

    def setAccelXSelfTest(self, enabled):
        self.driver.writeBit(MPU6050_RA_ACCEL_CONFIG,
                             MPU6050_ACONFIG_XA_ST_BIT, enabled)

    def getAccelYSelfTest(self):
        return self.driver.readBit(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_YA_ST_BIT)

    def setAccelYSelfTest(self, enabled):
        self.driver.writeBit(MPU6050_RA_ACCEL_CONFIG,
                             MPU6050_ACONFIG_YA_ST_BIT, enabled)

    def getAccelZSelfTest(self):
        return self.driver.readBit(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_ZA_ST_BIT)

    def setAccelZSelfTest(self, enabled):
        self.driver.writeBit(MPU6050_RA_ACCEL_CONFIG,
                             MPU6050_ACONFIG_ZA_ST_BIT, enabled)

    def getFullScaleAccelRange(self):
        """
        Get full-scale accelerometer range.
        @return Current full-scale accelerometer range setting
        """
        return self.driver.readBits(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH)

    def setFullScaleAccelRange(self, range):
        """
        Set full-scale accelerometer range.
        @param range New full-scale accelerometer range setting
        """
        self.driver.writeBits(
            MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, range)

    def getDHPFMode(self):
        """
        Get the high-pass filter configuration.
        @return Current high-pass filter configuration
        """
        return self.driver.readBits(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_ACCEL_HPF_BIT, MPU6050_ACONFIG_ACCEL_HPF_LENGTH)

    def setDHPFMode(self, bandwidth):
        """
        Set the high-pass filter configuration.
        @param bandwidth New high-pass filter configuration
        """
        self.driver.writeBits(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_ACCEL_HPF_BIT,
                              MPU6050_ACONFIG_ACCEL_HPF_LENGTH, bandwidth)

    def getFreefallDetectionThreshold(self):
        """
        Get free-fall event acceleration threshold.
        @return Current free-fall acceleration threshold value (LSB = 2mg)
        """
        return self.driver.readByte(MPU6050_RA_FF_THR)

    def setFreefallDetectionThreshold(self, threshold):
        """
        Set free-fall event acceleration threshold.
        @param threshold New free-fall acceleration threshold value (LSB = 2mg)
        """
        self.driver.writeByte(MPU6050_RA_FF_THR, threshold)

    def getFreefallDetectionDuration(self):
        """
        Get free-fall event duration threshold.
        @return Current free-fall duration threshold value (LSB = 1ms)
        """
        return self.driver.readByte(MPU6050_RA_FF_DUR)

    def setFreefallDetectionDuration(self, duration):
        """
        Set free-fall event duration threshold.
        @param duration New free-fall duration threshold value (LSB = 1ms)
        """
        self.driver.writeByte(MPU6050_RA_FF_DUR, duration)

    def getMotionDetectionThreshold(self):
        """
        Get motion detection event acceleration threshold.
        @return Current motion detection acceleration threshold value (LSB = 2mg)
        """
        return self.driver.readByte(MPU6050_RA_MOT_THR)

    def setMotionDetectionThreshold(self, threshold):
        """
        Set motion detection event acceleration threshold.
        @param threshold New motion detection acceleration threshold value (LSB = 2mg)
        """
        self.driver.writeByte(MPU6050_RA_MOT_THR, threshold)

    def getMotionDetectionDuration(self):
        """
        Get motion detection event duration threshold.
        @return Current motion detection duration threshold value (LSB = 1ms)
        """
        return self.driver.readByte(MPU6050_RA_MOT_DUR)

    def setMotionDetectionDuration(self, duration):
        """
        Set motion detection event duration threshold.
        @param duration New motion detection duration threshold value (LSB = 1ms)
        """
        self.driver.writeByte(MPU6050_RA_MOT_DUR, duration)

    def getZeroMotionDetectionThreshold(self):
        """
        Get zero motion detection event acceleration threshold.
        @return Current zero motion detection acceleration threshold value (LSB = 2mg)
        """
        return self.driver.readByte(MPU6050_RA_ZRMOT_THR)

    def setZeroMotionDetectionThreshold(self, threshold):
        """
        Set zero motion detection event acceleration threshold.
        @param threshold New zero motion detection acceleration threshold value (LSB = 2mg)
        """
        self.driver.writeByte(MPU6050_RA_ZRMOT_THR, threshold)

    def getZeroMotionDetectionDuration(self):
        """
        Get zero motion detection event duration threshold.
        @return Current zero motion detection duration threshold value (LSB = 64ms)
        """
        return self.driver.readByte(MPU6050_RA_ZRMOT_DUR)

    def setZeroMotionDetectionDuration(self, duration):
        """
        Set zero motion detection event duration threshold.
        @param duration New zero motion detection duration threshold value (LSB = 1ms)
        """
        self.driver.writeByte(MPU6050_RA_ZRMOT_DUR, duration)

    def getTemperatureFIFOEnabled(self):
        """
        Get temperature FIFO enabled value.
        @return Current temperature FIFO enabled value
        """
        return self.driver.readBit(MPU6050_RA_FIFO_EN, MPU6050_TEMP_FIFO_EN_BIT)

    def setTemperatureFIFOEnabled(self, enabled):
        """
        Set temperature FIFO enabled value.
        @param enabled New temperature FIFO enabled value
        """
        self.driver.writeBit(MPU6050_RA_FIFO_EN,
                             MPU6050_TEMP_FIFO_EN_BIT, enabled)

    def getXGyroFIFOEnabled(self):
        """
        Get gyroscope X-axis FIFO enabled value.
        @return Current gyroscope X-axis FIFO enabled value
        """
        return self.driver.readBit(MPU6050_RA_FIFO_EN, MPU6050_XG_FIFO_EN_BIT)

    def setXGyroFIFOEnabled(self, enabled):
        """
        Set gyroscope X-axis FIFO enabled value.
        @param enabled New gyroscope X-axis FIFO enabled value
        """
        self.driver.writeBit(MPU6050_RA_FIFO_EN,
                             MPU6050_XG_FIFO_EN_BIT, enabled)

    def getYGyroFIFOEnabled(self):
        """
        Get gyroscope Y-axis FIFO enabled value.
        @return Current gyroscope Y-axis FIFO enabled value
        """
        return self.driver.readBit(MPU6050_RA_FIFO_EN, MPU6050_YG_FIFO_EN_BIT)

    def setYGyroFIFOEnabled(self, enabled):
        """
        Set gyroscope Y-axis FIFO enabled value.
        @param enabled New gyroscope Y-axis FIFO enabled value
        """
        self.driver.writeBit(MPU6050_RA_FIFO_EN,
                             MPU6050_YG_FIFO_EN_BIT, enabled)

    def getZGyroFIFOEnabled(self):
        """
        Get gyroscope Z-axis FIFO enabled value.
        @return Current gyroscope Z-axis FIFO enabled value
        """
        return self.driver.readBit(MPU6050_RA_FIFO_EN, MPU6050_ZG_FIFO_EN_BIT)

    def setZGyroFIFOEnabled(self, enabled):
        """
        Set gyroscope Z-axis FIFO enabled value.
        @param enabled New gyroscope Z-axis FIFO enabled value
        """
        self.driver.writeBit(MPU6050_RA_FIFO_EN,
                             MPU6050_ZG_FIFO_EN_BIT, enabled)

    def getAccelFIFOEnabled(self):
        """
        Get accelerometer FIFO enabled value.
        @return Current accelerometer FIFO enabled value
        """
        return self.driver.readBit(MPU6050_RA_FIFO_EN, MPU6050_ACCEL_FIFO_EN_BIT)

    def setAccelFIFOEnabled(self, enabled):
        """
        Set accelerometer FIFO enabled value.
        @param enabled New accelerometer FIFO enabled value
        """
        self.driver.writeBit(MPU6050_RA_FIFO_EN,
                             MPU6050_ACCEL_FIFO_EN_BIT, enabled)

    def getPassthroughStatus(self):
        """
        Get FSYNC interrupt status.
        @return FSYNC interrupt status
        """
        return self.driver.readBit(MPU6050_RA_I2C_MST_STATUS, MPU6050_MST_PASS_THROUGH_BIT)

    def getInterruptMode(self):
        """
        Get interrupt logic level mode.
        @return Current interrupt mode (0=active-high, 1=active-low)
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG,
                                   MPU6050_INTCFG_INT_LEVEL_BIT)

    def setInterruptMode(self, mode):
        """
        Set interrupt logic level mode.
        @param mode New interrupt mode (0=active-high, 1=active-low)
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_INT_LEVEL_BIT, mode)

    def getInterruptDrive(self):
        """
        Get interrupt drive mode.
        @return Current interrupt drive mode (0=push-pull, 1=open-drain)
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_INT_OPEN_BIT)

    def setInterruptDrive(self, drive):
        """
        Set interrupt drive mode.
        @param drive New interrupt drive mode (0=push-pull, 1=open-drain)
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_INT_OPEN_BIT, drive)

    def getInterruptLatch(self):
        """
        Get interrupt latch mode.
        @return Current latch mode (0=50us-pulse, 1=latch-until-int-cleared)
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_LATCH_INT_EN_BIT)

    def setInterruptLatch(self, latch):
        """
        Set interrupt latch mode.
        @param latch New latch mode (0=50us-pulse, 1=latch-until-int-cleared)
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_LATCH_INT_EN_BIT, latch)

    def getInterruptLatchClear(self):
        """
        Get interrupt latch clear mode.
        @return Current latch clear mode (0=status-read-only, 1=any-register-read)
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_INT_RD_CLEAR_BIT)

    def setInterruptLatchClear(self, clear):
        """
        Set interrupt latch clear mode.
        @param clear New latch clear mode (0=status-read-only, 1=any-register-read)
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_INT_RD_CLEAR_BIT, clear)

    def getFSyncInterruptLevel(self):
        """
        Get FSYNC interrupt logic level mode.
        @return Current FSYNC interrupt mode (0=active-high, 1=active-low)
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT)

    def setFSyncInterruptLevel(self, level):
        """
        Set FSYNC interrupt logic level mode.
        @param mode New FSYNC interrupt mode (0=active-high, 1=active-low)
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT, level)

    def getFSyncInterruptEnabled(self):
        """
        Get FSYNC pin interrupt enabled setting.
        @return Current interrupt enabled setting
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_FSYNC_INT_EN_BIT)

    def setFSyncInterruptEnabled(self, enabled):
        """
        Set FSYNC pin interrupt enabled setting.
        @param enabled New FSYNC pin interrupt enabled setting
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_FSYNC_INT_EN_BIT, enabled)

    def getI2CBypassEnabled(self):
        """
        Get I2C bypass enabled status.
        @return Current I2C bypass enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_I2C_BYPASS_EN_BIT)

    def setI2CBypassEnabled(self, enabled):
        """
        Set I2C bypass enabled status.
        @param enabled New I2C bypass enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_I2C_BYPASS_EN_BIT, enabled)

    def getClockOutputEnabled(self):
        """
        Get reference clock output enabled status.
        @return Current reference clock output enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_PIN_CFG, MPU6050_INTCFG_CLKOUT_EN_BIT)

    def setClockOutputEnabled(self, enabled):
        """
        Set reference clock output enabled status.
        @param enabled New reference clock output enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_PIN_CFG,
                             MPU6050_INTCFG_CLKOUT_EN_BIT, enabled)

    def getIntEnabled(self):
        """
        Get full interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readByte(MPU6050_RA_INT_ENABLE)

    def setIntEnabled(self, enabled):
        """
        Set full interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeByte(MPU6050_RA_INT_ENABLE, enabled)

    def getIntFreefallEnabled(self):
        """
        Get Free Fall interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_FF_BIT)

    def setIntFreefallEnabled(self, enabled):
        """
        Set Free Fall interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_ENABLE,
                             MPU6050_INTERRUPT_FF_BIT, enabled)

    def getIntMotionEnabled(self):
        """
        Get Motion Detection interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_MOT_BIT)

    def setIntMotionEnabled(self, enabled):
        """
        Set Motion Detection interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_ENABLE,
                             MPU6050_INTERRUPT_MOT_BIT, enabled)

    def getIntZeroMotionEnabled(self):
        """
        Get Zero Motion Detection interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_ZMOT_BIT)

    def setIntZeroMotionEnabled(self, enabled):
        """
        Set Zero Motion Detection interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_ENABLE,
                             MPU6050_INTERRUPT_ZMOT_BIT, enabled)

    def getIntFIFOBufferOverflowEnabled(self):
        """
        Get FIFO Buffer Overflow interrupt enabled status.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_FIFO_OFLOW_BIT)

    def setIntFIFOBufferOverflowEnabled(self, enabled):
        """
        Set FIFO Buffer Overflow interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_ENABLE,
                             MPU6050_INTERRUPT_FIFO_OFLOW_BIT, enabled)

    def getIntDataReadyEnabled(self):
        """
        Get Data Ready interrupt enabled setting.
        @return Current interrupt enabled status
        """
        return self.driver.readBit(MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_DATA_RDY_BIT)

    def setIntDataReadyEnabled(self, enabled):
        """
        Set Data Ready interrupt enabled status.
        @param enabled New interrupt enabled status
        """
        self.driver.writeBit(MPU6050_RA_INT_ENABLE,
                             MPU6050_INTERRUPT_DATA_RDY_BIT, enabled)

    def getIntStatus(self):
        """
        Get full set of interrupt status bits.
        @return Current interrupt status
        """
        return self.driver.readByte(MPU6050_RA_INT_STATUS)

    def getIntFreefallStatus(self):
        """
        Get Free Fall interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_FF_BIT)

    def getIntMotionStatus(self):
        """
        Get Motion Detection interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_MOT_BIT)

    def getIntZeroMotionStatus(self):
        """
        Get Zero Motion Detection interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_ZMOT_BIT)

    def getIntFIFOBufferOverflowStatus(self):
        """
        Get FIFO Buffer Overflow interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_FIFO_OFLOW_BIT)

    def getIntDataReadyStatus(self):
        """
        Get Data Ready interrupt status.
        @return Current interrupt status
        """
        return self.driver.readBit(MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_DATA_RDY_BIT)

    def getMotion9(self):
        """
        Get raw 9-axis motion sensor readings (accel/gyro/compass).
        @return A new tuple, include: ax, ay, az, gx, gy, gz, mx, my, mz
        """
        ax, ay, az, gx, gy, gz = self.getMotion6()
        return (ax, ay, az, gx, gy, gz, 0, 0, 0)

    def getMotion6(self):
        """
        Get raw 6-axis motion sensor readings (accel/gyro).
        @return A new tuple, include: ax, ay, az, gx, gy, gz
        """
        buffer = self.driver.readBytes(MPU6050_RA_ACCEL_XOUT_H, 14)
        ax = (buffer[0] << 8) | buffer[1]
        ay = (buffer[2] << 8) | buffer[3]
        az = (buffer[4] << 8) | buffer[5]
        # skip temperature
        gx = (buffer[8] << 8) | buffer[9]
        gy = (buffer[10] << 8) | buffer[11]
        gz = (buffer[12] << 8) | buffer[13]
        return (ax, ay, az, gx, gy, gz)

    def getAcceleration(self):
        """
        Get 3-axis accelerometer readings.
        @return A new tuple, include: ax, ay, az
        """
        buffer = self.driver.readBytes(MPU6050_RA_ACCEL_XOUT_H, 6)
        ax = (buffer[0] << 8) | buffer[1]
        ay = (buffer[2] << 8) | buffer[3]
        az = (buffer[4] << 8) | buffer[5]
        return (ax, ay, az)

    def getAccelerationX(self):
        """
        Get X-axis accelerometer reading.
        @return X-axis acceleration measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_ACCEL_XOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getAccelerationY(self):
        """
        Get Y-axis accelerometer reading.
        @return Y-axis acceleration measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_ACCEL_YOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getAccelerationZ(self):
        """
        Get Z-axis accelerometer reading.
        @return Z-axis acceleration measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_ACCEL_ZOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getTemperature(self):
        """
        Get current internal temperature.
        @return Temperature reading in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_TEMP_OUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getRotation(self):
        """
        Get 3-axis gyroscope readings.
        @return A new tuple, include: x, y, z
        """
        buffer = self.driver.readBytes(MPU6050_RA_GYRO_XOUT_H, 6)
        x = (buffer[0] << 8) | buffer[1]
        y = (buffer[2] << 8) | buffer[3]
        z = (buffer[4] << 8) | buffer[5]
        return (x, y, z)

    def getRotationX(self):
        """
        Get X-axis gyroscope reading.
        @return X-axis rotation measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_GYRO_XOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getRotationY(self):
        """
        Get Y-axis gyroscope reading.
        @return Y-axis rotation measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_GYRO_YOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getRotationZ(self):
        """
        Get Z-axis gyroscope reading.
        @return Z-axis rotation measurement in 16-bit 2's complement format
        """
        buffer = self.driver.readBytes(MPU6050_RA_GYRO_ZOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getMotionStatus(self):
        """
        Get full motion detection status register content (all bits).
        @return Motion detection status byte
        """
        return self.driver.readByte(MPU6050_RA_MOT_DETECT_STATUS)

    def getXNegMotionDetected(self):
        """
        Get X-axis negative motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_XNEG_BIT)

    def getXPosMotionDetected(self):
        """
        Get X-axis positive motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_XPOS_BIT)

    def getYNegMotionDetected(self):
        """
        Get Y-axis negative motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_YNEG_BIT)

    def getYPosMotionDetected(self):
        """
        Get Y-axis positive motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_YPOS_BIT)

    def getZNegMotionDetected(self):
        """
        Get Z-axis negative motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_ZNEG_BIT)

    def getZPosMotionDetected(self):
        """
        Get Z-axis positive motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_ZPOS_BIT)

    def getZeroMotionDetected(self):
        """
        Get zero motion detection interrupt status.
        @return Motion detection status
        """
        return self.driver.readBit(MPU6050_RA_MOT_DETECT_STATUS, MPU6050_MOTION_MOT_ZRMOT_BIT)

    def resetGyroscopePath(self):
        """
        Reset gyroscope signal path.
        """
        self.driver.writeBit(MPU6050_RA_SIGNAL_PATH_RESET,
                             MPU6050_PATHRESET_GYRO_RESET_BIT, True)

    def resetAccelerometerPath(self):
        """
        Reset accelerometer signal path.
        """
        self.driver.writeBit(MPU6050_RA_SIGNAL_PATH_RESET,
                             MPU6050_PATHRESET_ACCEL_RESET_BIT, True)

    def resetTemperaturePath(self):
        """
        Reset temperature sensor signal path.
        """
        self.driver.writeBit(MPU6050_RA_SIGNAL_PATH_RESET,
                             MPU6050_PATHRESET_TEMP_RESET_BIT, True)

    def getAccelerometerPowerOnDelay(self):
        """
        Get accelerometer power-on delay.
        @return Current accelerometer power-on delay
        """
        return self.driver.readBits(MPU6050_RA_MOT_DETECT_CTRL, MPU6050_DETECT_ACCEL_ON_DELAY_BIT, MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH)

    def setAccelerometerPowerOnDelay(self, delay):
        """
        Set accelerometer power-on delay.
        @param delay New accelerometer power-on delay (0-3)
        """
        self.driver.writeBits(MPU6050_RA_MOT_DETECT_CTRL, MPU6050_DETECT_ACCEL_ON_DELAY_BIT,
                              MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH, delay)

    def getFreefallDetectionCounterDecrement(self):
        """
        Get Free Fall detection counter decrement configuration.
        @return Current decrement configuration
        """
        return self.driver.readBits(MPU6050_RA_MOT_DETECT_CTRL, MPU6050_DETECT_FF_COUNT_BIT, MPU6050_DETECT_FF_COUNT_LENGTH)

    def setFreefallDetectionCounterDecrement(self, decrement):
        """
        Set Free Fall detection counter decrement configuration.
        @param decrement New decrement configuration value
        """
        self.driver.writeBits(MPU6050_RA_MOT_DETECT_CTRL, MPU6050_DETECT_FF_COUNT_BIT,
                              MPU6050_DETECT_FF_COUNT_LENGTH, decrement)

    def getMotionDetectionCounterDecrement(self):
        """
        Get Motion detection counter decrement configuration.
        """
        return self.driver.readBits(MPU6050_RA_MOT_DETECT_CTRL, MPU6050_DETECT_MOT_COUNT_BIT, MPU6050_DETECT_MOT_COUNT_LENGTH)

    def setMotionDetectionCounterDecrement(self, decrement):
        """
        Set Motion detection counter decrement configuration.
        @param decrement New decrement configuration value
        """
        self.driver.writeBits(MPU6050_RA_MOT_DETECT_CTRL, MPU6050_DETECT_MOT_COUNT_BIT,
                              MPU6050_DETECT_MOT_COUNT_LENGTH, decrement)

    def getFIFOEnabled(self):
        """
        Get FIFO enabled status.
        @return Current FIFO enabled status
        """
        return self.driver.readBit(MPU6050_RA_USER_CTRL, MPU6050_USERCTRL_FIFO_EN_BIT)

    def setFIFOEnabled(self, enabled):
        """
        Set FIFO enabled status.
        @param enabled New FIFO enabled status
        """
        self.driver.writeBit(MPU6050_RA_USER_CTRL,
                             MPU6050_USERCTRL_FIFO_EN_BIT, enabled)

    def resetFIFO(self):
        """
        Reset the FIFO.
        """
        self.driver.writeBit(MPU6050_RA_USER_CTRL,
                             MPU6050_USERCTRL_FIFO_RESET_BIT, True)

    def resetSensors(self):
        """
        Reset all sensor registers and signal paths.
        """
        self.driver.writeBit(MPU6050_RA_USER_CTRL,
                             MPU6050_USERCTRL_SIG_COND_RESET_BIT, True)

    def reset(self):
        """
        Trigger a full device reset.
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_1,
                             MPU6050_PWR1_DEVICE_RESET_BIT, True)

    def getSleepEnabled(self):
        """
        Get sleep mode status.
        @return Current sleep mode enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_SLEEP_BIT)

    def setSleepEnabled(self, enabled):
        """
        Set sleep mode status.
        @param enabled New sleep mode enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_1,
                             MPU6050_PWR1_SLEEP_BIT, enabled)

    def getWakeCycleEnabled(self):
        """
        Get wake cycle enabled status.
        @return Current sleep mode enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_CYCLE_BIT)

    def setWakeCycleEnabled(self, enabled):
        """
        Set wake cycle enabled status.
        @param enabled New sleep mode enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_1,
                             MPU6050_PWR1_CYCLE_BIT, enabled)

    def getTemperatureSensorEnabled(self):
        """
        Get temperature sensor enabled status.
        @return Current temperature sensor enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_TEMP_DIS_BIT)

    def setTemperatureSensorEnabled(self, enabled):
        """
        Set temperature sensor enabled status.
        @param enabled New temperature sensor enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_1,
                             MPU6050_PWR1_TEMP_DIS_BIT, not enabled)

    def getClockSource(self):
        """
        Get clock source setting.
        @return Current clock source setting
        """
        return self.driver.readBits(MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_CLKSEL_BIT, MPU6050_PWR1_CLKSEL_LENGTH)

    def setClockSource(self, source):
        """
        Set clock source setting.
        @param source New clock source setting
        """
        self.driver.writeBits(
            MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_CLKSEL_BIT, MPU6050_PWR1_CLKSEL_LENGTH, source)

    def getWakeFrequency(self):
        """
        Get wake frequency in Accel-Only Low Power Mode.
        @return Current wake frequency
        """
        return self.driver.readBits(
            MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_LP_WAKE_CTRL_BIT, MPU6050_PWR2_LP_WAKE_CTRL_LENGTH)

    def setWakeFrequency(self, frequency):
        """
        Set wake frequency in Accel-Only Low Power Mode.
        @param frequency New wake frequency
        """
        self.driver.writeBits(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_LP_WAKE_CTRL_BIT,
                              MPU6050_PWR2_LP_WAKE_CTRL_LENGTH, frequency)

    def getStandbyXAccelEnabled(self):
        """
        Get X-axis accelerometer standby enabled status.
        @return Current X-axis standby enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_STBY_XA_BIT)

    def setStandbyXAccelEnabled(self, enabled):
        """
        Set X-axis accelerometer standby enabled status.
        @param New X-axis standby enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_2,
                             MPU6050_PWR2_STBY_XA_BIT, enabled)

    def getStandbyYAccelEnabled(self):
        """
        Get Y-axis accelerometer standby enabled status.
        @return Current Y-axis standby enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_STBY_YA_BIT)

    def setStandbyYAccelEnabled(self, enabled):
        """
        Set Y-axis accelerometer standby enabled status.
        @param New Y-axis standby enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_2,
                             MPU6050_PWR2_STBY_YA_BIT, enabled)

    def getStandbyZAccelEnabled(self):
        """
        Get Z-axis accelerometer standby enabled status.
        @return Current Z-axis standby enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_STBY_ZA_BIT)

    def setStandbyZAccelEnabled(self, enabled):
        """
        Set Z-axis accelerometer standby enabled status.
        @param New Z-axis standby enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_2,
                             MPU6050_PWR2_STBY_ZA_BIT, enabled)

    def getStandbyXGyroEnabled(self):
        """
        Get X-axis gyroscope standby enabled status.
        @return Current X-axis standby enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_STBY_XG_BIT)

    def setStandbyXGyroEnabled(self, enabled):
        """
        Set X-axis gyroscope standby enabled status.
        @param New X-axis standby enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_2,
                             MPU6050_PWR2_STBY_XG_BIT, enabled)

    def getStandbyYGyroEnabled(self):
        """
        Get Y-axis gyroscope standby enabled status.
        @return Current Y-axis standby enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_STBY_YG_BIT)

    def setStandbyYGyroEnabled(self, enabled):
        """
        Set Y-axis gyroscope standby enabled status.
        @param New Y-axis standby enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_2,
                             MPU6050_PWR2_STBY_YG_BIT, enabled)

    def getStandbyZGyroEnabled(self):
        """
        Get Z-axis gyroscope standby enabled status.
        @return Current Z-axis standby enabled status
        """
        return self.driver.readBit(MPU6050_RA_PWR_MGMT_2, MPU6050_PWR2_STBY_ZG_BIT)

    def setStandbyZGyroEnabled(self, enabled):
        """
        Set Z-axis gyroscope standby enabled status.
        @param New Z-axis standby enabled status
        """
        self.driver.writeBit(MPU6050_RA_PWR_MGMT_2,
                             MPU6050_PWR2_STBY_ZG_BIT, enabled)

    def getFIFOCount(self):
        """
        Get current FIFO buffer size.
        @return Current FIFO buffer size
        """
        buffer = self.driver.readBytes(MPU6050_RA_FIFO_COUNTH, 2)
        return (buffer[0] << 8) | buffer[1]

    def getFIFOByte(self):
        """
        Get byte from FIFO buffer.
        @return Byte from FIFO buffer
        """
        return self.driver.readByte(MPU6050_RA_FIFO_R_W)

    def getFIFOBytes(self, length):
        return self.driver.readBytes(MPU6050_RA_FIFO_R_W, length) if length > 0 else bytearray(0)

    """
    /** Get latest byte from FIFO buffer no matter how much time has passed.
    * ===                  GetCurrentFIFOPacket                    ===
    * ================================================================
    * Returns 1) when nothing special was done
    *         2) when recovering from overflow
    *         0) when no valid data is available
    * ================================================================ */
    int8_t MPU6050::GetCurrentFIFOPacket(uint8_t *data, uint8_t length)
    { // overflow proof
        int16_t fifoC;
        // This section of code is for when we allowed more than 1 packet to be acquired
        // uint32_t BreakTimer = micros();
        uint32_t BreakTimer = time_us_32();
        do
        {
            if ((fifoC = getFIFOCount()) > length)
            {

                if (fifoC > 200)
                {                // if you waited to get the FIFO buffer to > 200 bytes it will take longer to get the last packet in the FIFO Buffer than it will take to  reset the buffer and wait for the next to arrive
                    resetFIFO(); // Fixes any overflow corruption
                    fifoC = 0;
                    while (!(fifoC = getFIFOCount()) && ((time_us_32() - BreakTimer) <= (11000)))
                        ; // Get Next New Packet
                }
                else
                { // We have more than 1 packet but less than 200 bytes of data in the FIFO Buffer
                    uint8_t Trash[BUFFER_LENGTH];
                    while ((fifoC = getFIFOCount()) > length)
                    {                           // Test each time just in case the MPU is writing to the FIFO Buffer
                        fifoC = fifoC - length; // Save the last packet
                        uint16_t RemoveBytes;
                        while (fifoC)
                        {                                                 // fifo count will reach zero so this is safe
                            RemoveBytes = MIN((int)fifoC, BUFFER_LENGTH); // Buffer Length is different than the packet length this will efficiently clear the buffer
                            getFIFOBytes(Trash, (uint8_t)RemoveBytes);
                            fifoC -= RemoveBytes;
                        }
                    }
                }
            }
            if (!fifoC)
                return 0; // Called too early no data or we timed out after FIFO Reset
            // We have 1 packet
            if ((time_us_32() - BreakTimer) > (11000))
                return 0;
        } while (fifoC != length);
        getFIFOBytes(data, length); // Get 1 packet
        return 1;
    }
    """

    def setFIFOByte(self, data):
        """
        Write byte to FIFO buffer.
        """
        self.driver.writeByte(MPU6050_RA_FIFO_R_W, data)

    def getDeviceId(self):
        """
        Get Device ID.
        @return Device ID (6 bits only! should be 0x34)
        """
        return self.driver.readBits(MPU6050_RA_WHO_AM_I, MPU6050_WHO_AM_I_BIT, MPU6050_WHO_AM_I_LENGTH)

    def setDeviceId(self, id):
        """
        Set Device ID.
        @param id New device ID to set.
        """
        self.driver.writeBits(
            MPU6050_RA_WHO_AM_I, MPU6050_WHO_AM_I_BIT, MPU6050_WHO_AM_I_LENGTH, id)
