import requests as rq

url = "https://news.naver.com/" # 요청 페이지 URL 주소

# 해당 URL로 GET요청
res = rq.get(url)
# 해당 URL로 POST요청
# res = rq.post(url)

print(res) # 응답 객체
print(res.status_code) # 응답코드 확인
print(res.headers) # 헤더쿠키가져오기
print(res.cookies) # 쿠키 가져오기
print(res.text) # HTML코드로 가져오기
print(res.content) # 바이너리 형태로 변환된 HTML 코드 가져오기
print(res.encoding) # 페이지 인코딩 확인
