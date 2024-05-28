from time import sleep


class RotatePlate:
    increment_value = 0.01
    delay_s = 0.01

    @staticmethod
    def rotate_plate(rotation_plate, angle):
        increment_value = 0.5
        delay_s = 0.01
        
        if rotation_plate.get_angle() < angle:
            while rotation_plate.get_angle() < angle:
                rotation_plate.set_angle(rotation_plate.get_angle() + increment_value)
                sleep(delay_s)
            return
            
        elif rotation_plate.get_angle() > angle:
            while rotation_plate.get_angle() > angle:
                rotation_plate.set_angle(rotation_plate.get_angle() - increment_value)
                sleep(delay_s)