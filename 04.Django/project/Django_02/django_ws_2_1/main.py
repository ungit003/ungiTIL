import requests
from pprint import pprint

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbung031138002'
params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'MaxResults': 50,
    'start': 1,
    'SearchTarget': 'Book',
    'Output': 'JS',
    'Version': 20131101,
}

r = requests.get(API_URL, params).json()
tar = r['item']
# print(tar)
# print(len(tar))
ans = []
for t in tar:
    summary = {}
    summary['국제 표준 도서 번호'] = t['isbn']
    summary['저자'] = t['author']
    summary['제목'] = t['title']
    summary['출간일'] = t['pubDate']
    ans.append(summary)
pprint(ans)