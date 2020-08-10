import requests as rq
from bs4 import BeautifulSoup

# 1. http://pjt3591oo.github.io/ 접속
# 2. body > main.page-content > div.wrapper div.home div.p
# 2-1. 원하는 요소에 접근 후 text속성을 가져오면 해당 태그
# 3. /page숫자 형태로 다음 페이지 접속
# 4. 응답 코드가 404가 나올때까지 2-3 반복

# 2. body > main.page-content > div.wrapper div.home div.p
# 2-1. 원하는 요소에 접근 후 text속성을 가져오면 해당 태그
def get_posts(soup): # 돔 접근
    return soup.select('body main.page-content div.wrapper div.home div.p')

def data_parse(posts): # 해달 돔에서 필요한 데이터 뽑기
    for post in posts:
        title = post.find('h3').text.strip()
        descript = post.find('h4').text.strip()
        author = post.find('span').text.strip()
        print(title, descript, author)

base_url = "https://pjt3591oo.github.io"
page_path = '/page%d' # url을 변경할 수 있도록 포멧팅 활용
page = 2

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')

posts = get_posts(soup)
data_parse(posts)

# 3. /page숫자 형태로 다음 페이지 접속
while True: # 다음 페이지로 접속할 수 있도록 반복문 이용
    sub_path = page_path%(page) # url을 생성해준다.
    page += 1
    res = rq.get(base_url + sub_path)

    # 4. 응답 코드가 404가 나올때까지 2-3 반복
    if(res.status_code != 200): # 200코드가 아니라면 해당 반복문 탈출
        break

    soup = BeautifulSoup(res.content, 'lxml')
    posts = get_posts(soup)

    data_parse(posts)
