from bs4 import BeautifulSoup
import requests

# requests.URLRequired('https://www.engadget.com/')
# with open('new_scrap.html') as scrap:
# session=requests.Session()

# content=requests.get('https://sports.theonion.com/').text
# soup=BeautifulSoup(content,'lxml')


# HEADING
# lk=soup.find('a',class_="sc-5dqm2n-0 sc-19j4917-1 dxtqhj js_link sc-1out364-0 fwjlmD")
# Div=lk.find_all('div')[0]
# result=Div.find('img')['srcset'].split(" ")[-4]
# print(result)

# DETAIL
# abs = soup.find_all('div' ,class_='curation-module__item__wrapper')
# for news in abs:
#     main=news.find_all('a')[0]
#     Link=main['href']
#     Img_src=main.div.img['srcset'].split(" ")[-4]
#     Title=main['title']
#     print(Link)
#     print(Img_src)
#     print(Link)
#     print()

# con1=soup.find('div',class_="js_lazy-image sc-1xh12qx-2 kgfyHI")
# smp=con1.img
# cal=soup.find_all('div',class_="cw4lnv-5 jbXSRk")
# for obj in cal[:10]:
#     R=obj.find('a')
#     Lnk=R['href']
#     Title=R.text
#     print(Lnk)
#     print(Title)
#     print()

# print(smp.prettify())
#     # Img=A.img['srcset'].split(" ")[-4]
#     Title = A.a.h2.text
#     Link=A.a['href']
#     # print(Img)
#     print(Title)
#     print(Link)
#     print()
    # print(A)
    # print(B)


# L1=[1,2,3]
# L2=[4,5,6]
# for (a,b) in zip(L1,L2):
#     print(a)
#     print(b)
#     print()

# image = A.div.img['srcset'].split(" ")[-4]
# Title=A['title']
# Link=A['href']
# print(image)
# print(Title)
# print(Link)

# session=requests.Session()
# session.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36T'}
# url="https://sports.theonion.com/"
#
# content=session.get(url,verify=False).content
# soup=BeautifulSoup(content,'html.parser')

# cds=soup.find('div',class_='cw4lnv-11 gmDuZG')
# main=cds.find('a')
# Img=main.div
# print(Img.prettify())


# "class=cw4lnv-11 gmDuZG"
# "class=cw4lnv-11 gmDuZG"
#       "cw4lnv-11 gmDuZG"

# import urllib3
# urllib3.disable_warnings()

# content=requests.get('https://entertainment.theonion.com/').text
# soup=BeautifulSoup(content,'lxml')


# cont=soup.find_all('div',class_="curation-module__item__wrapper")
# for A in cont:
#     main=A.find_all('a')[0]
#     Link=main['href']
#     Title=main['title']
#     Image=main.div.img['srcset'].split(' ')[-4]
#     print(Link)
#     print(Title)
#     print(Image)
#     print()





# content=requests.get('https://politics.theonion.com/').text
# soup=BeautifulSoup(content,'lxml')
#
# count=soup.find('a',class_='sc-5dqm2n-0 sc-19j4917-1 dxtqhj js_link sc-1out364-0 fwjlmD')
# res=count.div.img['srcset'].split(' ')[-4]
# print(res)



# content=requests.get('https://www.theonion.com/').text
# soup=BeautifulSoup(content,'lxml')



# First information

# count=soup.find_all('div',class_='curation-module__item__wrapper')
# for A in count:
#     main=A.find_all('a')[0]
#     Link = main['href']
#     Title = main['title']
#     Image = main.div.img['srcset'].split(' ')[-4]
#     print(Link)
#     print(Title)
#     print(Image)
#     print()
    # Obj = EntertainData()
    # Obj.image = Image
    # Obj.title = Title
    # Obj.url = Link
    #  Obj.save()



# Second information

# count=soup.find_all('div',class_='cw4lnv-11 gmDuZG')
# for A in count[:10]:
#     main=A.find_all('a')
#     Lnk=main[0]['href']
#     text=A.h2.text
#     print(Lnk)
#     print(text)
#     print()


# for A in count:
#     main=A.find_all('a')[0]
#     Link = main['href']
#     Title = main['h2'].text
#     Image = main.div.img['srcset'].split(' ')[-4]
#     print(Link)
#     print(Title)
#     print(Image)
#     print()

# 'cw4lnv-11 gmDuZG' 'cw4lnv-11 gmDuZG'
#
# 'sc-3kpz0l-1 enQhvo' 'sc-3kpz0l-1 enQhvo' 'sc-3kpz0l-1 enQhvo'




# Another way of Retrieving

# from requests_html import HTML,HTMLSession,AsyncHTMLSession
# session=HTMLSession()
# response=session.get('https://sports.theonion.com/')
# article=response.html.find('article',first=True)
#
# print(article.html)










# Abstraction(OOPs)

# from abc import ABC,abstractmethod
#
# class A(ABC):
#     def __init__(self,value):
#         self.value=value
#     @abstractmethod
#     def m1(self):
#         print('Hello')
#     # @abstractmethod
#     def m2(self):
#         print('I am in first m2')
# class B(A):
#     def m1(self):
#         print('I am in M1 and value is',self.value)
#
# class C(B):
#     def m2(self):
#         print('I am in M2 and value is',self.value)
#
#
# obj=C(100)
# obj.m1()
# obj.m2()







# S={}
# def fibo(N):
#     if N in S:
#         return S[N]
#     else:
#         if N<=0:
#             print('Invalid Input')
#         elif(N==1):
#             S[N]=0
#             return 0
#         elif(N==2):
#             S[N]=1
#             return 1
#         else:
#             S[N]=fibo(N-1)+fibo(N-2)
#             return S[N]
# A=fibo(5)
# print(A)
# print(S)


def fibo(N,lookup):
    if(N==0 or N==1):
        lookup[N]=N

    if(lookup[N] is 0):
        lookup[N]=fibo(N-1,lookup) + fibo(N-2,lookup)
    # else:
    #     pass
    return lookup[N]
N=5
lookup=[0]*10
print(fibo(5,lookup))

