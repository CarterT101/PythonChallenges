import random

def random_floor(n, end, start=1):  # n being the number it can't be
    return [*range(start, n), *range(n+1, end)]  # makes a list within a range and a restriction

"""
'*' unpacks an iterable, each element is passed as separate argument, 
rather than function receiving iterable as a single argument
"""


"""
this function/loop makes a dictionary of people and assigns them a random floor they are on, and then it makes another
random number with the restriction that the floor they want to go to CAN NOT BE the same floor they are on
"""

person_list = dict()  # creating dictionary object

def create_people_list(n=10):
    # THIS IS AN ELEVATOR THAT STARTS ON FLOOR 1 AND HAS 5 FLOORS, so randrange(1,6) makes it so that is true

    for i in range(1, n+1):
        person_list[i] = [random.randrange(1, 6), 0]
        # add values to iterated person with a random choice of floor and a temp number '0'
        go_to = random_floor(person_list[i][0], 6)
        # makes a new random list with restriction
        person_list[i][1] = random.choice(go_to)
        # replaces temp number with another random number that is NOT the floor they are currently on

    """
    print(person_list[1][0])  # prints the floor they are on
    print(person_list[1][1])  # prints the floor they want to go to
    """


"""
if the current_floor value is in the people_go_to, that means there is someone who needs to get dropped off on the 
current floor and this function will drop off the person from the list so they are no longer in the elevator
"""

def going_up(current_floor, people_go_to, people_on_floor, total_floors, people_list, elevator_population):
    print("Elevator currently going up...\n")
    max_level = max(people_on_floor + people_go_to)  # finds the max level the elevator needs to go to
    go_up = True
    while go_up:
        if current_floor == max_level:  # makes it so if there is no one on the top floor or wants to go to it, it won't
            go_up = False
        if current_floor == 1:          # if current floor is one, pass this if statement
            pass
        else:               # if current floor is not one, meaning it is currently in the loop of going upwards, print
            print("Going up to floor {}...\n".format(current_floor))
        # prints current floor, elevator population, and the floor population of the current floor it is on,
        # if the floor population is above 0, it means people want to get on the elevator
        print("Current Floor: " + str(current_floor), "\nElevator Pop: " + str(elevator_population),
              "\nFloor {} Population: ".format(current_floor) + str(total_floors[current_floor]))
        print("")

        if people_on_floor.count(current_floor) > 0:     # if the current_floor variable has people on it, ie: '> 0',
                                                # it should continue with the next lines of code
            for person in range(total_floors[current_floor]):

                if elevator_population == 5 and people_go_to.count(current_floor) == 0:
                    print("1 Elevator at max capacity: {}".format(elevator_population))
                    break
                elevator_population += 1
                total_floors[current_floor] -= 1
                print("One person getting on...")
                if elevator_population > 5 and people_go_to.count(current_floor) > 0:
                    pass
                else:
                    print("People currently inside elevator: " + str(elevator_population),
                          "\tCurrent outside: " + str(total_floors[current_floor]))
        print("")
        if current_floor in people_go_to:
            reply = True
            for people in range(1, len(people_list)):
                if people_list[people][0] <= current_floor and people_list[people][1] == current_floor:
                    if reply:
                        reply = False
                    elevator_population -= 1
                    people_go_to.remove(current_floor)
                    print("One person getting off...")
            if elevator_population >= 5 and total_floors[current_floor] != 0:
                print("2 Elevator at max capacity: {}".format(elevator_population))
                pass
            else:
                for person in range(total_floors[current_floor]):
                    if elevator_population == 5:
                        print("3 Elevator at max capacity: {}".format(elevator_population))
                        pass
                    else:
                        elevator_population += 1
                        total_floors[current_floor] -= 1
                        print("One person getting on...")
        print("")
        current_floor += 1
    print("People currently inside elevator: " + str(elevator_population), "\tPeople on floors: " + str(total_floors))
    going_down(current_floor, people_go_to, people_on_floor, total_floors, people_list, elevator_population)


def going_down(current_floor, people_go_to, people_on_floor, total_floors, people_list, elevator_population):
    print("Now going down...")
    go_down = True
    while go_down:
        if current_floor < 1:
            go_down = False
        current_floor -= 1
        if current_floor in people_go_to:
            for i in people_go_to:
                if i == current_floor:
                    pass
        break
    pass

