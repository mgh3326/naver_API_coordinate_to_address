#본 예제는 Python에서 주소좌표변환 api를 호출하는 예제입니다.
import os
import sys
import urllib.request
import json

Authorization = "641c05b3a82b7b68a8e6edc0ab90cc83"
# client_secret = "kpOxKkLdiK"
encText = urllib.parse.quote("삼성동 100")
url = "https://dapi.kakao.com/v2/local/search/address.json?query=" + encText  # json 결과
# url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("Authorization", Authorization)
print(request)

# request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()

    print(response_body.decode('utf-8'))
    _json=json.loads(response_body.decode('utf-8'))
    longitude = _json["result"]["items"][0]["point"]["x"]
    latitude = _json["result"]["items"][0]["point"]["y"]

    # for i in response_body.decode('utf-8'):
    #     print(i)

else:
    print("Error Code:" + rescode)
