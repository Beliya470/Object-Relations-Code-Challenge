class DriveIn:
    def __init__(self, name):
        self._name = name
        self._screens = []

    def name(self):
        return self._name

    def screens(self):
        return self._screens

    def whats_playing(self):
        return [screen.movie_title() for screen in self._screens]

    def full_house(self):
        return all(screen.at_capacity() for screen in self._screens)


class MovieScreen:
    _all_screens = []

    def __init__(self, movie_title, capacity, drive_in):
        self._movie_title = movie_title
        self._capacity = capacity
        self._drive_in = drive_in
        self._cars = []
        self._drive_in._screens.append(self)
        self._all_screens.append(self)

    @classmethod
    def all_screens(cls):
        return cls._all_screens

    def movie_title(self):
        return self._movie_title

    def capacity(self):
        return self._capacity

    def drive_in(self):
        return self._drive_in

    def cars(self):
        return self._cars


    def at_capacity(self):
        return len(self._cars) >= self._capacity

    def available_spots(self):
        return self._capacity - len(self._cars)

    def add_car(self, car):
        if not self.at_capacity():
            self._cars.append(car)
            car.current_movie_screen = self
            return "Enjoy!"
        else:
            return "Sold Out!"

class Car:
    _all_cars = []

    def __init__(self):
        self._current_movie_screen = None
        self._all_cars.append(self)

    @classmethod
    def all(cls):
        return cls._all_cars

    @property
    def current_movie_screen(self):
        return self._current_movie_screen

    @current_movie_screen.setter
    def current_movie_screen(self, movie_screen):
        self._current_movie_screen = movie_screen
