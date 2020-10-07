

# Function to get answer from a txt file
def get_answer_from_file(answer_file: str):

    answer = open(answer_file, 'r+')
    b = []
    for line in answer:
        for x in line.rstrip('\n'):
            if x.isalpha() and x.upper() in 'ABCD':
                b.append(x.upper())
    answer.close()
    return b


def get_user_answer_input(user_id):
    file_name = 'user_answer_' + str(user_id)
    user_answer = open(file_name, 'a')
    print('Enter answer for each question (A/B/C/D): ')
    for i in range(1, 21):

        while True:  # Keep getting input from the user
            try:
                answer = str(input('Q{}: '.format(i)))
                if len(answer) != 1 or answer.upper() not in 'ABCD':
                    print('Enter a valid answer: ')
                    continue
                else:
                    break
            except ValueError:
                print('Error input! Enter a valid answer: ')
                continue

        user_answer.write('{}. {} \n'.format(i, answer))
    return user_answer


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
            result = 'passed'
        else:
            result = 'failed'
        print('You have {} the exam with {}/20 correct answers.'.format(result, correct_num))
        if len(wrong_ans) > 0:
            print('The id of wrongly answered questions: ', wrong_ans)
        # print('The id of wrongly answered questions: ', wrong_ans if len(wrong_ans) > 0 else 'none')



def exam_taking():
    while True:  # Keep getting input from the user
        try:
            user_id = int(input('Enter your id (10 digits): '))
            if len(str(user_id)) != 10:
                print('Invalid id!')
                continue
            else:
                break
        except ValueError:
            print('Re-input id!')
            continue


    get_user_answer_input(user_id)



def see_result(user_id, org_answer):
    user_answer = 'user_answer_' + user_id
    user_answer_list = get_answer_from_file(user_answer)
    correct_answer_list = get_answer_from_file(org_answer)
    return compare_result(user_answer_list, correct_answer_list)










