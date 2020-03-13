from urllib.parse import quote_plus
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
baseUrl='https://www.google.com/search?q='
f=open('stocklist.csv','r')
stocklist=[]
while True:
    line=f.readline()
    if not line: break
    stocklist.append(line[:len(line)-1])
f.close()

hdr={'User-Agent' : 'Mozilla/6.0'}
g_url='https://datalab.naver.com/keyword/realtimeList.naver?where=main'
req=urllib.request.Request(g_url,headers=hdr)
g_html=urllib.request.urlopen(req).read()
soup=BeautifulSoup(g_html,'html.parser')

wrapper=list(map(str,soup.select('.item_title')[5::]))
result=[]
for i in wrapper:
    result.append(i[25:len(i)-7])   #making trend word list from naver

search_list=[i for i in result if i in stocklist]   

if len(search_list)==0: print('not found')
else:
    for i in search_list:
        plusUrl=i
        url=baseUrl+quote_plus(plusUrl)
        driver=webdriver.Chrome()
        driver.get(url)
        #html=driver.page_source
        #soup=BeautifulSoup(html,'html.parser')

        #r=soup.select('.r')
        #for i in r:
         #   print(i.select_one('.LC201b.DKV0Md').text)
          #  print(i.select_one('.iUh30.bc.tjvcx').text)
           # print(i.a.attrs['href'])
            #print()   these are not necessiary.
    
    
