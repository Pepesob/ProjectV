from machine import Pin

class Led:

    def __init__(self) -> None:
        self.led_pin = Pin("LED", Pin.OUT)

    def on(self):
        self.led_pin.on()
        print("On LED")

    def off(self):
        self.led_pin.off()
        print("Off LED")