class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuelCapacity = 15
        self.fuel = 0

    def fuel_tank(self):
        self.fuel = self.fuelCapacity
        print("Fuel Tank is Full")

    def drive(self):
        print("Car is driving")


if __name__ == "__main__":
    my_drive = Car("Audi", "A6", 2023)
    print(my_drive.fuel)
    my_drive.fuel_tank()
    my_drive.drive()
