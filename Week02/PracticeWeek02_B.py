

#Declare a dictionary of morse code
morse_code_dic = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-',
            'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--',
            'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', ', ': '--..--', '.': '.-.-.-',
            '?': '..--..'
    }


# Function to convert
# english to morse code
def english_to_morsecode(s):
    #Declare an empty string to store the converted morse code
    morse_code = ""
    # for each letter in given sentence
    #    convert it to correspoding morse code
    for x in s:

        if x != " ":
            morse_code += morse_code_dic[x] + " "
        else:
            morse_code += " "
    return morse_code

# Function to convert a series of morse code
# back to english
def morsecode_to_english(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            #           # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                #                 # accessing the keys using their values (reverse of encryption)
                key_list = list(morse_code_dic.keys())
                value_list = list(morse_code_dic.values())
                index = value_list.index(citext)

                decipher += key_list[index]
                citext = ''

    return decipher







