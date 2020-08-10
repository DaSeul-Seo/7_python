import requests as rq

# Header body에 포함하여 요청
url = "http://blog.naver.com/pjt3591oo" # 요청 페이지 URL 주소

res = rq.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Inter Max OS X 10_12_5) "
                                        "AookeWebKit/537.36 (KHTML, like Gekko) Chrome/60.0.3112.113 Safari/537.36"})

print(res.url)
