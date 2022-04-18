import datetime

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
        i = 1       # sets iterable to 1
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
    newlist=[]
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
    return [ch1+ch2 for ch1, ch2 in zip(a[::2],a[1::2]+'_')]  # ::2 means two increments

# print(split_pairs2('aa'))

def beginning_zeros(str):
    i=0
    for s in str:
        if s == '0':
            i+=1
        else:
            return i
    return i

# print(beginning_zeros('000100'))


def nearest_value(values: set, i: int) -> int:
    return min((abs(n-i), n) for n in values)[1]    # makes a list of tuples, with the difference of the iterable
                                                    # subtracted by given number, and returns the min(), the smallest
                                                    # number found in the list of tuples and then gives the second index
                                                    # which is the number that created smallest number
# print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

def between_markers(str, m, n):
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

    return string_found

# print(between_markers('What is >apple<', '>', '<'))

def correct_sentance(str):
    result = str[0].upper() + str[1:]  # makes sure first index is upper
    if result[-1] != '.':  # if the last index is not a period, add it and then return result
        result = result+'.'
    return result

# print(correct_sentance("greetings, friends"))

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
    i = 0                           # setting iterable in case you have to switch index numbers
    if '.' in str:
        str = str.split(".")        # splits hello.world example
        while "" in str:            # removes white space
            str.remove("")
    else:                           # if no . in str, normal split
        str = str.split()
    if "," in str[i]:               # if there is a comma, get rid of it
        str[i] = str[i].replace(",", "")
    result = ""                     # making empty string to help with white space
    str[i] = str[i].strip()         # gets rid of beginning and ending whitespace
    for m in str[i]:                # for each item in str[i], add to new string
        if m == " ":                # if 'm' reaches a whitespace, it has hit second word,
                                    # which means it should stop and return result
            break
        result = result+m   # keeps adding iterable to new string to form new word in new string variable
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
    str=str.split(" ")
    newstring=""
    for s in str:
        newstring = newstring + s[::-1]
    return newstring

print(backward_string_by_word('hello    world'))
