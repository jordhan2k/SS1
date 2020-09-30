

#  Separate a number into separate digits and assign it to a e
# return a dictionary of
# Array with Row 9
def get_separate_number():
    s =int(input('Enter a sum of money: '))
    s = str(s).zfill(12)
    sep_number_str = list(s)
    sep_number = []
    for x in sep_number_str:
        sep_number.append(int(x))
    return sep_number


def get_second_array(s : list):
    second_array = [s[0] , s[0] + s[1], s[0] + s[1] + s[2],
                    s[3], s[3] + s[4], s[3] + s[4] + s[5],
                    s[6], s[6] + s[7], s[6] + s[7] + s[8],
                    s[9], s[9] + s[10], s[9] + s[10] + s[11],
                    ]
    print(second_array)






list_number_one = ['một', 'hai' , 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
def get_initial_number(sep_number: list):

    for x in sep
    if




    # return a list of initial numbers
    return






# Tính mươi, tỉ, triệu, nghìn
#  index: index of the number
#  y is the number
def get_number_unit(index,number):
    s = ''
    x = index + 1
    if x in [1, 4, 7, 10]:
        if number != 0:
            s += 'trăm'
    if x in [2, 5, 8, 11]:
        if number == 0:
            s += ''
        else:
            if number == 1:
                s += ''
            else:
                s += 'mươi'
    if x == 1000000000:
        s+= 'tỷ'
    if x == 1000000:
        s += 'triệu'
    if x == 1000:
        s += 'nghìn'

    return s






