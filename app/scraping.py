import urllib.request
import csv
from .models import News

from datetime import datetime
from bs4 import BeautifulSoup
quote_page='https://www.indiatoday.in/sports/cricket'
page=urllib.request.urlopen(quote_page)
soup=BeautifulSoup(page,'html.parser')



with open('title.csv','a') as csv_file:
    writer=csv.writer(csv_file)
    for title_box in soup.find_all('h3'):
        title=title_box.text
        print(title)
        writer.writerow([title,datetime.now()])
