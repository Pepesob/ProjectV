from machine import Pin, PWM

class RotationPlate:

    def __init__(self, pwm_pin:int) -> None:
        self.freq = 50
        self.max_ms = 2.6
        self.min_ms = 0.41

        self.max_angle = 180

        self.current_angle = 0

        self.pwm_pin_num = pwm_pin
        self.gpio_pin = Pin(self.pwm_pin_num)
        self.pwm_pin = PWM(self.gpio_pin, freq=self.freq)
        
        self.set_angle(0)
    
    def set_angle(self, value):
        if not (0 <= value <= 180):
            print("Wrong duty cycle value!: " + str(value))
            return
        self.pwm_pin.duty_u16(self.ms_to_uint16(self.min_ms) + self.ms_to_uint16(self.angle_to_ms(value)))
        self.current_angle = value
        print("Uint value:", self.ms_to_uint16(self.min_ms) + self.ms_to_uint16(self.angle_to_ms(value)))
        print("Rotating to:", value)
    
    def get_duty_cycle(self):
        return 100 * self.pwm_pin.duty_u16() / 0xFFFF

    def get_angle(self):
        return self.current_angle
    def angle_to_ms(self, angle):
        return self.min_ms + ((self.max_ms - self.min_ms) * (angle / self.max_angle))

    def uint16_to_ms(self, value):
        return value * (self.max_ms - self.min_ms) / 0xFFFF + self.min_ms
    
    def ms_to_angle(self, value):
        return (value - self.min_ms) * 180 / (self.max_ms - self.min_ms)


    def ms_to_uint16(self, value):
        return int(value * 0xFFFF * self.freq / 1000)


    def precentage_to_uint16(self, value):
        return 0xFFFF * value
    

    def ms_to_percentage(self, time_ms):
        return time_ms * self.freq / 1000 # ms factor