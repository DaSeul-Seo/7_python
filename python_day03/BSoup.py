from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# HTTP GET Request
req = urlopen('http://media.daum.net')

# 먼저 req가 정상 코드를 받아왔는지 확인
print(req.getcode()) # HTTP 200은 정강

if req.getcode() == 200:
    # html을 받아오자
    html = req.read();
    print(html)

    html = html.decode("utf-8")
    print(html) # 정상이다.

else:
    print("HTTP ERROR")

# soup만들기
soup = BeautifulSoup(html, "html.parser")

print(soup.title)
# 타이틀에서 텍스트를 뽑아보자
print(soup.title.text)
