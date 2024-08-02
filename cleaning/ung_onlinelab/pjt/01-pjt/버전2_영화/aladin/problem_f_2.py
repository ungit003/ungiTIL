import json


def sorted_cs_books_by_price(books, categories):
    # 여기에 코드를 작성합니다.
    book_box = {}
    for i in range(len(books)) :
        for j in range(2) :
            if books[i]['categoryId'][j] == 2721 :
                # book_box[books[i]['title']] = books[i]['priceSales']
                book_box[books[i]['priceSales']] = books[i]['title']

    # book_box_re = []
    # max_price = max(book_box.values())
    # for key, value in book_box.items() :
    #     if value == max_price :
    #         book_box_re.append(key)
    #     else :
    #         book_box_re.append(key)
    # return book_box_re
    org_bb = []
    nums = len(book_box)
    keys = list(book_box.keys())
    keys.sort()
    
    for i in range(nums) :
        org_bb.append(book_box[keys[nums-i-1]])
    
    return org_bb
        
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
