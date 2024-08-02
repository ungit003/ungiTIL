import json
from pprint import pprint


def new_books(books):
    # 여기에 코드를 작성합니다.
    id_box = []
    for i in range(len(books)) :
        book_id = books[i]['id']
        id_box.append(book_id)
    
    date_dict = {}
    for num in id_box :
        data_books = open(f'data/books/{num}.json', encoding='utf-8')
        book_info = json.load(data_books)
        date_dict[book_info['title']] = book_info['pubDate']

    year_2023 = []
    for key, value in date_dict.items() :
        year = value[:4]
        year = int(year)     
        if year == 2023 :
            year_2023.append(key)
    # for i in range(len(date_dict)) :
    #     year = date_dict[i][:4]
    #     year = int(year)
    #     if year == 2023 :
    #         year_2023.append(list(date_dict.keys())[i])
    return year_2023


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
