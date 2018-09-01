import requests
import re
from article import Article
from bs4 import BeautifulSoup

blog_url = "https://www.joyhwong.com"
pat_category_path = "/archives/category/pat/"
request_url = blog_url + pat_category_path
article_list = []

while True:
    r = requests.get(request_url)
    soup = BeautifulSoup(r.text, "html.parser")

    headers = soup.find_all('header', class_='entry-header')

    for header in headers:
        a = header.find("a")
        if re.findall('乙级', a.text) or (re.findall('甲级', a.text) and re.findall('C\+\+版', a.text)):
            continue
        try:
            article_list.append(Article(a['href'], a.text, re.findall('[0-9]{4}', a.text)[0]))
        except IndexError:
            None

    if soup.find('a', class_='next page-numbers') is None:
        break
    else:
        request_url = soup.find('a', class_='next page-numbers')['href']

for article in sorted(article_list):
    print(article.id, article.title, article.url)
    print()
