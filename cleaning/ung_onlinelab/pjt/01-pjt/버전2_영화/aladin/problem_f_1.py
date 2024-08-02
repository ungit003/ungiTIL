import json


def best_new_books(books):
    # 여기에 코드를 작성합니다.
    id_box = []
    for i in range(len(books)) :
        book_id = books[i]['id']
        id_box.append(book_id)
        
    date_rank_dict = []
    for num in id_box :
        data_books = open(f'data/books/{num}.json', encoding='utf-8')
        book_info = json.load(data_books)
        name_date_rank = [book_info['title'], book_info['pubDate'], book_info['customerReviewRank']]
        date_rank_dict.append(name_date_rank)
        
    rank_2023_dict = {}
    for data in date_rank_dict :
        if data[1][:4] == '2023' :
            rank_2023_dict[data[0]] = data[2]

    highest_value = max(rank_2023_dict.values())
        
    for key, value in rank_2023_dict.items() :
        if value == highest_value :
            highest_key = key
    return highest_key
        
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
