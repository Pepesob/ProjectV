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

        self.preasures = [PreasureSensor(0), PreasureSensor(1), PreasureSensor(2) ]#, PreasureSensor(3)]# PreasureSensor(4)]
        self.positions = [0, 62, 127] # 108, 144]

        self.pump = WaterPump(9)

        self.plate = RotationPlate(5)
        
        self.button = PreasureSensor(6)
    
    def wait_for_button(self):
        prev = self.button.get_input()
        while prev == self.button.get_input():
            time.sleep(0.2)
    
    def start_pouring_procedure(self):
        try:
            for i in range(3):
                self.move_and_pour(i)
        except:
            self.reset_procedure()
    
    def start_pouring_procedure_reverse(self):
        try:
            for i in range(2,-1,-1):
                self.move_and_pour(i)
        except:
            self.reset_procedure()

    def move_and_pour(self, i):
        preasure = self.preasures[i]
        position = self.positions[i]
        RotatePlate.rotate_plate(self.plate, position)
        if preasure.get_input() == 1:
            PourLiquid.pour_liquid(self.pump)
    
    def get_preasure_values(self):
        return [p.get_input() for p in self.preasures]
                
    def reset_procedure(self):
        self.pump.stop()
        RotatePlate.rotate_plate(self.plate, 0)
            
