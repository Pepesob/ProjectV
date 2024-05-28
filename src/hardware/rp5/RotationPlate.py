import gpiozero
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
        # self.pwm_pin2 = gpiozero.AngularServo(pwm_pin, initial_angle=0, min_angle=0, max_angle=self.max_angle, min_pulse_width=self.min_ms * 1e-3, max_pulse_width=self.max_ms * 1e-3, frame_width=1/self.freq)
        # self.pwm_pin3 = HardwarePWM(0, self.freq, 2)

    def set_angle_angulaservo(self, value):
        if not 0 <= value <= 180:
            print("Wrong angle value!")
            return
        self.pwm_pin2.angle = value
        print("Rotating to:", value)
    
    def stop(self):
        self.pwm_pin2.angle = None
    
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
    ps.pwm_pin3.change_duty_cycle(0)
    # for i in range(60):
    #     ps.set_angle(i*3)
    #     time.sleep(0.5)
