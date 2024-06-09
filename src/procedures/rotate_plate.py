from time import sleep


class RotatePlate:
    increment_value = 0.005
    delay_s = 0.05

    @staticmethod
    def rotate_plate(rotation_plate, angle):
        increment_value = 0.3 #0.5
        delay_s = 0.05 #0.01
        
        if rotation_plate.get_angle() < angle:
            while rotation_plate.get_angle() < angle:
                set_value = rotation_plate.get_angle() + increment_value
                if set_value > 180:
                    set_value = 180
                rotation_plate.set_angle(set_value)
                sleep(delay_s)
            return
            
        elif rotation_plate.get_angle() > angle:
            while rotation_plate.get_angle() > angle:
                set_value = rotation_plate.get_angle() - increment_value
                if set_value < 0:
                    set_value = 0
                rotation_plate.set_angle(set_value)
                sleep(delay_s)
