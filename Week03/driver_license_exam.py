



# Function to get answer from a txt file
def get_answer(answer_file: str):
    answer = open(answer_file, 'r+')
    b = []
    for line in answer:
        for x in line:
            if x.isalpha() and x.upper() in 'ABCD':
                b.append(x.upper())
    return b




def get_user_answer_input():
    user_answer = open('user_answer.txt', 'r+')
    print('Enter answer for each question: ')
    for i in range (1, 21):
        a = input('Q{}: '.format(i)).upper()

        user_answer.write('{0}. {1} \n'.format(i, a))
    return user_answer


def compare_result(correct_ans : list , user_answer : list):


    if len(correct_ans) != len(user_answer):
        return 'Cannot compare result'
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


corr = get_answer('org_answer.txt')
user = get_answer('user_answer.txt')
compare_result(corr, user)