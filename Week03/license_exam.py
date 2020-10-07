

def license_exam_program():
    while True:
        print('>> 1. Take an exam')
        print('>> 2. See available result')
        print('>> 3. Quit')
        while True:
            try:
                option = int(input('Choose 1/2/3: '))
                if option not in [1,2, 3]:
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
    return None








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
    while True:  # Keep getting input from the user
        try:
            exam_code = int(input('Enter your exam code (1/2/3/4): '))
            if len(str(exam_code)) != 1:
                print('Invalid id!')
                continue
            else:
                break
        except ValueError:
            print('Re-input id!')
            continue


    see_result(str(user_id), str(exam_code))




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

def see_result(user_id, exam_code):
    user_answer = 'code0' + exam_code + '_' + user_id + '.txt'
    exam_answer ='ans_code0' + exam_code + '.txt'
    user_answer_list = load_answer_from_file(user_answer)
    correct_answer_list = load_answer_from_file(exam_answer)
    return compare_result(user_answer_list, correct_answer_list)

def compare_result(correct_ans : list , user_answer : list):
    if len(correct_ans) != len(user_answer):
        print('Cannot compare result')
    else:
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


license_exam_program()