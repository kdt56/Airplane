'''

Kai Todd.
Assignment 10.1: Your Own Class.
Purpose: Practicing creating custom classes, encapsulation (private internal object variables), object-oriented programming, get-set methods, and using GitHub (extra credit).

**ACKNOWLEDGEMENTS**
https://www.geeksforgeeks.org/getter-and-setter-in-python/
https://www.tutorialspoint.com/python/python_classes_objects.htm
https://www.travelmath.com/flying-time/from/California/to/Japan
https://www.vistajet.com/en-us/stories/fastest-private-jet/
https://www.distance.to/California/Japan


'''




# Import time for use later.
import time
# Global variable that stores the distance from California to Japan.
JAPAN_DIST = 5355


# Define custom class 'Airplane'.
class Airplane:
    # Define class initialization.
    # Arguments include self, position set to 0, and speed set to 0.
    # They are then stored as private data variables.
    def __init__(self, position=0, speed=0):
        self.__position = position
        self.__speed = speed
        

    # Define first get method (position).
    def get_position(self):
        return self.__position
    # Define first set method (position).
    def set_position(self, x):
        self.__position = x


    # Define second get method (speed).
    def get_speed(self):
        return self.__speed
    # Define second set method (speed).
    def set_speed(self, x):
        self.__speed = x


    # Method that will use the speed of the plane to determine flight times to different imaginary locations.
    # Position represents the distance from the location. For example, 0 means not yet airborne, and 100 means arrived at location.
    def flight_time(self, plane):
        # Calculates the flight time based on the chosen airplane.
        hours = JAPAN_DIST / Airplane.get_speed(self)
        # Round to 2 decimal places
        hours = round(hours, 2)
        #Print a message telling the user the estimated hours with the selected plane.
        print(f'Flight time to Japan estimated to be {hours} hours while flying in {plane}.')


    # Method to start flying the plane to Japan.
    def start_flying(self):
        # P variable divides the speed of the current plane by 100.
        p = Airplane.get_speed(self) / 100
        flying = True
        print('Liftoff from position 0')
        time.sleep(1)
        # While loop that runs to show the position relevant to Japan. 0 means no lift-off, 100 means arrived in Japan.
        while flying == True:
            self.__position += p
            time.sleep(0.3)
            # When the position is greater than 100, breaks from the while loop and stops printing the current position.
            if self.__position > 100:
                break
            print(f'Current position at {self.__position}')
        print('Arrived in Japan!')


# Define main function.
def main():
    # Initialize class Airplane assigned to boeing variable.
    boeing = Airplane()
    
    # Prompts user to select a plane listed below.
    print('Welcome to blank airlines!')
    print('Please choose a plane:')
    print('Plane A')
    print('Plane B')
    print('Plane C')

    # Type name of chosen airplane.
    chosen_plane = input('>> ')

    # Sets the values for the chosen plane.
    if chosen_plane == 'Plane A':
        boeing.set_speed(460)
    
    elif chosen_plane == 'Plane B':
        boeing.set_speed(520)

    elif chosen_plane == 'Plane C':
        boeing.set_speed(575)

    # Prints the estimated flight time of the selected plane.
    boeing.flight_time(chosen_plane)

    print('Would you like to depart now?')
    print('Yes')
    print('No')

    # If user inputs 'Yes', the plane takes off.
    flying = input('>> ')

    if flying == 'Yes':
        # Call the start_flying() function.
        boeing.start_flying()
    # If the user inputs 'No', pass and the program ends.
    elif flying == 'No':
        pass
    

# Call the main function.
if __name__ == '__main__':
    main()