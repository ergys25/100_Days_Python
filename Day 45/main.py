from bs4 import BeautifulSoup
import requests  

url = "https://news.ycombinator.com/news"

response = requests.get(url=url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find_all(class_="titleline", )







for tag in article_tag:
    print(tag.getText())
