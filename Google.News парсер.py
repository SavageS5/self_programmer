# Парсим Google.News

import urllib.request

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)

        with open('google-pars.txt', 'w') as file_handler:
            for tag in sp.find_all('a'):
                url = tag.get('href')
                label = tag.get('aria-label')

                if url is None:
                    continue
                if "https" in url:
                    if label is not None:
                        print('\n', label, end = '')            # Пишем на экран
                        file_handler.write('\n' + label + '')   # Пишем в файл
                    print('\n' + url)
                    file_handler.write('\n' + url + '\n')
                
news = "https://news.google.ru/"
Scraper(news).scrape()
