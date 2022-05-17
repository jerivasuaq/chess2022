# Abstract
class MotorVehicle:
    no_wheels = 0
    max_velocity = 0
    power = 0
    gas_mileage = 0
    no_passangers = 0
    color = "black"

    def __init__(self):
        pass

    def crash(self, obj):
        pass

    def fill_tank(self, gas):
        self.fuel_level = self.fuel_level + gas

    def run_over(self, person):
        self.crash(person)

    def push_brakes(self):
        pass

    def sit_passanger(self, person):
        pass

    def start_machine(self):
        print("start_machine")

    def switch_gears(self):
        pass

    def push_gas(self):
        pass

    def __add__(self, val: int):
        self.no_wheels += val


class Sedan(MotorVehicle):
    def __init__(self, model, color, max_velocity):
        """
        class Sedan

        it has information about the vehicle
        """
        super(Sedan, self).__init__()

        self.model = model
        self.color = color
        self.wheels = 4
        self.max_velocity = max_velocity
        self.power = 10
        self.gas_mileage = 9.4
        self.no_passangers = 5

    def switch_gears(self):
        print("Push clutch pedal")
        print("Switch gear stick to another")
        print("Release the clutch and push the gas")

    def __str__(self):
        return str(
            {
                "model": self.model,
                "color": self.color,
                "wheels": self.wheels,
                "max_velocity": self.max_velocity,
                "power": self.power,
                "gas_mileage": self.gas_mileage,
                "no_passangers": self.no_passangers,
            }
        )


class Motorcycle(MotorVehicle):
    def __init__(self, model, color, max_velocity):
        """
        class MotorVehicle

        it has information about the Motorcycle
        """
        super(Motorcycle, self).__init__()

        self.model = model
        self.color = color
        self.no_wheels = 2
        self.max_velocity = max_velocity
        self.power = 5
        self.gas_mileage = 20
        self.no_passangers = 2

    def switch_gears(self):
        print("Pull the left handle bar")
        print("Switch gear using the left pedal")
        print("Release the clutch and push the gas")

    def __str__(self):
        return str(
            {
                "model": self.model,
                "color": self.color,
                "wheels": self.wheels,
                "max_velocity": self.max_velocity,
                "power": self.power,
                "gas_mileage": self.gas_mileage,
                "no_passangers": self.no_passangers,
            }
        )


if __name__ == "__main__":
    sedan_luis = Sedan(model="Versa", color="black", max_velocity=180)
    sedan_luis.start_machine()
    sedan_luis.no_wheels = 20

    print(sedan_luis)

    erik_moto = Motorcycle(model="Kawasaki", color="yellow", max_velocity=120)
    erik_moto.start_machine()
    print("before", erik_moto.no_wheels)
    erik_moto + 5
    print("after", erik_moto.no_wheels)

    ""
