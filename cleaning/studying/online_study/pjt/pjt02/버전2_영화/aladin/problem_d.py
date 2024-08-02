import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

def get_author_other_books(title):
    # 여기에 코드를 작성합니다.
    params = {
        'ttbkey': 'ttbung031138001',
        'Query': title,
        'QueryType': 'book',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,
    }
    response = requests.get(URL, params=params).json()
    try :
        a1 = response['item'][0]['author']
    except :
        return None
    # print(a1)
    a2 = a1.split()
    # print(a2)
    a3 = a2[:2]
    # print(a3)
    info_author = ' '.join(a3)
    # print(info_author)
    params2 = {
        'ttbkey': 'ttbung031138001',
        'Query': info_author,
        'QueryType': 'author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,
    }
    response2 = requests.get(URL, params=params2).json()
    
    title_list = []
    for i in range(len(response2['item'])):
        title_list.append(response2['item'][i]['title'])
        
    title_list2 = set(title_list)
    title_list3 = list(title_list2)    
    b1 = title_list.index(f'{title}')
    # print(title)
    # print(b1)
    del title_list[b1]
    
    ans = {}
    ans[f'"{title}"의 저자 "{info_author}"의 다른 도서 목록'] = title_list3[0:5]
    return ans


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_other_books('베니스의 상인'), width=120)
    pprint(get_author_other_books('죄와 벌'), width=120)
    pprint(get_author_other_books('*'), width=120)
