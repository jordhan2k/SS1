import os

######### BOOK RECOMMENDER ############
## Author: Hoang Tien Dung - 1801040037



# Load all information from  ratings file
# input: the file name (a text file)
# output: a list containg all information (e.g [username, book, rating, ...])
def load_info_from_file(file_name: str):
    try:  # try opening a file
        f = open(file_name, 'r')
    except ValueError:
        print('File not found')
    info = []
    for line in f:
        info.append(line.strip('\n'))
    f.close()
    return info


# Load all books from the given info list
def get_books(info: list):
    if len(info) == 0:
        print('no info available')
        return
    books = []
    for item in info:
        if info.index(item) % 3 == 1 and item not in books:
            books.append(item)
    return books



# Get a dictionary for users' ratings
def get_user_ratings(info: list, books: list):
    if len(info) != 0 and len(books) != 0:

        init_ratings = [0] * len(books)
        user_rating_dict = {}

        # add users as keys to the rating_dict
        for item in info:
            if info.index(item) % 3 == 0:
                user_rating_dict[item] = init_ratings



        # Updating user ratings
        for i in range(0, len(info)):
            if i % 3 == 0:                                              # index of user name
                book_index = books.index(info[i+1])                     # get index of a book in books list
                print(info[i], ' ', info[i+1], ' ', info[i+2])
                user_rating_dict[info[i]][book_index] = int(info[i+2])
                ## THE ABOVE CODES DON NOT WORK PROPERLY  ##
    return user_rating_dict


def recommend(user_rating_dict: dict):
    username = str('user? ')




def averages():
    return None





def book_recommender():
    while True:
        try:
            print('Welcome to the CSC110 Book Recommnder . Type the word in the' ,
                'left column to do the action on the right.',
                'recommend: recommend books for a particular user',
                'averages : ouput the average ratings of all books in the system',
                 'quit: exit the program', sep = '\n')
            user_choice = str(input('next task?'))

            if user_choice.upper not in ['RECOMMEND', 'AVERAGES', 'QUIT']:
                print('Please re-input')
                continue
            if user_choice.upper == 'RECOMMEND':
                recommend()
                continue
            if user_choice.upper == 'AVERAGES':
                averages()
                continue
            if user_choice.upper == 'QUIT':
                print('See your next time')
                break
        except ValueError:
            print('Please re-input')
            continue















if __name__ == '__main__':

    ## KEEP THIS LINE ONLY ##
    # book_recommender()
    #########################


    info = load_info_from_file('ratings-small.txt')
    # print(info)
    books = get_books(info)
    # print(books)
    user_rating = get_user_ratings(info, books)
    print(user_rating)










