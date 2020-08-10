import requests as rq

url = "http://www.example.com" # 요청 페이지 URL 주소

# 웹 페이지 접속하기 - 데이터 포함하여 요청
# 쿼리스트링 만들어서 요청
res = rq.get(url, params={"key1":"value1","key2":"value2"})
res = rq.post(url, data={"key1":"value1","key2":"value2"})

print(res.url)
