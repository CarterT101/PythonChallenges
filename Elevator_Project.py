import random
import Elevator_Functions as Ef

max_capacity = 5        # maximum capacity of elevator
current_floor = 1       # starting current floor should be level 1
total_floors = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}        # total floors should be 5 as they will be 5 floors, and the value being the amount of people on it


"""
This section will allow users to input how many people will be in the building, if they do not want to input,
it will automatically make 10
"""
people_amount = input("How many people should be in this building?\nIf not just hit 'enter' key.\n")
if people_amount:
    Ef.create_people_list(int(people_amount))
else:
    Ef.create_people_list()

"""
This section will allow users to customize the floor the current person is on and wants to go to, if at any point
the user does not want to input data, they can hit enter key and values will already be created for them
"""


line = input("Input the floor the first person is on and the floor they want to go to separated by ',':"
             "\nIf not just hit 'enter' key.\n")
i = 1
while line:
    a, b = line.split(',')
    Ef.person_list[i] = [int(a), int(b)]
    print("Floor they are on: " + str(Ef.person_list[i][0]) + "\tFloor they want to go to: " +
          str(Ef.person_list[i][1]))
    i += 1
    line = input("Input the floor the next person is on and the floor they want to go to separated by ',': ")

print("\nCurrent list of people:\n")
for i, k in Ef.person_list.items():
    pass
    print("Person: " + str(i) + " \tCurrent Floor: " + str(k[0]) + "\tGo to Floor: " + str(k[1]))

print("")

temp_person_list = {
    1: [1, 5],
    2: [1, 5],
    3: [1, 3],
    4: [1, 3],
    5: [5, 2]
}

floor_list_amount = []
for s in temp_person_list.items():
    floor_list_amount.append(s[1][0])

for k in total_floors.keys():
    total_floors[k] = floor_list_amount.count(k)

for floornumber, amountofpeople in total_floors.items():
    print("Floor: " + str(floornumber) + " has " + str(amountofpeople) + " people")

print("")

Ef.going_up(current_floor, temp_person_list, total_floors)

