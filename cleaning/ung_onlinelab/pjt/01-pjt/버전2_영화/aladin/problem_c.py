import json
from pprint import pprint


def books_info(books, categories):
    info_box = []
    for i in range(len(books)) :
        info = {}
        info['id'] = books[i]['id']
        info['title'] = books[i]['title']
        info['author'] = books[i]['author']
        info['priceSales'] = books[i]['priceSales']    
        info['description'] = books[i]['description']
        info['cover'] = books[i]['cover']
        # 북스-카테고리아이디-넘버 == 카테고리-아이디:넘버 -> 카테고리 네임을  카테고리네임에 저장
        info['categoryName'] = [] #categoryId books[i]
        for j in range(len(books)) : 
            if categories[j]['id'] == books[i]['categoryId'][0] :
                num_name = categories[j]['name']
                info['categoryName'].append(num_name)
        for j in range(len(books)) : 
            if categories[j]['id'] == books[i]['categoryId'][1] :
                num_name = categories[j]['name']
                info['categoryName'].append(num_name)
        info_box.append(info)
            
        #     for category_id in books :
        #         num_name = []
        #         if category_id['categoryId'] == categories['name'] :
        #             info['categoryName'].append(num_name)
        # for category_Id in books['categoryId']:
        #     for category in categories:
        #         if category['id'] == category_Id:
        #             info['categoryName'].append(category['name'])
        #             break
   
        
        
    return info_box


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
