from src.hardware.rp5.PreasureSensor import PreasureSensor
from src.hardware.rp5.RotationPlate import RotationPlate
from src.hardware.rp5.WaterPump import WaterPump

from src.procedures.pour_liquid import PourLiquid
from src.procedures.rotate_plate import RotatePlate

# from src.PouringMachine import PouringMachine
import time

def main():
    ps1 = PreasureSensor(14)
    ps2 = PreasureSensor(15)
    ps3 = PreasureSensor(18)
    ps4 = PreasureSensor(23)
    ps5 = PreasureSensor(24)

    while True:
        print(ps1.get_input(), ps2.get_input(), ps3.get_input(), ps4.get_input(), ps5.get_input())
        time.sleep(3)

if __name__ == "__main__":
    main()
