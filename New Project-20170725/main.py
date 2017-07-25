import math

print("\n**********  Traffic Calculator  **********\n\n")

def print_list():
    print("Select:\n\t 1 : Skid to Stop ")
    print("\t 2 : MPH to FPS")
    print("\t 99 : Quit Program")
    return ""

def skidToStop():
    '''
    30DF formula. Takes in the distance of a skid and friction of the roadway.
    returns how fast the vehicle was going just prior to the skid.

    :param distance: test
    :param friction:
    :return:
    '''

    print("Skid to Stop Selected")
    dist = input("Enter distance in feet-> ")
    friction = input("Enter friction -> ")

    speed = math.sqrt(30 * dist* friction)
    print "The vehicle was traveling ", speed , " MPH"
    return speed

def mph_to_fps():
    '''
    MPH to FPS calculation. Takes in a MPH and returns its value in FPS.
    :param mph:
    :return:
    '''

    print("MPH to FPS Selected")
    mph = input("Enter MPH -> ")
    fps = mph * 1.467
    print mph, "MPH", " is ", fps , "FPS"

    return ""





choice = 0

while choice != 99:
    print_list()
    choice = input("Make a Selection -> ")
    if choice == 1:

        skidToStop()

        break

    if choice == 2:

        mph_to_fps()

        break

print("\nExiting Program. Bye!")