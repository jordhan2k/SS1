import os




# Load all information from  ratings file
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
            if i % 3 == 0:
                book_index = books.index[info[i+1]]
                user_rating_dict[info[i]][book_index] = info[i+2]




    return user_rating_dict












    return None




if __name__ == '__main__':
    info = load_info_from_file('ratings-small.txt')
    books = get_books(info)
    print(books)
    user_rating = get_user_ratings(info, books)
    print(user_rating)





