# finding if number is to the power of 2
import random



# interview question solution

lis = [1, 15, 2, 9, 7, 14]
newlist = []

for item1 in lis:  # for each item in list 'lis'
    for item2 in lis:  # and for every item in list 'lis' compare another item in list to find sum of the two
        if item1 + item2 == 16:  # if the sum of the two numbers = 16, add to new list in tuple form to gather pairs
                                # and then remove item from first list
            newlist.append((item1, item2))
            lis.remove(item1)

print(newlist)


def power_of_Two(n):
    return n > 0 and (n & (n - 1)) == 0


# return true if number is greater than 0 AND the binary digits == 0 together


"""print(power_of_Two(4))
print(power_of_Two(36))
print(power_of_Two(16))
print(power_of_Two(64))"""


def power_of_Two_two(n):
    if (n == 0):  # makes sure user doesn't input 0
        return False
    while (n != 1):  # while n is not 1, continue
        if (n % 2 != 0):  # if the remainder is not 0, return false
            return False
        n = n // 2  # keeps dividing by two as long as variable n is not 1
    return True  # if it gets to this point, it is to the power of two


"""print(power_of_Two_two(4))
print(power_of_Two_two(36))
print(power_of_Two_two(16))"""


# finding median of list
def tips_median(list):
    list.sort()
    list_length = len(list)
    if list_length % 2 == 0:
        return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
    return list[int(list_length / 2)]


"""print(tips_median([1, 2, 3, 4]))
print(tips_median([1, 2, 3, 4, 5]))"""

alist = list(range(20))
alist = random.sample(alist, len(alist))  # making random list


#  print(alist)

# START OF 10 CODE CHALLENGES OF PYTHON
def sort_list(n, st):
    if st == 'asc':
        answer = sorted(n)
        print(answer)
    elif st == 'desc':
        answer = sorted(n, reverse=True)
        print(answer)
    elif st == 'none':
        print(n)
    else:
        print("Please enter either asc, desc, or none as an input")


#  sort_list(alist, 'asc')

def dec_to_bin(d):
    if d > 1024:
        print("Number less than 1024")
        return
    print(bin(d).replace("0b", ""))  # bin makes it a binary, .replace makes it so it doesn't have 0b in front


#  dec_to_bin(1000)

def vowels(st):
    vowel = []
    for x in st:
        if (x == 'a') or (x == 'e') or (x == 'i') or (x == 'o') or (x == 'u'):
            vowel.append(x)
    if len(vowel) == 0:
        print("There are no vowels")
    else:
        print(len(vowel))


# vowels('Hello')


def creditcard(cc):
    num = str(cc)
    num1 = '*' * (len(num) - 4) + num[-4:]
    print(num1)


# creditcard(4444444444444444)


def x_and_o(xo):
    x = []
    o = []
    xo = xo.lower()
    for i in xo:
        if i == 'x':
            x.append(i)
        elif i == 'o':
            o.append(i)
    if len(x) == len(o):
        print(True)
    else:
        print(False)


# x_and_o('XOXOXOXO')

def calc(n, o, i):
    try:
        n = int(n)
        i = int(i)
        if o == '+':
            print(n + i)
        elif o == '-':
            print(n - i)
        elif o == '/':
            print(n / i)
        else:
            print("Please input correct operator")
    except:
        print("Please enter integers")


"""n = input("Enter first integer: ")
o = input("Enter operator: ")
i = input("Enter second integer: ")

calc(n, o, i)"""


def discount(i, n):
    i = int(i)
    n = float(n)
    disc = (n / 100) * i
    print(i - disc)


# discount(80, 20)

numlist = list(range(20))
alist = ['hello', 'bye', 'never', 'list']
for x in numlist: alist.append(x)
alist = random.sample(alist, len(alist))


def just_numbers(ls):
    print(ls)
    numberlist = []
    for i in ls:
        if type(i) == int:
            numberlist.append(i)
    return numberlist


# print(just_numbers(alist))


def repeat(st):
    st = "".join([x * 2 for x in st])
    return st


# print(repeat("Hello"))

# END OF 10 PYTHON CHALLENGES

#  START OF PYTHON PRINCIPLES QUESTIONS
# LINK: https://pythonprinciples.com/challenges/

def capital_indexes(st):
    inlist = []  # created empty list
    i = 0  # created iterable variable to count index number
    for s in st:
        if s.isupper():
            inlist.append(i)  # if iterable item is uppercase, add the index number
        i += 1  # add 1 to index number for next iteration
    return inlist


# print(capital_indexes("HeLlO"))


def mid(st):
    i = 0  # created iterable item to count string amount
    for s in st:
        i += 1  # gets length of string
    if i % 2 == 0:  # basically if 'i' is evenly divisible, it doesn't have a middle letter therefore it returns empty
        return ""
    elif i % 2 == 1:  # if 'i' leaves a remainder, it has a middle letter so continue steps
        i = i // 2  # divides length of string by two and returns the floor number to get the middle letter of sequence
        return st[i]


# print(mid("acd"))

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(dict):
    num = 0
    for i, s in dict.items():  # goes through each item in dictionary
        if s == "online":  # checks item in dictionary to see if string matches 'online'
            num += 1  # if item == online, add one to number
    return num


#  print(online_count(statuses))

def random_number():
    i = random.randint(1, 100)  # produces random number 1-100
    return i


#  print(random_number())

def only_ints(i, s):
    if isinstance(i, int) and isinstance(s, int) and not isinstance(i, bool) and not isinstance(s, bool):
        # checks if the two arguments are integer and NOT bool since bool True and False are subs of int data type
        return True
    else:
        return False


# print(only_ints(1, 1))

def double_letters(st):
    i = 0
    num = 0
    for s in st:  # for each item in string, go through loop
        if i == 0:  # first iteration will always be 0, this is just to gather the first letter of the word
            i += 1
            letter = s
        else:
            if s == letter:  # checks if there are two in a row, if not, it goes onto next letter
                num += 1  # if there are two letters in row, it adds a number to this variable
            else:
                letter = s
                i += 1
    if num > 0:
        return True  # after running through whole string, if num variable is greater than 0, it had two letters in row
    else:
        return False


# print(double_letters("hello"))

def add_dots(st):
    newstring = ""  # creates empty string
    length = len(st)  # gets length of string
    for s in st:  # for each item in string
        newstring += "{}".format(s)  # adds the current letter to new string
        if length > 1:
            newstring += '.'  # this is to prevent a '.' at end of word.
        length -= 1  # subtracts one from length of string to help with '.' at end
    return newstring  # returns newly created string


# print(add_dots("test"))

def remove_dots(st):
    newstring = ""  # creates newstring
    for s in st:  # goes through each item in string
        if s == '.':  # checks if the current item is a '.', if it is, continue to next iteration
            continue
        newstring += s  # adds item to newstring IF it is not a '.'
    return newstring


# print(remove_dots(add_dots("test")))

# counting syllables
def count(st):
    num = 1  # sets number equal to 1 because all words have at least one syllable
    for s in st:
        if s == "-":  # if it finds a '-' it means a new syllable is starting therefore the count of syllables
            # needs to go up one
            num += 1
    return num


# print(count("ho-tel"))
# print(count("ter-min-a-tor"))

def is_anagram(str1, str2):
    string1 = []  # create two empty lists to make string into lists
    string2 = []
    i = 0  # sets iterable equal to 0 for index of second string
    if len(str1) != len(str2):  # checks right away if length of str1 is equal to str2, if not return False
        # because in order for it to be an anagram it has to be the same length
        return False
    for s in str1:
        string1.append(s)  # adds first word to list
    for s in str2:
        string2.append(s)  # adds second word to list
    string1 = sorted(string1)  # sorts both the lists
    string2 = sorted(string2)
    print(string1, string2)
    for item in string1:  # for each item in string1, if item does not equal the same item index number in string2
        # return false as that means it does not have the same letters
        if item != string2[i]:
            return False
        i += 1  # adds 1 to iterable so second string follows along in index number as the first string index
    return True
    # if it makes it through all of that it means all the letters are the same therefore it is an anagram


#  print(is_anagram("typhoon", "opython"))

def flatten(lis):
    newlist = []
    for m, n in lis:  # for each item in lis, add it to a new list
        newlist.append(m)
        newlist.append(n)
    return newlist


# print(flatten([[1, 2], [3, 4]]))

def largest_difference(lis):
    return max(lis) - min(lis)  # gets largest and smallest number in list and subtract them together


# print(largest_difference([1, 2, 3]))

def div_3(i):
    if i % 3 == 0:  # if there is no remainder, return True
        return True
    else:
        return False  # if there is a remainder, return False because it is not divisible by 3

# print(div_3(15))

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

def get_row_col(st):
    st = st.lower()
    i = 0  # column / letter
    r = 0  # row / number
    if len(st) == 2:
        if st[0] == 'a':  # using the created variables as placeholders for the row and column numbers
            r = 0
        if st[0] == 'b':
            r = 1
        if st[0] == 'c':
            r = 2
        if st[1] == '1':
            i = 0
        if st[1] == '2':
            i = 1
        if st[1] == '3':
            i = 2
        x = (i, r)  # make a tuple
        return x
    else:
        return "Please enter valid spot"


# print(get_row_col("A3"))

def palindrome(st):
    if st == st[::-1]:  # reverses the string to check if the string is the same as the string backwards
        return True
    else:
        return False

# print(palindrome("bob"))

def up_down(i):
    s = i-1
    i += 1
    result = (s, i)  # returns tuple with one number higher and one number lower than inputted number
    return result

# print(up_down(5))

def consecutive_zeros(st):
    x = st.split('1')  # splits the string by 1s to find the groups of 0
    return len(max(x))  # prints the length of the largest group of 0s

# print(consecutive_zeros("1001101000110"))

def all_equal(items):
    for item1 in items:
        for item2 in items:  # goes through each list comparing each item to the one before it
            if item1 != item2:  # if one item does not equal another, return false
                return False
    return True  # if it makes it through the list, then it should return True as all of them were equal

# print(all_equal([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

def triple_and(l, m , o):
    if l and m and o:  # if all equal true, return true
        return True
    if not l and m and o:  # if all equal false, return true
        return True
    else:                   # if not all equal either true or false, return false
        return False

# print(triple_and(True, True, True))

def convert(lis):
    return list(map(str, lis))  # produces map object which is then converted back into a list

# print(convert([1, 2, 3]))

def zap(a, b):
    newlist = []  # empty list
    s = 0           # iterable
    for i in a:     # for every item in list a
        newlist.append((i, b[s]))  # add current item in list a and current item in list b with iterable variable
        s += 1
    return newlist

"""print(zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
))"""

def list_xor(n, list1, list2):
    if n in list1 and n in list2:  # checks if n is in both
        return False
    if n not in list1 and n not in list2:  # checks if n is not in both
        return False
    if n in list1 or n in list2:
        return True  # only returns true if in either, not both or none

# print(list_xor(1, [1, 2, 3], [4, 5, 6]))

def param_count(*args):
    return len(args)

# print(param_count(1, 2, 3))

def format_number(n):
    return "{:,}".format(n)  # format placeholder, adds , as thousands separator

# print(format_number(1000000))

#  END OF PYTHON PRINCIPLES QUESTIONS
