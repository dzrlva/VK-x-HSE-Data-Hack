import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_article_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_title_tag = soup.find('h1', itemprop='headline')
    article_text_tag = soup.find('div', class_='entry-body')
    
   
    if article_title_tag and article_text_tag:
        article_title = article_title_tag.text.strip()
        article_text = article_text_tag.text.strip()
        return article_title, article_text.replace('\n', '')
    else:
        return None, None

articles_data = []

for page_num in range(2, 52):
    url = f'https://3dnews.ru/news/page-{page_num}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_links = soup.find_all('div', class_='article-entry')

    for article_link in article_links:
        article_id = article_link['id']
        article_url = f'https://3dnews.ru/{article_id}'
        article_title, article_text = get_article_data(article_url)
        if article_title and article_text:
            articles_data.append({'url': article_url, 'title': article_title, 'text': article_text})

df = pd.DataFrame(articles_data)
