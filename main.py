# from src.hardware.rp5.PreasureSensor import PreasureSensor
# from src.hardware.rp5.RotationPlate import RotationPlate
# from src.hardware.WaterPump import WaterPump

# from src.procedures.pour_liquid import PourLiquid
# from src.procedures.rotate_plate import RotatePlate

from src.PouringMachine import PouringMachine
import time

def main():
    pm = PouringMachine()
    
    while True:
        pm.wait_for_button()
        pm.start_pouring_procedure()
        pm.wait_for_button()
        pm.start_pouring_procedure_reverse()
        

if __name__ == "__main__":
    main()
