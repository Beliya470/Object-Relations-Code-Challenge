# CLASS DriveIn:
#     INIT with name
#     METHOD to get name

# CLASS MovieScreen:
#     INIT with movie_title, capacity, drive_in
#     METHOD to get movie title
#     METHOD to get capacity
#     METHOD to get associated drive-in
#     CLASS METHOD to get all movie screens
#     METHOD to get all cars
#     METHOD to get number of viewers
#     METHOD to check if at capacity
#     METHOD to get available spots
#     METHOD to add a car

# CLASS Car:
#     INIT with passenger_count
#     METHOD to get passenger count
#     METHOD to set and get current movie screen
#     CLASS METHOD to get all cars



# ipdb> drive_in1 = DriveIn("Sunset DriveIn")
# ipdb> screen1 = MovieScreen("Avengers", 5, drive_in1)
# ipdb> car1 = Car()
# ipdb> screen1.add_car(car1)
# ipdb> print(car1.current_movie_screen.movie_title())
