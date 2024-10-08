import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
        'ttbkey': 'ttbung031138001',
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,
}

response = requests.get(URL, params=params).json()


def get_best_review_books(response):
    # 여기에 코드를 작성합니다.
    book_list = []
    for i in range(len(response['item'])) :
        if response['item'][i]['customerReviewRank'] >= 9 :
            book_name = response['item'][i]
            book_list.append(book_name)
    return book_list

# result = get_best_review_books(response)
# pprint(result)

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_best_review_books(response))
