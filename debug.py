from drive import DriveIn, MovieScreen, Car  
def main():
    
    sunset_drivein = DriveIn("Sunset DriveIn")

    avengers_screen = MovieScreen("Avengers", 5, sunset_drivein)
    print(MovieScreen.all_screens())

    car1 = Car()
    print(avengers_screen.add_car(car1))

    

if __name__ == "__main__":
    main()
