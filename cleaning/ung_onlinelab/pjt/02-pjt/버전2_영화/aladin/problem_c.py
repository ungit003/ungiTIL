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

def get_bestseller_books(response):
    # 여기에 코드를 작성합니다.
    book_list = []
    for i in range(len(response['item'])) :
        list_dict = {'제목': response['item'][i]['title'], '판매지수': response['item'][i]['salesPoint']}
        book_list.append(list_dict)
        
    pld = {}
    for i in range(len(book_list)) :
        pld[book_list[i]['판매지수']] = book_list[i]
        
    guide = list(pld.keys())
    guide.sort()
    guide.reverse()
    
    ans = []
    for g in guide:
        ans.append(pld[g])
        
    return ans[0:5]

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_bestseller_books(response))
