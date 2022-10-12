
import bs4
import requests


HUBS = ['Старое железо']
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

URL = 'https://habr.com/ru/all/'

response = requests.get(URL, headers=HEADERS)
text = response.text
#print(text)

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
    hubs = [hub.text.strip() for hub in hubs]
    #print(hubs)
    for hub in hubs:
        if hub in HUBS:
            href = article.find(class_='tm-article-snippet__title_link').attrs['href']
            title = article.find('h2').find('span').text        
            result = f'{title} ==> {URL}{href}'
            datatime_ = article.find(class_='tm-article-snippet__datetime-published').attrs['datatime']
            print(datatime_, result)            

