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
    print(response_body.decode('utf-8'))
else:
    print("Error Code: %d" % rescode)
