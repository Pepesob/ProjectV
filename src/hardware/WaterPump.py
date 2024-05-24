from machine import Pin

class WaterPump:

    def __init__(self, gpio_num):
        self.gpio_num = gpio_num
        self.gpio_pin = Pin(self.gpio_num, Pin.OUT)
    
    def start(self):
        self.gpio_pin.on()
        print("Water pump on")

    def stop(self):
        self.gpio_pin.off()
        print("Water pump off")