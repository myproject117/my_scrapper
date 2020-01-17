from django.shortcuts import render,redirect
from test_app.models import SportData,SportExten
from test_app.models import EntertainData,EntertainExten
from test_app.models import Polity,PolityExten
from test_app.models import LatestData,LatestExten
# Create your views here.
def Home(request):
    # content=Select.objects.get()
    # context={'content':content}
    return render(request,'test_app/start.html')

def LatestSelect(request):
    return render(request,'test_app/LatestAdd.html')

def SportSelect(request):
    return render(request,"test_app/SportAdd.html")

def EntertainSelect(request):
    return render(request,"test_app/EntertainAdd.html")

def PolitySelect(request):
    return render(request,"test_app/PolityAdd.html")

from bs4 import BeautifulSoup
import requests
def latest(request):
    LatestData.objects.all().delete()
    LatestExten.objects.all().delete()
    content=requests.get('https://www.theonion.com/').text
    soup=BeautifulSoup(content,'lxml')
    abs=soup.find_all('div',class_='curation-module__item__wrapper')

    for news in abs:
        main = news.find_all('a')[0]
        Link = main['href']
        Img_src = main.div.img['srcset'].split(" ")[-4]
        Title = main['title']
        obj=LatestData()
        obj.image=Img_src
        obj.title=Title
        obj.url=Link
        obj.save()
    count=soup.find_all('div',class_='cw4lnv-11 gmDuZG')
    for A in count[:10]:
        main = A.find_all('a')
        Lnk = main[0]['href']
        text = A.h2.text
        obj1=LatestExten()
        obj1.url=Lnk
        obj1.title=text
        obj1.save()
    context1=LatestData.objects.all()
    context2=LatestExten.objects.all()
    return render(request,'test_app/latest.html',{'context1':context1,'context2':context2})

def sports(request):
    SportData.objects.all().delete()
    SportExten.objects.all().delete()
    content = requests.get('https://sports.theonion.com/').text
    soup = BeautifulSoup(content, 'lxml')
    abs = soup.find_all('div', class_='curation-module__item__wrapper')

    for news in abs:
        main = news.find_all('a')[0]
        Link = main['href']
        Img_src = main.div.img['srcset'].split(" ")[-4]
        Title = main['title']
        Obj=SportData()
        Obj.image=Img_src
        Obj.title=Title
        Obj.url=Link
        Obj.save()
    cal = soup.find_all('div', class_="cw4lnv-5 jbXSRk")
    for obj in cal[:10]:
        R = obj.find('a')
        Link = R['href']
        Title = R.text
        Obj1=SportExten()
        Obj1.title=Title
        Obj1.url=Link
        Obj1.save()
    context1=SportData.objects.all()
    context2=SportExten.objects.all()
    return render(request,'test_app/sports.html',{'context1':context1,'context2':context2})

def Entertainment(request):
    EntertainData.objects.all().delete()
    EntertainExten.objects.all().delete()
    content=requests.get('https://entertainment.theonion.com/').text
    soup=BeautifulSoup(content,'lxml')

    cont = soup.find_all('div', class_="curation-module__item__wrapper")
    for A in cont:
        main = A.find_all('a')[0]
        Link = main['href']
        Title = main['title']
        Image = main.div.img['srcset'].split(' ')[-4]
        Obj=EntertainData()
        Obj.image=Image
        Obj.title=Title
        Obj.url=Link
        Obj.save()
    cal = soup.find_all('div', class_="cw4lnv-5 jbXSRk")
    for obj in cal[:10]:
        R = obj.find('a')
        Link = R['href']
        Title = R.text
        Obj1 = EntertainExten()
        Obj1.title = Title
        Obj1.url = Link
        Obj1.save()
    context1=EntertainData.objects.all()
    context2=EntertainExten.objects.all()
    return render(request,"test_app/entertain.html",{'context1':context1,'context2':context2})

def Politics(request):
    Polity.objects.all().delete()
    PolityExten.objects.all().delete()
    content = requests.get('https://politics.theonion.com/').text
    soup = BeautifulSoup(content, 'lxml')

    cont = soup.find_all('div', class_="curation-module__item__wrapper")
    for A in cont:
        main = A.find_all('a')[0]
        Link = main['href']
        Title = main['title']
        Image = main.div.img['srcset'].split(' ')[-4]
        Obj = Polity()
        Obj.image = Image
        Obj.title = Title
        Obj.url = Link
        Obj.save()
    cal = soup.find_all('div', class_="cw4lnv-5 jbXSRk")
    for obj in cal[:10]:
        R = obj.find('a')
        Link = R['href']
        Title = R.text
        Obj1 = PolityExten()
        Obj1.title = Title
        Obj1.url = Link
        Obj1.save()
    context1 = Polity.objects.all()
    context2=PolityExten.objects.all()
    return render(request, "test_app/polity.html", {'context1': context1,'context2':context2})

