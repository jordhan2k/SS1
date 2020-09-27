# Problem 1
# A program to get the initials
# of a proper name
from setuptools.command.test import test


def get_initials(s):
    sep_part = s.split(' ')
    for x in sep_part:
        print("{}.".format(x[0].capitalize()), end='')
        # end=' ' print on the same line


# Problem 2
# a list of months
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]


# A program that prints a date
# in a specified form
def date_printer():
    # prompt user to enter a date
    date = input("Enter a date in the form dd/mm/yyyy: ")
    # seperate the date by "/"
    date_sep = date.split("/")
    # print the input date in the form March 12, 2020
    print("{0} {1}, {2}".format(months[int(date_sep[1]) - 1], int(date_sep[0]), date_sep[2]))


# Problem 3
# Function to translate a alphabetical phone number
# to a numerical one
def telephone_number_translate():
    phone_num = input("Enter the number in the format of XXX-XXX-XXXX: ")
    translated_phone = ''

    for char in phone_num:
        if char == 'A' or char == 'B' or char == 'C':
            translated_phone += '2'
        elif char == 'D' or char == 'E' or char == 'F':
            translated_phone += '3'
        elif char == 'G' or char == 'H' or char == 'I':
            translated_phone += '4'
        elif char == 'J' or char == 'K' or char == 'L':
            translated_phone += '5'
        elif char == 'M' or char == 'N' or char == 'O':
            translated_phone += '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            translated_phone += '7'
        elif char == 'T' or char == 'U' or char == 'V':
            translated_phone += '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            translated_phone += '9'
        elif char == '-':
            translated_phone += '-'
        else:
            translated_phone += char

    print(translated_phone)

#Problem 4
#
def sentence_capitalizeer():
    return


#Problem 5
vowel = ['u', 'e', 'o', 'a', 'i', 'U', 'A', 'E', 'I', 'O']
#Function to count vowels
# in a string
def vowel_count():
    string = input('Enter a string: ')
    count = 0
    for char in string:
        if char in vowel:
            count += 1
    print(count)
# Function to count consonants
# in a string
def consonant_count():
    string = input('Enter a string: ')
    count = 0
    for char in string:
        if char not in vowel:
            count += 1
    print(count)

#Problem 6
#Incompleted
# Function to find the most frequent character in a string
#
def most_frequent_char():
    string = input("Enter a string: ")

    dictionary = {}

    for character in list(string):
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1

    results = []

    for key, value in dictionary.items():
        results.append((value, key))



    for value, key in reversed(sorted(results)):
        print("Character", key, "occurred", value, "times")






#main procedure
def main():
   most_frequent_char()



main()
