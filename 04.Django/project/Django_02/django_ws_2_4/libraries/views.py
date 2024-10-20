import requests
from django.shortcuts import render
from pprint import pprint

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbung031138002'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)
    # pprint(result)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)


def bestseller(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
            'salesPoint': item['salesPoint'],
        }
        if 'bestDuration' in item:
                info['bestDuration'] = item['bestDuration']
        result.append(info)
    result.sort(key=lambda x: x['salesPoint'], reverse=True)
    pprint(result)
    context = {
        'result': result
    }
    return render(request, 'bestseller.html', context)