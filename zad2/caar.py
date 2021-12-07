class Car:
    def FuelChceck(self):
        pass

    def chceckEngineTemperature(self):
        pass

    def setDestination(self, destination):
        pass


class CarImpl:
    def __init__(self):
        self.car = Car()

    def FuelChceck(self):
        return self.car.FuelChceck()

    def chceckEngineTemperature(self):
        if self.chceckEngineTemperature() > 110:
            return "Za duża temperatura"
        else:
            return self.car.chceckEngineTemperature()

    def setDestination(self, destination):
        return self.car.setDestination(destination)