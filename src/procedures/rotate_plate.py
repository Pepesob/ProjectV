from time import sleep


class RotatePlate:
    increment_value = 0.01
    delay_s = 0.01

    @staticmethod
    def rotate_plate(rotation_plate, value):
        increment_value = 0.01
        delay_s = 0.01
        print(rotation_plate.get_duty_cycle())
        
        if rotation_plate.get_duty_cycle() < value:
            while rotation_plate.get_duty_cycle() < value:
                rotation_plate.set_duty_cycle(rotation_plate.get_duty_cycle() + increment_value)
                sleep(delay_s)
            return
            
        elif rotation_plate.get_duty_cycle() > value:
            while rotation_plate.get_duty_cycle() > value:
                rotation_plate.set_duty_cycle(rotation_plate.get_duty_cycle() - increment_value)
                sleep(delay_s)
