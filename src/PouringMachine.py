from src.hardware.PreasureSensor import PreasureSensor
from src.hardware.WaterPump import WaterPump
from src.hardware.RotationPlate import RotationPlate

from src.procedures.rotate_plate import RotatePlate
from src.procedures.pour_liquid import PourLiquid

# from machine import Pin
from time import sleep

class PouringMachine:

    def __init__(self) -> None:
        # self.led = Pin("LED", Pin.OUT)
        # self.led.on()
        # sleep(1)
        # self.led.off()
        # sleep(1)
        # self.led.on()

        self.preasures = [PreasureSensor(10), PreasureSensor(11), PreasureSensor(12), PreasureSensor(13), PreasureSensor(14)]
        self.positions = [0, 20, 40, 60, 80]

        self.pump = WaterPump(9)

        self.plate = RotationPlate(7)
    
    def start_pouring_procedure(self):
        try:
            for preasure, position in zip(self.preasures, self.positions):
                RotatePlate.rotate_plate(self.plate, position)
                if preasure.get_input() == 0:
                    PourLiquid.pour_liquid(self.pump)
        except:
            self.reset_procedure()
                
    def reset_procedure(self):
        self.pump.stop()
        RotatePlate.rotate_plate(self.plate, 0)
            
