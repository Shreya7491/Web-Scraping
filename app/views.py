from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db import models
from . models import News
# # Create your views here.
# def index(request):
#     webpages_list=AccessRecord.objects.order_by('date')
#     date_dict={'access_record':webpages_list}
#     return render(request,'level_two/index.html',context=date_dict)
import urllib.request
import csv
from datetime import datetime
from bs4 import BeautifulSoup
# from django.core.cache import cache

from background_task import background


quote_page='https://www.indiatoday.in/sports/cricket'
page=urllib.request.urlopen(quote_page)
soup=BeautifulSoup(page,'html.parser')

@background(schedule=5)
def index():
    with open('title.csv','a') as csv_file:
        writer=csv.writer(csv_file)
        # cache.clear()
        News.objects.all().delete()
        for title_box in soup.find_all('h3'):
            title=title_box.text

            print(title)
            writer.writerow([title,datetime.now()])
            new_instance=News.objects.create(title=title)




            # new_instance.save()
    # return HttpResponse("done")

def send(self):
    index(repeat=120,repeat_until=None)
    new_inst = News.objects.all()
    return render(self,'app/index.html',context={'new':new_inst})
