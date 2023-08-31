import ipdb;
from drive import DriveIn, MovieScreen, Car  

if __name__ == "__main__":
    drive_in1 = DriveIn("Sunset DriveIn")
    screen1 = MovieScreen("Avengers", 5, drive_in1)
    car1 = Car()
    ipdb.set_trace()
