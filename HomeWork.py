from machine import Pin, I2C
import utime

#人体传感器
human = Pin(11, Pin.IN)
led = Pin(25, Pin.OUT)

abc = 0

#oled显示
i2c=I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)

# 打开主板自带的LED灯
def led_on():
    led.value(1)

# 关闭主板自带的LED灯
def led_off():
    led.value(0)


def detect_someone():
    if human.value() == 1:
        return True
    return False

while True:
    if detect_someone() == True:
        abc += 1
        led_on()
        print("human")
        oled.text('Welcome Home!', 0, 12)
        oled.show()
    #else:
        #led_off()
        #print("nothing")
        #utime.sleep(3)




