

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
        info.append(line.rstrip())
    f.close()
    return info


# Load all books from the given info list
# input: info list loaded from file
# output: a book list
def get_books(info: list):
    if len(info) == 0:
        print('no info available')
        return
    books = []
    for item in info:
        if info.index(item) % 3 == 1 and str(item) not in books:
            books.append(item)
    return books



# Get a dictionary for users' ratings
# input: info list , book list
# output: a dictionary containing user names and their ratings for books
def get_user_ratings(info: list, books: list):
    if len(info) != 0 and len(books) != 0:
        user_rating_dict = {}
        # add users as keys to the rating_dict
        for item in info:
            if info.index(item) % 3 == 0:
                user_rating_dict[item] = [0] * len(books)

        # Updating user ratings
        for i in range(0, len(info)):
            if i % 3 == 0:                                              # index of user name
                book_index = books.index(info[i+1])                     # get index of a book in books list
                user_rating_dict[info[i]][book_index] = int(info[i+2])
    return user_rating_dict


def recommendations(user_rating_dict: dict, books: list):
    username = str(input('user? '))
    if username not in user_rating.keys():
        averages(user_rating_dict, books)




# Function to get a list containing book title and its average rating
def averages(user_rating_dict: dict, books: list):
    average_list = []
    ratings = user_rating_dict.values()

    for i in range(0,len(books)):
        total_rate = 0
        total_user = 0
        for each in ratings:
            if each[i] != 0:
                total_user += 1
                total_rate += each[i]
        average_list.append([total_rate/total_user, books[i]])

    sorted_ave = sorted(average_list, key= lambda item: item[0], reverse=True)

    for each in sorted_ave:
        print(each[1], ' ', each[0])












# Main function to run the program
def book_recommender(info: list, books: list, user_rating_dict: dict):
    while True:
        try:
            print('Welcome to the CSC110 Book Recommnder . Type the word in the' ,
                'left column to do the action on the right.',
                'recommend: recommend books for a particular user',
                'averages : ouput the average ratings of all books in the system',
                 'quit: exit the program', sep = '\n')
            user_choice = str(input('next task? '))
            uc = user_choice.upper()


            if uc not in ['RECOMMEND', 'AVERAGES', 'QUIT']:
                print('Please re-input')
                continue

            if uc == 'RECOMMEND':
                recommendations(user_rating_dict, books)
                print()
                continue

            if uc ==  'AVERAGES':
                averages(user_rating_dict, books)
                print()
                continue

            if uc =='QUIT':
                print('See your next time')
                break

        except ValueError:
            print('Please re-input')
            continue


# Run the program HERE
if __name__ == '__main__':
    info = load_info_from_file('ratings-small.txt')
    # print(info)
    books = get_books(info)
    # print(books)
    user_rating = get_user_ratings(info, books)
    # print(user_rating)

    # average_res = averages(user_rating, books)
    # print(average_res)

    book_recommender(info, books, user_rating)

    # print('averages'.upper)










