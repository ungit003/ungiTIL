from django.shortcuts import render
# from rest_framework.response import Response
from django.http import JsonResponse 
from rest_framework.decorators import api_view
import requests

from django.conf import settings

from .models import Weather
from .serializers import WeatherSerializer

# 1. OpenWeatherMap API로 부터 데이터 다운로드
# 2. 그대로 출력

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city_name = "Busan,KR"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = requests.get(url).json()
    return Response(response)


def save_data(request):
    # 1. API를 통해 데이터를 가져온다.
    api_key = settings.API_KEY
    city_name = "Busan,KR"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = requests.get(url).json()
    
    # 2. 원하는 필드(dt_txt, temp, feels_like)만 꺼내서 
    for li in response.get('list'): 
        dt_txt = li.get('dt_txt') 
        temp = li.get('main').get('temp') 
        feels_like = li.get('main').get('feels_like')
        
        # 3. "DB에 없다면" 저장한다.
        # 저장하기 위해 데이터를 '포장'해야한다
        # -> serializer 로 변환
        # -> 유효성 검증, 저장 등등 과정을 편하게 다룰 수 있다.   
        
        # DB에 이미 저장되어 있는 지 중복 확인
        if Weather.objects.filter(dt_txt=dt_txt, temp=temp, feels_like=feels_like).exists():
            continue
    
        save_data = {
            'dt_txt': dt_txt,
            'temp': temp,
            'feels_like': feels_like
            } 
    
        serializer = WeatherSerializer(data=save_data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
    return JsonResponse({'message': '저장 성공'})