from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://movie.naver.com/movie/running/current.nhn')

resp = urlopen(req)
html = resp.read().decode('utf-8')

# BeautifulSoup로 html정제
bs = BeautifulSoup(html, "html.parser")

# lis_detail_t1(ul)클래스의 하위 li접근
current_movies = bs.select(".lst_detail_t1 > li")
# print(type(current_movies))
# print(current_movies[0])
# for info in current_movies:
#     print(info.prettifu())

for movie in current_movies:
    titles = movie.select(".lst_dsc > .tit > a")

    for title in titles:
        print(title.text, title['href'])
