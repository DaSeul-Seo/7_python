import requests as rq
import time

# Timeout에러가 발생했다면 일정시간 딜레이를 준 후 다시 요청하여 해결
url = "http://blog.naver.com/pjt3591oo"  # 요청 페이지 URL 주소
delay_time = 1

def connection(u):
    return rq.get(u)

try:
    connection(url)

except rq.exceptions.Timeout:
    time.sleep(delay_time)
    connection(url)
