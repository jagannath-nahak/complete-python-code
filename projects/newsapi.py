import requests
import json

query=input("what type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-08-20&sortBy=publishedAt&apiKey=9b851e537cd54b9fa6e7e9ccd8a0069b"

r=requests.get(url)

news=json.loads(r.text)
# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------")