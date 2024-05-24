from machine import Pin, PWM

class RotationPlate:

    def __init__(self, pwm_pin:int) -> None:
        self.freq = 20_000
        self.duty_cycle = 0 # 0 % - 100 %

        self.pwm_pin_num = pwm_pin
        self.gpio_pin = Pin(self.pwm_pin_num)
        self.pwm_pin = PWM(self.gpio_pin, freq=self.freq, duty_u16=self.duty_cycle)
    
    def set_duty_cycle(self, value):
        if not 0 <= value <= 100:
            print("Wrong duty cycle value!")
            return
        self.duty_cycle = value
        self.pwm_pin.duty_u16(0xFFFF * self.duty_cycle)
        print("Rotating to:", value)