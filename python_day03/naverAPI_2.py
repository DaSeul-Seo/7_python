import json
import urllib.request

client_id = "xfXkP2dCQFroOmzHyUDf"
client_secret = "0d6Hds9azD"

enc_text = urllib.parse.quote("코로나")
url = "https://openapi.naver.com/v1/search/news.json?query={}".format(enc_text)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

print(rescode)

if(rescode == 200):
    response_body = response.read()

    # 수집 데이터를 json으로 가공
    json_rt = response_body.decode("utf-8")
    py_rt = json.loads(json_rt)

    news_list = py_rt['items']

    for news in news_list:
        print("title: {title} @ {pubDate}".format_map(news))
        # news['title']
        # print("title: {title} @ {pubDate}".format_map(news))
else:
    print("Error Code: %d" % rescode)
