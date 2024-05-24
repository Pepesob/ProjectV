from machine import Pin, PWM

class RotationPlate:

    def __init__(self, pwm_pin:int) -> None:
        self.freq = 20_000

        self.pwm_pin_num = pwm_pin
        self.gpio_pin = Pin(self.pwm_pin_num)
        self.pwm_pin = PWM(self.gpio_pin, freq=self.freq)
        
        self.pwm_pin.duty_u16(0)
    
    def set_duty_cycle(self, value):
        if not 0 <= value <= 100:
            print("Wrong duty cycle value!")
            return
        self.pwm_pin.duty_u16(int(0xFFFF * value / 100))
        print("Rotating to:", value)
    
    def get_duty_cycle(self):
        return 100 * self.pwm_pin.duty_u16() / 0xFFFF 