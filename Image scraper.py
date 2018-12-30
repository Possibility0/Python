import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import random

inp = input('Enter the name of the image you want to download: ' )

k = str(random.random())
os.chdir(r'E:\course\1. py\m')
current_directory = os.getcwd()
final_directory = os.path.join(current_directory,k+'_'+ inp)
if not os.path.exists(final_directory):
   os.makedirs(final_directory)
os.chdir(final_directory)   

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 

"""car?page="""


def make_soup(url):
    request= urllib.request.Request(url, None,headers) #The assembled request
    thepage = urllib.request.urlopen(request)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

urls = []
for i in range(1):
    site = 'https://www.istockphoto.com/in/photos/'+inp+'?page='+str(i+1)
    
    soup = make_soup(site)
    for img in soup.findAll('img'):
        temp = img.get('src')
        #print(temp)
        if temp is not None and "photos" in temp:
            #print(temp)
            urls.append(temp)
    print('Page ', i+1, ' done')
len(urls)
for i in range(len(urls)):
    filename = str(i+0+1) +'_' + inp
    path =  filename
    imagefile = open(path + ".jpg", 'wb')
    request= urllib.request.Request(urls[i], None,headers) #The assembled request
    imagefile.write(urllib.request.urlopen(request).read())
    imagefile.close()    
