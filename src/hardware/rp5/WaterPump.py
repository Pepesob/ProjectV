import gpiozero
import time

class WaterPump:

    def __init__(self, gpio_num):
        self.gpio_num = gpio_num
        self.gpio_pin = gpiozero.LED(gpio_num)
    
    def start(self):
        self.gpio_pin.on()
        print("Water pump on")

    def stop(self):
        self.gpio_pin.off()
        print("Water pump off")

if __name__ == "__main__":
    ps = WaterPump(17)
    ps.start()
    time.sleep(17)
    ps.stop()