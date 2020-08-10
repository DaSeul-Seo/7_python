# 여러개의 태그를 이용해 돔 가져오기
from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head>
            <body><p>test1</p><p class="d">test2</p><p class="c">test3</p>
            <a>a tag</a><b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(['a','b']))
