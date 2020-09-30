
# Function to separate a number into single digits
# and save them to a 12-item array
# e.g. :
#    1245345 -> [0,0,0,0,0,1,2,4,5,3,4,5]
def get_separate_number():
    s =int(input('Enter a sum of money that need converting to text: '))
    # Fill the number with 0 before spliting
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
    return second_array



list_number_one = ['một', 'hai' , 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
list_number_two = ['mười', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']

# Function to get the
#  Pass in separate number

def get_initial_number_str(sn: list):

    initial_number = []
    for i in range(0, len(sn)):

        if i in [0, 3]:
            # ex:
            if sn[i] == 0:
                initial_number.append('')
            else:
                # ex sn[i] == 9 -> append(list_number_one[8]) -> append 'chín'
                initial_number.append(list_number_one[sn[i]-1])
        if i in [1, 4]:
            if sn[i] == 0:
                if sn[i-1] != 0 and sn[i+1] != 0:
                    initial_number.append('lẻ')
                else:
                    initial_number.append('')
            else:
                initial_number.append(list_number_two[sn[i] - 1])

        if i in [2, 5, 8, 11]:
            if sn[i] == 0:
                initial_number.append('')
            else:
                if sn[i-1] > 1 and sn[i] == 1:
                    initial_number.append('mốt')
                if sn[i] == 5 and sn[i-1] != 0:
                    initial_number.append('lăm')
                else:
                    initial_number.append(list_number_one[sn[i]-1])

        if i in [6, 9]:
            if sn[i] == 0:
                if sn[i+1] == 0:
                    initial_number.append('')
                else:
                    if sn[i-2] == 0 and sn[i-1] == 0 and sn[i+1] != 0:
                        initial_number.append('')
                    else:
                        initial_number.append('không trăm')
            else:
                initial_number.append(list_number_one[sn[i]-1])

        if i in [7, 10]:
            if sn[i] == 0:
                if sn[i+1] == 0:
                    initial_number.append('')
                else:
                    if sn[i-2] == 0 and sn[i-1] == 0 and sn[i+1] != 0:
                        initial_number.append('')
                    else:
                        initial_number.append('lẻ')
            else:
                initial_number.append(list_number_two[sn[i]-1])

    # return a list of initial numbers
    return initial_number



def get_number_unit(sn: list, sca: list):
    number_unit = []
    for i in range(0, len(sn)):
        if i in [0, 3, 6, 9]:
            if sn[i] == 0:
                number_unit.append('')
            else:
                number_unit.append('trăm')

        if i in [1, 4, 7, 10]:
            if sn[i] == 0:
                number_unit.append('')
            else:
                if sn[i] == 1:
                    number_unit.append('')
                else:
                    number_unit.append('mươi')

        if i == 2:
            if sn[i] == 0 and sca[i] == 0:
                number_unit.append('')
            else:
                number_unit.append('tỷ')

        if i == 5:
            if sn[i] == 0 and sca[i] == 0:
                number_unit.append('')
            else:
                number_unit.append('triệu')

        if i == 8:
            if sn[i] == 0 and sca[i] == 0:
                number_unit.append('')
            else:
                number_unit.append('ngàn')

        if i == 11:
            number_unit.append('')

    return number_unit

# Function to convert a number
# to text and text with monetary curency
def number_to_text():
    a = get_separate_number()
    b = get_second_array(a)
    c = get_initial_number_str(a)
    d = get_number_unit(a, b)

    s = []
    for i in range(0, len(a)):
        if c[i] != '':
            s.append(c[i])
        if d[i] != '':
            s.append(d[i])

    print(s)
    s = ' '.join(s).replace('  ', '').split()
    s[0] = s[0].capitalize()
    s = ' '.join(s)

    print('In text: ', s)
    print('In text with currency: ', s,'đồng./.')



number_to_text()