from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head>
            <body><div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p>
            <a>a tag</a><b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.select('body p')) # body 태그에서 p태그 가져오기
print(soup.select('body .d')) # body 태그에서 class가 d인 태그 가져오기
print(soup.select('body p.d')) # body 태그에서 class가 d인 p태그 가져오기
print(soup.select('body #i')) # body 태그에서 id가 i인 태그 가져오기
print(soup.select('body p#i')) # body 태그에서 id가 i인 p태그 가져오기
print(soup.select('div p')) # div 태그에서 p태그 가져오기

