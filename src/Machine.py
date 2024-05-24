from hardware.PreasureSensor import PreasureSensor
from hardware.WaterPump import WaterPump
from hardware.RotationPlate import RotationPlate

from procedures.rotate_plate import RotatePlate
from procedures.pour_liquid import PourLiquid

from machine import Pin
from time import sleep

class Machine:

    def __init__(self) -> None:
        self.led = Pin(25, Pin.OUT)
        self.led.on()
        sleep(0.2)
        self.led.off()
        sleep(0.2)
        self.led.on()

        self.preasures = [PreasureSensor(10), PreasureSensor(11), PreasureSensor(12), PreasureSensor(13), PreasureSensor(14)]
        self.positions = [0, 20, 40, 60, 80]

        self.pump = WaterPump(9)

        self.plate = RotationPlate(7)
    
    def start_pouring_procedure(self):
        for preasure, position in zip(self.preasures, self.positions):
            RotatePlate.rotate_plate(self.plate, position)
            if preasure.get_input() == 1:
                PourLiquid.pour_liquid(self.pump)
            
