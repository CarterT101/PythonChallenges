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
if the current_floor value is in the people_goto_list, that means there is someone who needs to get dropped off on the 
current floor and this function will drop off the person from the list so they are no longer in the elevator
"""

def going_up(current_floor, people_goto_list, total_floors):
    elevator_population = 0
    print("variable = " + str(people_goto_list[current_floor]))
    go_up = True
    while go_up:
        if current_floor == len(total_floors):  # if current floor is every the length of total_floors (which is 5)
                                                # it should stop as there are no more floors to go up to
            go_up = False
        if total_floors[current_floor] > 0:     # if the current_floor variable has people on it, '> 0',
                                                # it should continue with the next lines of code
            for person in range(total_floors[current_floor]):
                if elevator_population == 5:
                    print("Elevator at max capacity: {}".format(elevator_population))
                    break
                elevator_population += 1
                total_floors[current_floor] -= 1
                print("People currently outside of elevator: " + str(total_floors[current_floor]))
        current_floor += 1
        # WORK ON GETTING THE PEOPLE OUT OF THE ELEVATOR
    pass


def going_down(current_floor, go_to_floor, people_goto_list):
    go_down = True
    while go_down:
        if current_floor == go_to_floor:
            break
        current_floor -= 1
        if current_floor in people_goto_list:
            for i in people_goto_list:
                if i == current_floor:
                    pass
        break
    pass

