from time import sleep


class PourLiquid:
    pouring_time_seconds = 2

    @staticmethod
    def pour_liquid(water_pump):
        water_pump.start()
        sleep(PourLiquid.pouring_time_seconds)
        water_pump.stop()