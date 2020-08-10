from urllib.request import urlopen, Request

# urllib는 없는 페이지 요청 시 에러 발생
url = "http://blog.naver.com/pjt3591oo/1/"

req_post = Request(url)
page = urlopen(req_post)

print(page)
print(page.url)
