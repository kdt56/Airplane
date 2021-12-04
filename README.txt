**GitHub**


**CLASS DESCRIPTION**
The Airplane class can be used to estimate flight times to Japan depending on the speed of the plane. The arguments include position and speed, which are created upon initialization of the class.

**CLASS AND DATA VARIABLES**
self.__position - Stores the position of the plane as a private data attribute.
self.__speed - Stores the speed of the plane as a private data attribute.

**METHODS**
get_position(self) - No arguments necessary. Simply calling the function will return self.__position.
set_position(self, x) - One argument is required. The argument is an integer and is set equal to self.__position in order to update the position value.

get_speed(self) - No arguments necessary. Simply calling the function will return self.__speed.
set_speed(self, x) - One argument is required. The argument is an integer and is set equal to self.__speed.

flight_time(self, plane) - This method is used to estimate the flight time of a plane to Japan, given the speed of that plane. One argument is required. The argument is the plane that is being flown in. Options include Plane A, Plane B, and Plane C. Returns a message that states the # of hours estimated for arrival in the specified plane.

start_flying(self) - This method is used to initiate takeoff from position 0. No arguments necessary. The plane flies until position reaches 100, meaning arrived in Japan. 

**DEMO PROGRAM**
The demo program prompts the user to select an airplane from the provided ones, and then sets the speed to a specific value that corresponds to the selected plane. The program then estimates the flight time using the speed of the plane, and prints it.

**INSTRUCTIONS**
Select from one of the planes listed and input it (case-sensitive). User may change the set_speed() values at lines 98, 101, and 104 to affect the estimated travel time.
