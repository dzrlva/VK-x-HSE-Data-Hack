import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text_containers = soup.find_all('div', class_='page_text_container text_content')
    article_text = '\n'.join([text_container.get_text(strip=True) for text_container in text_containers]).strip()
    return article_text

данных
data = []

до 51
for page_num in range(2, 52):
    url = f'https://daily.afisha.ru/archive/gorod/people/page{page_num}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article', class_='articles_item')

    for article in articles:
        article_link = article.find('a')['href']
        article_url = f'https://daily.afisha.ru{article_link}'
        article_text = extract_article_text(article_url)
        data.append({'link': article_url, 'text': article_text, 'tag': 'people'})

df = pd.DataFrame(data)

print(df.head())
