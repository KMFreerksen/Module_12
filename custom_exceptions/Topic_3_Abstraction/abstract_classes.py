from abc import ABC, abstractmethod


class Rider(ABC):
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass


class Bicycle(Rider):

    def __init__(self):
        self._Ride = 'human-powered, pedal-driven, open air single-track vehicle'
        self._Riders = '1 standard, 2 if tandem'

    def ride(self):
        return self._Ride

    def riders(self):
        return self._Riders + '\n'


class Motorcycle(Rider):

    def __init__(self):
        self._Ride = 'engine-powered, gasoline-fueled, open air single-track vehicle'
        self._Riders = '1 or 2, driver is required to have a motorcycle license'

    def ride(self):
        return self._Ride

    def riders(self):
        return self._Riders + '\n'

class Car(Rider):

    def __init__(self):
        self._Ride = 'engine-powered, gasoline, diesel, or battery power, enclosed, 4 wheels'
        self._Riders = '2 to 6 people, driver must have valid license, must comply with seatbelt and carseat requirements'

    def ride(self):
        return self._Ride

    def riders(self):
        return self._Riders + '\n'


# Driver
bike = Bicycle()
chopper = Motorcycle()
toyota = Car()

print(bike.ride())
print(bike.riders())

print(chopper.ride())
print(chopper.riders())

print(toyota.ride())
print(toyota.riders())
