from bs4 import BeautifulSoup
import re

html = """<html><head><title>test site</title></head>
            <body><div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p>
            <a href="/example/test">a tag</a><b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(class_=re.compile('d'))) # class에 d가 포함된 모든 요소 가져오기
print(soup.find_all(id=re.compile('i'))) # id에 i가 포하묀 모든 요소 가져오기
print(soup.find_all(re.compile('t'))) # 태그에 t가 포함된 모든 요소 가져오기
print(soup.find_all(re.compile('^t'))) # 태그가 t로 시작하는 모든 요소 가져오기
print(soup.find_all(href=re.compile('/'))) # href에 슬래시(/)가 포함된 모든 요소 가져오기
