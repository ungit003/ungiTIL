import json
from pprint import pprint


def book_info(book, categories):
    info = {}
    info['id'] = book['id']
    info['title'] = book['title']
    info['author'] = book['author']
    info['priceSales'] = book['priceSales']    
    info['description'] = book['description']
    info['cover'] = book['cover']
    info['categoryName'] =[]
    for j in range(len(book)) : 
        if categories[j]['id'] == book['categoryId'][0] :
            num_name = categories[j]['name']
            info['categoryName'].append(num_name)
    for j in range(len(book)) : 
        if categories[j]['id'] == book['categoryId'][1] :
            num_name = categories[j]['name']
            info['categoryName'].append(num_name)
    return info
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
