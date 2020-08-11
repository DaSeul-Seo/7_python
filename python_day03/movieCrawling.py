from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

requset = Request('https://movie.naver.com/movie/running/current.nhn')

response = urlopen(requset)

if response.getcode() == 200:
    # 코드가 깨지기 때문에 인코딩 변경(decode('utf-8'))
    html = response.read().decode('utf-8')
    print(html)

else:
    print("HTTP ERROR")

bs = BeautifulSoup(html, 'html.parser')
# print(bs.title)
# print(bs.title.text)
# print(bs.prettify() [:1024])

# ul태그의 attribute가 lis_detail_t1인 것들
currents = bs.find("ul", attrs={"class":"lst_detail_t1"})

# currents에서 child를 하나씩 꺼낸다.
# 이때 child는 ul에 자식이니까 li이다.(소스보기로 보면 됨)
for child in currents:
    # 혹시 찾지 못할 수 있으니 예외처리
    try:
        # child(li)중에 dt에 tit 클래스를 찾아온다.
        titles = child.find("dt", attrs={"class":"tit"})
        for title in titles:
            try:
                # tit클래스의 a태그를 가지고 와서 href 링크 뿌려준다.
                if title.name == "a":
                    print(title.text, title['href'])
            except:
                pass
    except:
        pass
