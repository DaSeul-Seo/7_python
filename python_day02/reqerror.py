import requests as rq
url = "http://blog.naver.com/pjt3591oo" # 요청 페이지 URL 주소

# requests 오류를 처리하는 방법
try:
    res = rq.get(url)
    
    print(res.url)
    
except rq.exceptions.HTTPError:
    print('HTTP에러 발생')
except rq.exceptions.Timeout:
    print('Timeout 에러발생')

