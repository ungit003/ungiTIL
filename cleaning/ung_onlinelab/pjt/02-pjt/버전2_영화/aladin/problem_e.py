import requests
from pprint import pprint

URL1 = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
URL2 = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx'

# http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx
# ?ttbkey=[TTBKey]&itemIdType=ISBN&ItemId=[도서의ISBN]&output=xml
# &Version=20131101&OptResult=ebookList,usedList,reviewList


def get_users_books(title):
    # 여기에 코드를 작성합니다.
    params1 = {
        'ttbkey': 'ttbung031138001',
        'Query': title,
        'QueryType': 'book',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,
    }
    response1 = requests.get(URL1, params=params1).json()
    try :
        isbn13 = response1['item'][0]['isbn13']
    except :
        return None
    
    params2 = {
        'ttbkey': 'ttbung031138001',
        'itemIdType': 'ISBN13',
        'ItemId': isbn13,
        'output': 'js',
        'Version': 20131101,
        'OptResult': 'usedList'
    }
    response2 = requests.get(URL2, params=params2).json()
    a = response2['item'][0]['subInfo']['usedList']

    # 모든 아이템의 itemCount가 0인지 확인
    all_out_of_stock = all(item['itemCount'] == 0 for item in a.values())

    if all_out_of_stock:    
        return f'도서 "{title}"의 중고 재고가 없으며, 새 제품은 ""원에 판매 중입니다.'
    else:
        # 재고가 있는 아이템들 중에서 minPrice가 가장 낮은 것을 찾기
        min_price_key = None
        min_price_value = float('inf')  # 무한대 값을 초기값으로 설정

        for key, item in a.items():
            if item['itemCount'] > 0 and item['minPrice'] < min_price_value:
                min_price_value = item['minPrice']
                min_price_key = key

        # minPrice가 가장 낮은 아이템의 정보 반환
        if min_price_key:
            min_price_item = a[min_price_key]
            return f"도서의 가장 저렴한 중고는 {min_price_key}가 보유중이며 {min_price_item['minPrice']}원에 판매중입니다."
    


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
    pprint(get_users_books('로미오와 줄리엣'))
    pprint(get_users_books('*'))
