import json
from pprint import pprint

def best_book(books):
    # 여기에 코드를 작성합니다.
    id_box = []
    for i in range(len(books)) :
        book_id = books[i]['id']
        id_box.append(book_id)
    
    lank_dict = {}
    for num in id_box :
        data_books = open(f'data/books/{num}.json', encoding='utf-8')
        book_info = json.load(data_books)
        lank_dict[book_info['title']] = book_info['customerReviewRank']
        
    highest_value = max(lank_dict.values())
    # highest_key = [key for key, value in lank_dict.items() if value == highest_value]
    for key, value in lank_dict.items() :
        if value == highest_value :
            highest_key = key
    return highest_key
    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
