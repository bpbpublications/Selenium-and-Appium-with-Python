from Car import Car


class ElectricCar(Car):

    def __init__(self, make, model, year, electicCarUnit):
        super().__init__(make, model, year)
        self.electricCarUnit = electicCarUnit
        self.battrySize = 70
        self.chargeLevel = 0

    def charge(self):
        self.chargeLevel = 100
        print("Fully Charged")

    def fuel_tank(self):
        self.fuel = self.fuelCapacity
        print(str(self.fuel) + " " + "No Fuel Tank in Electric")


eleCar = ElectricCar("Tesla", "Model X", 2022, "WithSelfDriving")
eleCar.fuel_tank()
eleCar.drive()
