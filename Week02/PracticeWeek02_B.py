
# Function to convert an English sentence to morse code
#
#
#

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
def english_to_morsecode(s):
    morse_code = ""
    for x in s:
        if x != " ":
            morse_code += morse_code_dic[x] + " "
        else:
            morse_code += " "
    return morse_code

def morsecode_to_english(s):






if __name__ == '__main__':


    s = input("Enter a string: ")
    morse_code_converter(s)

