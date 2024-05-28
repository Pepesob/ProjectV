# from src.hardware.rp5.PreasureSensor import PreasureSensor
# from src.hardware.rp5.RotationPlate import RotationPlate
# from src.hardware.rp5.WaterPump import WaterPump

# from src.procedures.pour_liquid import PourLiquid
# from src.procedures.rotate_plate import RotatePlate

from src.PouringMachine import PouringMachine
import time

def main():
    pm = PouringMachine()

    pm.start_pouring_procedure()

if __name__ == "__main__":
    main()
