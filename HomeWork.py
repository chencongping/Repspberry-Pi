from machine import Pin, I2C, PWM
from color import color
import utime
import ws2812b
import random

#####人体传感器
human = Pin(11, Pin.IN)
led = Pin(25, Pin.OUT)
def detect_someone():
    if human.value() == 1:
        return True
    return False

#####oled显示
i2c=I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)

# 打开主板自带的LED灯
def led_on():
    led.value(1)

# 关闭主板自带的LED灯
def led_off():
    led.value(0)

#####初始化电机小风扇

fan = PWM(Pin(13))

fan.freq(1000) # 设置频率

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

####color show
#i2c=I2C(0, scl=Pin(21),sda=Pin(20), freq=100000)
#i2c=I2C(1, scl=Pin(19),sda=Pin(18), freq=100000)

# 初始化颜色识别传感器
#Color = color(i2c)

ring_pin = 17 # 灯环的引脚
numpix   = 8  # RGB灯的数量
strip = ws2812b.ws2812b(numpix, 0, ring_pin)
strip.fill(0,0,0) # 清空RGB缓存
strip.show()      # 刷新显示

# 关闭所有灯
strip.fill(0,0,0)
strip.show()

utime.sleep(.1)

while True:
    if detect_someone() == True:
        led_on()
        print("human")
        oled.text('Welcome Home!', 0, 12)
        oled.show()
        pwm_motor(50)
        utime.sleep(10)
    else:
        led_off()
        print("nothing")
        pwm_motor(0)
        utime.sleep(3)
