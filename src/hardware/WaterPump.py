from machine import Pin

class WaterPump:

    def __init__(self, gpio_num, operate=True):
        self.gpio_num = gpio_num
        self.gpio_pin = Pin(self.gpio_num, Pin.OUT, value=1)
        self.operate = operate
    
    def start(self):
        print("Water pump on")
        if not self.operate: return
        self.gpio_pin.value(0)
        

    def stop(self):
        print("Water pump off")
        if not self.operate: return
        self.gpio_pin.value(1)
        