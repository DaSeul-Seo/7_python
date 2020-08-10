# 태그, 아이디를 이용해 돔 가져오기
from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head>
            <body><p>test</p><p id="d">test2</p><p id="c">test3</p></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', id='d'))
print(soup.find_all('p', id='c'))
