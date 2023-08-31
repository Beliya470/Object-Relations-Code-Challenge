# Object-Relations-Code-Challenge
Object Relations Code Challenge - DriveIn
For this challenge, we will be working with a drive-in movie domain.
We have three models: DriveIn, MovieScreen, and Car.
For this challenge, a DriveIn has many MovieScreens, a MovieScreen has many Cars, and a Car belongs to a MovieScreen.
A DriveIn has many Cars through its MovieScreens. A Car is only at one DriveIn.
Note: You should draw your domain on paper or on a whiteboard before you start coding. Remember to identify a single source of truth for your data.
Topics
Classes and Instances
Class and Instance Methods
Variable Scope
Object Relationships
lists and list Methods
Instructions
To get started, run pipenv install while inside of this directory.
Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.
Remember! This code challenge does not have tests. You cannot run pytest. You'll need to create your own sample instances so that you can try out your code on your own. Make sure your relationships and methods work in the console before submitting.
We've provided you with a tool that you can use to test your code. To use it, run python tools/debug.py from the command line. This will start a ipdb session with your classes defined. You can test out the methods that you write here. You can add code to the tools/debug.py file to define variables and create sample instances of your objects.
Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.
Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.
Before you submit! Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.
Deliverables
Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.
Some of the methods listed are provided to you in the starter code. You should check that they work correctly, and that you understand them.
Initializers, Readers, and Writers
DriveIn
DriveIn __init__(name)
A drive-in should be initialized with a name as a string.
The name cannot be changed after the drive-in is initialized.
DriveIn name()
should return the name of the DriveIn
MovieScreen
MovieScreen __init__((movie_title, capacity, drive_in)
A movie screen should be initialized with a movie title as a string, capacity (as an integer), and a drive_in object.
The movie title, capacity, and drive in cannot be changed after the MovieScreen is initialized.
MovieScreen movie_title()
should return the movie title
MovieScreen capacity()
should return the MovieScreen's capacity
MovieScreen drive_in()
should return the DriveIn associated with this MovieScreen
MovieScreen all_screens() class method
Returns an list of all movie screens that have been created.
Car
Car __init__(passenger_count)
A car should be initialized with a passenger_count (as an integer).
the passenger count can be changed after the Car is initialized
Car passenger_count()
Returns the number of passengers in the car.
Car all()
Returns an list of all car instances that have been created.
Object Relationship Methods
Car
Car current_movie_screen()
Returns the current movie screen that a particular car is associated with.
Car current_movie_screen=
Assigns a movie screen object to a particular car to indicate which movie screen that car is currently at.
Note: this will happen after a car has already been created.
MovieScreen
MovieScreen cars()
Returns an list of all cars currently at this movie screen.
DriveIn
DriveIn screens()
Returns an list of all movie screens at this drive-in.
Aggregate Methods
MovieScreen
MovieScreen number_of_viewers()
Returns the total number of passengers viewing the movie, from all the cars currently at this movie screen
MovieScreen at_capacity()
Returns a boolean. If the number of cars at this movie screen is equal to or above the capacity of the movie screen, returns true. Otherwise, returns false.
MovieScreen available_spots()
Returns the number of spots for cars available at this movie screen. This should be the capacity minus the number of cars currently at this movie screen.
MovieScreen add_car(car)()
Takes in a Car instance as the argument
Depending on the available capacity of the movie screen, associates the Car with this movie screen.
If the movie screen is not at capacity, updates the car's current movie screen and returns the string "Enjoy!".
If the movie screen is at capacity, it should return the string "Sold Out!", and should not associate the car to the movie screen.
DriveIn
DriveIn whats_playing()
Returns an list of all the names of the movies playing at the movie screens at this drive-in.
DriveIn full_house()
Returns true if all movie screens at this drive-in are at capacity.
.

