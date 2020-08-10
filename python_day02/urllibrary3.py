from urllib.request import urlopen, Request
import urllib

# urllib는 data의 유무로 GET요청과 POST요청을 구분
url = "http://blog.naver.com/pjt3591oo"

# post요청 시 보낼 데이터 만들기
date = {'key1':'value1', 'key2':'value2'}
data = urllib.parse.urlencode(date)
data = data.encode('utf-8')

print(date)

# post요청
req_post = Request(url, data=data, headers={}) # 2번째 인자 데이터, 3번째 인자 헤더
page = urlopen(req_post)

print(page)
print(page.url)

# get 요청
req_get = Request(url+'?key1=value1&key2=value2', None, headers={}) # 2번때 인자 데이터, 3번때 인자 헤더
page = urlopen(req_get)

print(page)
print(page.url)
