
#Problem 1
# A program to get the initials
# of a proper name
def get_initials(s):
    sep_part = s.split(' ')
    for x in sep_part:
        print("{}.".format(x[0].capitalize()), end='')
        # end=' ' print on the same line

#Problem 2
#a list of months
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
#A program that prints a date
#in a specified form
def date_printer():
    #prompt user to enter a date
    date = input("Enter a date in the form dd/mm/yyyy: ")
    #seperate the date by "/"
    date_sep = date.split("/")
    #print the input date in the form March 12, 2020
    print("{0} {1}, {2}".format(months[int(date_sep[1])-1], int(date_sep[0]), date_sep[2]))

    






def main():

    date_printer()


main()
