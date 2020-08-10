from urllib.request import urlopen, Request

# urllib로 요청 후 데이터 가져오기
url = "http://blog.naver.com/pjt3591oo"

req = Request(url)
page = urlopen(req)

print(page) # 응답객체
print(page.code) # 응답 코드
print(page.headers) # 헤더확인
print(page.url) # 요청 url 확인
print(page.info().get_contest_charset()) # 인코딩 설정 확인
print(page.read()) # HTML 코드 가져오기
