



# DRIVER LICENSE EXAM PROGRAM (Not fully updated)
# File name format:
#      correct answer: answer.txt
#      questions: questions.txt
#      user answer: userans_userid.txt  where userid is the id given to
#                                       the user when entering the exam
# Main functions:
# 1. Take an exam:
#    1.a Enter id to store result in a file
#    1.b Load questions and allowing inputting answer
#    1.c Display result if needed
# 2. See result of an take attempt:
#    2.a Enter id to get the result file of the user
#    2.b Display result
#    2.c Compare result and decide if the user passed or failed
# 3. Quit




# Program to let user make an exam attempt
def license_exam_program():
    while True:
        print('>> 1. Take an exam')
        print('>> 2. See available result')
        print('>> 3. Quit')
        while True:
            try:
                option = int(input('Choose 1/2/3: '))
                if option not in [1,2,3]:
                    print('Re-input the option!')
                    continue
                if option == 1:
                    take_exam()
                    continue
                if option == 2:
                    see_available_result()
                    continue
                if option == 3:
                    break
            except ValueError:
                print('Re-input the option!')
                continue
        break
    print('See you next time!')





# Function to handle a exam attempt
def take_exam():
    while True:  # Keep getting input from the user
        try:
            user_id = int(input('Enter your exam id (10 digits): '))
            if len(str(user_id)) != 10:
                print('Invalid id!')
                continue
            else:
                break
        except ValueError:
            print('Re-input the id!')
            continue
    print('<<<<<<<<<<< START >>>>>>>>>>')
    questions_file = open('questions.txt', 'r')
    user_fname = 'userans_' + str(user_id) + '.txt'
    user_answer_file = open(user_fname, 'a')
    i = 1

    # Load questions from file and allow entering answers after each question
    for line in questions_file:
        if line != '\n':
            print(line.rstrip('\n'))
        else:
            while True: # Keeping asking for valid answer
                try:
                    user_ans = str(input('>> Enter your answer: '))
                    if len(user_ans) != 1 or user_ans.upper() not in 'ABCD':
                        print('Invalid answer! Re-input answer!')
                        continue
                    else: # write user answer to a file
                        print()
                        user_answer_file.write('{}. {} \n'.format(i, user_ans.upper()))
                        i += 1
                        break
                except ValueError:
                    print('Re-input answer!')
                    continue

    questions_file.close()
    user_answer_file.close()

    while True: #asking for the need to see the result immediately
        try:
            opt = str(input('Wanna see your result right now? [Y/N]: '))
            if len(opt) != 1 or opt.upper() not in 'YN':
                print('Re-input [Y/N]!')
                continue
            else:
                display_result(user_id)
                break
        except ValueError:
            print('Re-input [Y/N]!')
            continue

# Function to get result for an taken attempt
def see_available_result():
    print('<<<<<<<<<<< SEE RESULT >>>>>>>>>>')
    while True:  # Keep getting input from the user
        try:
            user_id = int(input('Enter your exam id (10 digits): '))
            if len(str(user_id)) != 10:
                print('Invalid id!')
                continue
            else:
                break
        except ValueError:
            print('Re-input the id!')
            continue
    display_result(str(user_id))



# Function to load any file which contain a list of answer in secified format
def load_answer_from_file(file_name):
    try:
        file = open(file_name, 'r')
    except ValueError:
        print(file_name, ': file not found')
    answer = []
    for line in file:
        line.strip('\n')
        for char in line:
            if char.isalpha() and char.upper() in 'ABCD':
                answer.append(char)
    file.close()
    return answer

# Function to display the exam result of the user, given a user id
def display_result(user_id):
    print('<<<<<<<<<< RESULT >>>>>>>>>>')
    user_answer = 'userans_' + str(user_id) + '.txt'
    user_answer_list = load_answer_from_file(user_answer)
    correct_answer_list = load_answer_from_file('answer.txt')
    question_file = open('questions.txt', 'r')

    i = 0
    for line in question_file:
        if line != '\n':
            print(line.rstrip('\n'))
        else:
            c = correct_answer_list[i].upper()
            u = user_answer_list[i].upper()
            status = 'Correct' if u == c else 'Wrong'
            print('{}|{}|{} \n'.format(('Correct Answer: ' + c), ('Your answer: ' + u), status ))

            i += 1
    question_file.close()
    compare_result(user_answer_list, correct_answer_list)

def compare_result(correct_ans : list , user_answer : list):
    # if len(correct_ans) != len(user_answer):
    #     print('Cannot compare result')
    # else:
        correct_num = 0
        wrong_ans = []
        n = len(correct_ans)
        for i in range(0, n):
            if correct_ans[i] == user_answer[i]:
                correct_num += 1
            else:
                wrong_ans.append(i+1)
        if correct_num >= 15:
            result = 'PASSED'
        else:
            result = 'FAILED'
        print('You have {} the exam with {}/20 correct answers.'.format(result, correct_num))
        if len(wrong_ans) > 0:
            print('The id of wrongly answered questions: ', wrong_ans)
        # print('The id of wrongly answered questions: ', wrong_ans if len(wrong_ans) > 0 else 'none')


if __name__ == '__main__':
    license_exam_program()