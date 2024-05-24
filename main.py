from src.hardware.PreasureSensor import PreasureSensor
from src.hardware.RotationPlate import RotationPlate
from src.hardware.WaterPump import WaterPump

from src.procedures.pour_liquid import PourLiquid
from src.procedures.rotate_plate import RotatePlate

from machine import Pin
from time import sleep


def main():
    led = Pin(25, Pin.OUT)
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    led.on()
    ps = PreasureSensor(9)
    rp = RotationPlate(2)
    wp = WaterPump(6)
    
    
    for i in range(5):
        RotatePlate.rotate_plate(rp, 20*i)
        PourLiquid.pour_liquid(wp)


if __name__ == "__main__":
    main()
