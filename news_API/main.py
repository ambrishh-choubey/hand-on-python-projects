import requests
query=input("what type of news you wanna read?\n")
api="3bcf1be722854a8aae762948282a511b"


url=f"https://newsapi.org/v2/everything?q={query}&from=2026-01-24&sortBy=publishedAt&apiKey={api}"
print(url)
r=requests.get(url)
data =r.json()
articles = data["articles"]
for index,article in enumerate(articles):
    print(index +1 ,article["title"],article["url"])
    print("\n**********************\n")