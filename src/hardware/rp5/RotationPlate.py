import gpiozero
from gpiozero.pins.rpigpio import RPiGPIOFactory
import time

class RotationPlate:

    def __init__(self, pwm_pin:int) -> None:
        self.freq = 50
        self.max_ms = 2.6
        self.min_ms = 0.41

        self.max_angle = 180


        self.pwm_pin_num = pwm_pin

        initial_pos = self.ms_to_percentage(self.angle_to_ms(0))
        print("initial pos:", initial_pos)
        self.pwm_pin = gpiozero.PWMOutputDevice(pin=pwm_pin, active_high=True, initial_value=initial_pos, frequency=self.freq)
        
    
    def set_angle(self, value):
        if not 0 <= value <= 180:
            print("Wrong angle value!")
            return
        time_ms = self.angle_to_ms(value)
        print("Ms:", time_ms)
        print("percentage:", self.ms_to_percentage(time_ms))
        self.pwm_pin.value = self.ms_to_percentage(time_ms)
        print("Rotating to:", value)
    
    def get_duty_cycle(self):
        return self.pwm_pin.value

    def angle_to_ms(self, angle):
        return self.min_ms + ((self.max_ms - self.min_ms) * (angle / self.max_angle))

    def ms_to_percentage(self, time_ms):
        return time_ms * self.freq / 1000 # ms factor

if __name__ == "__main__":
    ps = RotationPlate(17)
    for i in range(60):
        ps.set_angle(i*3)
        time.sleep(0.5)
    # ps.set_angle(40)
    # time.sleep(5)
    # ps.set_angle(80)
    # time.sleep(5)