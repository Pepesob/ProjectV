from src.hardware.PreasureSensor import PreasureSensor
from src.hardware.WaterPump import WaterPump
from src.hardware.RotationPlate import RotationPlate
from src.hardware.Led import Led

from src.procedures.rotate_plate import RotatePlate
from src.procedures.pour_liquid import PourLiquid

import time

class PouringMachine:

    def __init__(self) -> None:
        self.led = Led()
        self.led.on()

        self.preasures = [PreasureSensor(0), PreasureSensor(1), PreasureSensor(2), PreasureSensor(3), PreasureSensor(4)]
        self.positions = [0, 36, 72, 108, 144]

        self.pump = WaterPump(9)

        self.plate = RotationPlate(5)
    
    def start_pouring_procedure(self):
        try:
            for preasure, position in zip(self.preasures, self.positions):
                RotatePlate.rotate_plate(self.plate, position)
                time.sleep(1)
                if preasure.get_input() == 1:
                    PourLiquid.pour_liquid(self.pump)
        except:
            self.reset_procedure()
    
    def get_preasure_values(self):
        return [p.get_input() for p in self.preasures]
                
    def reset_procedure(self):
        self.pump.stop()
        RotatePlate.rotate_plate(self.plate, 0)
            
