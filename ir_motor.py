from machine import Pin
import time
from ir import ir
from machine import Pin, PWM

#配置红外接收引脚
pin = Pin(5, Pin.IN, Pin.PULL_UP)

speed = 5
cacheSpeed = 5
# 初始化电机小风扇
fan = PWM(Pin(13))
fan.freq(1000) # 设置频率
#配置红外接收库
Ir = ir(pin)
# 数值重映射
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# 设置风扇的转速，speed=[0, 100]
def pwm_motor(speed):
    if speed > 100 or speed < 0:
        print('Please enter a limited speed value of 0-100 ')
        return
    pulse = my_map(speed, 0, 100, 0, 65535)
    fan.duty_u16(pulse)
    
while True:
    #读取遥控器数据
    value = Ir.Getir()
    if value != None:
        if value == 22:
            speed = 0
            pwm_motor(speed *10)
        elif value == 12:
            speed = 1
            pwm_motor(speed *10)
        elif value == 24:
            speed = 2
            pwm_motor(speed *10)
        elif value == 94:
            speed = 3
            pwm_motor(speed *10)
        elif value == 8:
            speed = 4
            pwm_motor(speed *10)
        elif value == 28:
            speed = 5
            pwm_motor(speed *10)
        elif value == 90:
            speed = 6
            pwm_motor(speed *10)
        elif value == 66:
            speed = 7
            pwm_motor(speed *10)
        elif value == 82:
            speed = 8
            pwm_motor(speed *10)
        elif value == 74:
            speed = 9
            pwm_motor(speed *10)
        elif value == 69:
            # 开关启停
            if speed == 0:
                speed = cacheSpeed
            else:
                cacheSpeed = speed
                speed = 0
            pwm_motor(speed *10)
        print(speed)
        pwm_motor(speed *10)




