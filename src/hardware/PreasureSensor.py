from machine import Pin

class PreasureSensor:

    def __init__(self, gpio_in: int):
        self.gpio_in_num = gpio_in
        self.pin_in = Pin(self.gpio_in_num, Pin.IN, Pin.PULL_UP)

    def get_input(self):
        print("Preasure sensor read:", self.pin_in.value())
        return not self.pin_in.value()
    
    def update(self):
        # This function should check input and change output corespondingly; it will be run periodically in the loop
        pass