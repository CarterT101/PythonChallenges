from datetime import datetime
import math
import re


# python file full of challenges from py.checkio.org


def first_word(str):
    result = str.split()
    if ',' in result[0]:
        result[0] = result[0].replace(',', '')
    return result[0]


# print(first_word('Hello, world'))

def is_acceptable_password(password):
    if len(password) >= 6:
        return True
    else:
        return False


# print(is_acceptable_password('short'))

def num_length(n):
    return len(str(n))


def most_frequent(lis):
    counter = 0
    num = lis[0]  # sets variable to first item in list
    for i in lis:
        freq = lis.count(i)  # for each item it will check the amount of times the iterable appears in list
        if freq > counter:  # if that number is bigger than the counter, it sets the counter number to amount
            # of iterable in list
            counter = freq
            num = i  # sets returnable variable to the iteration value it is on
    return num


lis = [
    'a', 'b', 'c',
    'a', 'b',
    'a'
]


# print(most_frequent(lis))

# another solution

# print(max(set(lis), key=lis.count))

def end_zeros(n):
    n = str(n)  # converts number to string
    if n == 0 or n == '0':  # if it is just 0 it has 1 zero, so return 1
        return 1
    else:  # if it is not 0, continue with statement
        i = 1  # sets iterable to 1
        if n[len(n) - 1] == '0':
            while n[len(n) - i] == '0':
                i += 1
        return i - 1


# print(end_zeros('100010'))


def easy_unpack(item):
    return (item[0], item[2], item[-2])


# print(easy_unpack([1,2,3,4,5,6,7,9]))

def remove_all_before(lis, n):
    count = 0
    newlist = []
    if n in lis:
        for i in lis:
            if i == n:
                for l in lis[count:]:
                    newlist.append(l)
                return newlist
            count += 1
    else:
        return lis


# print(remove_all_before([1, 2, 3, 4, 5], 3))

def is_all_upper(str):
    for s in str:
        if s.isdigit():
            continue
        if s.islower():
            return False
    return True


# print(is_all_upper('HELLO 5 5 5 '))

def replace_first(lis):
    if len(lis) == 0:
        return lis
    lis.append(lis[0])
    lis.pop(0)
    return lis


# print(replace_first([1, 2, 3, 4]))

def max_digit(n):
    return max(map(int, str(n)))  # returns max of a list made from map object which put each item in str(n) into list
    # that was made into integers


# print(max_digit(12213))

def split_pairs(str):  # brute force way
    newlist = []
    i = 0
    count = 2
    if len(str) == 1:
        str += '_'
        return [str]
    elif len(str) == 2:
        return [str]
    elif len(str) % 2 != 0:
        str += '_'
    while count < len(str) and i < len(str):
        for s in str:
            print(i, count)
            newlist.append(str[i:count])
            i += 2
            count += 2
            if '' in newlist:
                newlist.remove('')
    return newlist


# print(split_pairs('aa'))

# another solution

def split_pairs2(a):  # fast easy way
    return [ch1 + ch2 for ch1, ch2 in zip(a[::2], a[1::2] + '_')]  # ::2 means two increments


# print(split_pairs2('aa'))

def beginning_zeros(str):
    i = 0
    for s in str:
        if s == '0':
            i += 1
        else:
            return i
    return i


# print(beginning_zeros('000100'))


def nearest_value(values: set, i: int) -> int:
    return min((abs(n - i), n) for n in values)[1]  # makes a list of tuples, with the difference of the iterable
    # subtracted by given number, and returns the min(), the smallest
    # number found in the list of tuples and then gives the second index
    # which is the number that created smallest number


# print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

"""def between_markers(str, m, n):
    string_found = ''  # makes empty string
    i = 1  # keeps track of string index, equal to one so it skips the first marker
    for s in str:
        if s == m:  # if iterable equals first marker, it breaks the for loop and continues to while
                    # loop with saved 'i' index, and continues from there
            break
        i += 1
    while str[i] != n:  # while str[i] does not equal second marker
        string_found = string_found+str[i]  # add index location to new string
        i += 1
    return string_found"""


# print(between_markers('What is >apple<', '>', '<'))

def correct_sentence(str):
    result = str[0].upper() + str[1:]  # makes sure first index is upper
    if result[-1] != '.':  # if the last index is not a period, add it and then return result
        result = result + '.'
    return result


# print(correct_sentence("greetings, friends"))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# print(is_even(9))

def sum_numbers(str):
    i = 0
    for s in str.split():
        if s.isdigit():
            i += int(s)
    return i


# print(sum_numbers('who is 2 here 4'))

def checkio(lis):
    if len(lis) == 0:
        return 0
    i = 0
    result = 0
    for n in lis:
        if i % 2 == 0 or i == 0:
            result += n
        i += 1
    return result * lis[-1]


# print(checkio([1, 3, 5]))

def distinguish_words(str):
    str = str.split()
    i = 0
    for s in str:
        if not s.isdigit():
            i += 1
        if s.isdigit():
            i = 0
        if i >= 3:
            return True
    return False


# print(distinguish_words('Hi i am 3'))

"""
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
"""


def first_word2(str):  # extreme brute force way, I am sure there is an easier way but this is how I solved it
    i = 0  # setting iterable in case you have to switch index numbers
    if '.' in str:
        str = str.split(".")  # splits hello.world example
        while "" in str:  # removes white space
            str.remove("")
    else:  # if no . in str, normal split
        str = str.split()
    if "," in str[i]:  # if there is a comma, get rid of it
        str[i] = str[i].replace(",", "")
    result = ""  # making empty string to help with white space
    str[i] = str[i].strip()  # gets rid of beginning and ending whitespace
    for m in str[i]:  # for each item in str[i], add to new string
        if m == " ":  # if 'm' reaches a whitespace, it has hit second word,
            # which means it should stop and return result
            break
        result = result + m  # keeps adding iterable to new string to form new word in new string variable
    return result


"""print(first_word2("... hello world ..."))
print(first_word2("hello.world"))
print(first_word2("  a word  "))
print(first_word2("don't touch it"))"""


# better solution
def first_word3(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in ',. ':  # makes sure to skip all of the text that is commas or periods
        i += 1
    j = i
    while j < len(text) and text[j] not in ',. ':  # gets ending point of word
        j += 1
    return text[i:j]  # prints the index numbers sliced


def days_diff(m, n):
    m = datetime.date(m[0], m[1], m[2])  # making datetime objects
    n = datetime.date(n[0], n[1], n[2])
    result = n - m  # subtracting from each other
    return abs(result.days)  # making sure answer is positive


# print(days_diff((1982, 4, 19), (1982, 4, 22)))


def count_digits(str):
    i = 0
    for s in str:
        if s.isdigit():
            i += 1
    return i


# print(count_digits("hi"))


def backward_string_by_word(str):
    result = ' '.join([x[::-1] for x in str.split(' ')])  # for every item (that is put in reverse)
    # in string split by spaces,
    return result


# print(backward_string_by_word('hello    world'))

def backward(str):
    if str == '':
        return ''
    newstring = str[::-1].split(' ')  # this fails because if there is only one space, then it will get rid of it
    result = ''
    print(newstring)
    i = (len(newstring) - 1)
    while i != -1:
        if newstring[i] == '':
            result = result + " "
        result = result + newstring[i]
        i -= 1
    return result


# print(backward('hello world'))


def left_join(str):
    return (",".join(str)).replace("right", "left")  # puts a comma between every iterable item in str iterable, and
    # replaces right with left


# print(left_join(("bright aright", "ok")))


def bigger_price(num, dict):
    i = 0  # makes iterable
    counterlist = []  # makes list to sort through
    newlist = []  # makes list that will be returned
    index = 0
    for x in dict:  # for each item in list, put iterable 'i' in to keep track of index, and
        counterlist.append((i, list(dict[i].values())[1]))  # inputs tuple of index and value of price into new list
        i += 1  # to keep track of index
    counterlist.sort(key=lambda counterlist: counterlist[1], reverse=True)  # sorts the list based off of value of
    # second value in tuple, and puts into reverse from greatest to smallest
    i = 0  # reset iterable to keep track of index
    for x in range(num):  # for each value in range of first inputted number, add it to new list
        newlist.append(dict[counterlist[i][0]])
        i += 1
    return newlist


"""print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))"""


def between_markers(str, first, second):
    if first not in str and second not in str:  # checks if first and second are not in string, if so, return string
        return str
    if first not in str:  # if first marker is not in string, print everything before second marker
        m = re.search('.*.{}'.format(second), str)  # makes an object to use functions on
        return str[:m.end() - (len(second) - 1)]
    elif second not in str:  # if second marker isnt in string, print everything after first marker
        m = re.search('{}.*.'.format(first), str)  # .*. will print everything passed certain mark, a fill in character
        return str[m.start() + len(first) - 1:]  # m is the object, .start finds the start of the index it found the
        # marker at, and .end finds the ending index of the other market
    elif first and second in str:  # if both markers are in string, go as normal
        if str.index(first) > str.index(second):  # makes sure second marker isn't before first marker, if so return ""
            return ""
        m = re.search(('{}.*.{}'.format(first, second)), str)  # finds the text between the two markers
        return str[m.start() + (len(first)):m.end() - (len(second))]  # prints the index values between markers


# print(between_markers("No[/b] hi","[b]","[/b]"))

def between_markers1(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


def return_nonunique(lis):
    newlist = []  # creating empty list
    for m in lis:
        if lis.count(m) > 1:  # for each item in list, count the amount the item is in the list
            newlist.append(m)  # if greater than 1 time in list, append it to new list and return
    return newlist


# print(return_nonunique([1, 2, 3, 1, 3]))

def popular_words(text, words):
    stringlist = text.lower().split()  # makes a new list to make all words in string lowercase to check easier
    result = {}  # makes dictionary
    for n in words:  # for each item in given array
        result[n] = stringlist.count(n)  # adds the amount of items in list to dictionary based on given words list
    return result


# print(popular_words("When I was One I had just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near']))


# find the second occurance of given symbol in given text

def second_index(text, symbol):
    if text.count(symbol) >= 2:  # if the symbol you are searching for appears twice, continue
        index = list(text).index(symbol, list(text).index(symbol) + 1)  # finds index of first occurance and then
        # gives arguments for .index() function
        # to search for it after first occurance, therefore finds second
    else:
        return None
    return index


# print(second_index("three occurrences","r"))


def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))


# first key is the number of appearances ('-' inverts the list)
# second key applies when two elements are equally often in list, items.index sorts by first appearance in original list

# print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

def split_list(items):
    result1 = []  # creates two empty lists to append to
    result2 = []
    split = math.ceil(len(items) / 2)  # gets length of item list divided by two and rounded up to make sure the two
    # lists are cut in half and more in the first list than the second
    i = 0  # keeps iterable to keep track of index number
    while i < split:
        result1.append(items[i])  # creates first list
        i += 1
    while i < len(items):
        result2.append(items[i])  # second list
        i += 1
    return [result1, result2]


# print(split_list([1,2,3]))

def all_the_same(lis):
    i = 0  # first index
    l = 1  # second index
    while l < len(lis):  # while second index is less than total length of list
        if lis[i] != lis[l]:
            return False  # if the previous index does not equal this index, return false
        i += 1
        l += 1  # for next index
    return True  # if it makes it through, all items are equal


# print(all_the_same([1, 1, 1]))

# print inputted string in english language
def date_time(time: str):
    newtime = time.split()  # year              # month                 # day               #hour
    result = datetime.datetime(int(newtime[0][6:]), int(newtime[0][3:5]), int(newtime[0][0:2]), int(newtime[1][0:2]),
                               int(newtime[1][3:5]))  # minute
    # day, full month, year, hour, minutes
    if int(newtime[1][0:2]) != 1 and int(newtime[1][3:5]) != 1:
        return result.strftime("{} %B %Y year {} hours {} minutes").format(int(newtime[0][0:2]), int(newtime[1][0:2]),
                                                                           int(newtime[1][3:5]))
    elif int(newtime[1][0:2]) != 1 and int(newtime[1][3:5]) == 1:
        return result.strftime("{} %B %Y year {} hours {} minute").format(int(newtime[0][0:2]), int(newtime[1][0:2]),
                                                                          int(newtime[1][3:5]))
    elif int(newtime[1][0:2]) == 1 and int(newtime[1][3:5]) == 1:
        return result.strftime("{} %B %Y year {} hour {} minute").format(int(newtime[0][0:2]), int(newtime[1][0:2]),
                                                                         int(newtime[1][3:5]))
    elif int(newtime[1][0:2]) == 1 and int(newtime[1][3:5]) != 1 and int(newtime[1][3:5]) != 1:
        return result.strftime("{} %B %Y year {} hour {} minutes").format(int(newtime[0][0:2]), int(newtime[1][0:2]),
                                                                          int(newtime[1][3:5]))


# used .format to make sure there are no leading zeros since int() takes away them

# each if/elif makes sure if the input is 1, it says minute, and if anything else its minutes according to conditions
# same thing for hour/hours

# print(date_time("09.01.2000 10:02"))

def replace_last(line):
    if len(line) == 0:
        return []
    result = [line[-1]]
    i = 0
    while i < len(line) - 1:
        result.append(line[i])
        i += 1
    return result


# print(replace_last([2, 3, 4, 1]))


def index_power(array, n):
    return array[n] ** n if len(array) > n else -1  # return the array of index 'n' and do to the power of n
    # only if the length of the array is greater than n, else return -1


# print(index_power([1, 2, 3, 4], 2))

def is_majority(items):
    if items.count(True) > items.count(False):  # if the amount of 'True' is larger than amount of 'False' return True
        return True
    else:
        return False


# print(is_majority([True, True, False, True, False]))

def sum_light(els) -> int:
    i = 0  # first index
    l = 1  # second index
    result = 0  # result to keep track of for seconds passed
    while l < len(els):  # makes sure it stops before getting past length of list of datetime objects
        result += (els[l] - els[i]).total_seconds()  # subtracting future date from passed date and getting the seconds
        i += 2  # skipping two index to get the next two comparisons
        l += 2
    return int(result)  # returning integer version of total seconds passed


"""print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 13, 11, 0, 0),
    ]))"""


def sum_light_2(*args):
    i = 0
    l = 1
    result = 0
    if args[1]:
        result = 0
        while l < len(args[0]):
            result += (args[0][l] - args[0][i]).total_seconds() - (args[1]).second
            i += 2
            l += 2
        return int(result)
    while l < len(args[0]):
        result += (args[0][l] - args[0][i]).total_seconds()
        i += 2
        l += 2
    return args[0][0]

print(sum_light_2([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
    datetime(2015, 1, 12, 10, 0, 5)))
