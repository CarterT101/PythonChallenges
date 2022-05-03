import random


def random_floor(n, end, start=1):  # n being the number it can't be
    return [*range(start, n), *range(n+1, end)]  # makes a list within a range and a restriction

person_list = dict()


"""
this loop makes a dictionary of people 1-10 and assigns them a random floor they are on, and then it makes another
random number with the restriction that the floor they want to go to CAN NOT BE the same floor they are on
"""

# THIS IS AN ELEVATOR THAT STARTS ON FLOOR 1 AND HAS 5 FLOORS, so randrange(1,6) makes it so that is true

for i in range(1, 11):
    person_list['person{}'.format(i)] = [random.randrange(1, 6), 0]
    # add values to iterated person with a random choice of floor and a temp number '0'
    gotofloor = random_floor(person_list['person{}'.format(i)][0], 6)
    # makes a new random list with restriction
    person_list['person{}'.format(i)][1] = random.choice(gotofloor)
    # replaces temp number with another random number that is NOT the floor they are currently on

# print(person_list['person1'][0])  # prints the floor they are on
# print(person_list['person1'][1])  # prints the floor they want to go to


"""
this section of code will allow the user to input their own data and they can stop at any point
if they stop before making 10 people with data, it will automatically create the others to make sure
at least 10 people are created. if the user decides to make more than 10 people, it will allow that
"""

line = input("Input the floor a person is on and the floor they want to go to separated by ',': ")
i = 1
while line:
    a, b = line.split(',')
    person_list['person{}'.format(i)] = [int(a), int(b)]
    print(person_list)
    i += 1
    line = input("Input the floor a person is on and the floor they want to go to separated by ',': ")

print("\nCurrent list of people:\n")
for i, k in person_list.items():
    print("Person: " + i + " \tCurrent Floor: " + str(k[0]) + "\tGo to Floor: " + str(k[1]))