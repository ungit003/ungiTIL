import json
from pprint import pprint


def book_info(book):
    info = {}
    info['id'] = book['id']
    info['title'] = book['title']
    info['author'] = book['author']
    info['priceSales'] = book['priceSales']    
    info['description'] = book['description']
    info['cover'] = book['cover']
    info['categoryId'] = book['categoryId']
    return info
    
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
