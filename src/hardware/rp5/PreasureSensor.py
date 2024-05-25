import gpiozero

class PreasureSensor:

    def __init__(self, gpio_in: int):
        self.gpio_in_num = gpio_in

        self.gpio_button = gpiozero.Button(gpio_in, pull_up=True)

    def get_input(self):
        print("Preasure sensor read:", self.gpio_button.value)
        return self.gpio_button.value
    
    def update(self):
        # This function should check input and change output corespondingly; it will be run periodically in the loop
        pass

if __name__ == "__main__":
    ps = PreasureSensor(1)
    ps.get_input()
