from src.hardware.PreasureSensor import PreasureSensor
from src.hardware.RotationPlate import RotationPlate
from src.hardware.WaterPump import WaterPump

from src.procedures.pour_liquid import PourLiquid
from src.procedures.rotate_plate import RotatePlate

from src.PouringMachine import PouringMachine

def main():
    pm = PouringMachine()

    pm.start_pouring_procedure()

if __name__ == "__main__":
    main()
