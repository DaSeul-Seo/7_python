from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head>
            <body><p id="i" class="a">test1</p><p class="d">test2</p><p class="d">test3</p>
            <a>a tag</a><b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find('p', class_="d")) # class가 d인 p태그 하나 가져오기
print(soup.find('p', class_="d")) # class가 d인 p태그 하나 가져오기
print(soup.find('p', id="i")) # id가 i인 p태그 하나 가져오기
