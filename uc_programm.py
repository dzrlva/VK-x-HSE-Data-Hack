import requests
from bs4 import BeautifulSoup as BS

path="https://news.mail.ru/society/"
r=requests.get(path)
html=BS(r.content, "html.parser")


items=html.find_all('a','newsitem__title link-holder')

for el in items:
  news_link = '/'.join(el.attrs['href'].split('/')[2:])
  path2="https://" + news_link
  l=requests.get(path2)
  soup=BS(l.content, "html.parser")
  soup.select('.paging js-module js-module > .paging__content js-pgng_cont padding_bottom_20')

  soup.find_all("div",class_="article__item article__item_alignment_left article__item_html")

  s=' '.join([tag.text for tag in soup.find_all('p')]).replace(u'\xa0', u' ').replace(u'\u2212', u' ')
  s=s.replace("\u215b"," ").replace("\xd7"," ").replace("\u20bd"," ")
  s=s.replace('\xbd',' ').replace("\xbc"," ").replace('\u2011',' ')
  s=s.replace("\xeb"," ")
  print(s)
  with open("../hard_proga/society.txt", 'r') as f:
      s2=f.read()
  with open("../hard_proga/society.txt", 'w') as f:
      f.write((s2+str("@@@")+s))

