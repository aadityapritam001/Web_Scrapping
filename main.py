import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import csv

class Scrapper:
    
    def __init__(self, url):
        self.link=url
            
    def scrap(self):
        try:
            page = urllib.request.urlopen(self.link)
        except:
            print("An error occured.")
    
        self.soup = BeautifulSoup(page, 'html.parser')
        self.content_lis = self.soup.find_all('mw-modal-trigger')
#         print(soup)
    
    def find_output(self):
        self.title=self.soup.title.text
        avail1={'Temporarily unavailable':'Out of Stock','Out of Stock':'Out of Stock','Discontinued':'Discontinued','Mixed Availability':'Variant'}
        avail=['Temporarily unavailable','Out of Stock','Discontinued','Mixed Availability']
        flag=''
        for ele in avail:
            if ele in str(self.content_lis[0]):
                flag=ele
            else:
                pass
        if(flag==''):
#             return {'Title':self.title,'Status':'In Stock','Hyperref':self.link}
            return [self.title,'In Stock',self.link]
#             print(self.title)
#             print(self.link)
#             print('In Stock')
        else:
#             return {'Title':self.title,'Status':avail1[flag],'Hyperref':self.link}
            return [self.title,avail1[flag],self.link]
#             print(self.title)
#             print(self.link)
#             print(avail1[flag])

    
if __name__=='__main__':
    result=[]
    fields=['Title','Product Status','Hyperref']
    with open('midwayusa.txt','r') as f:
        links=f.read().split()
    for url in links:
        obj=Scrapper(url)
        obj.scrap()
        result.append(obj.find_output())
#     print(result)
#     for i in result:
#         print(i)
    with open('output.csv','w') as f:
        wrt = csv.writer(f)
        wrt.writerow(fields)
        wrt.writerows(result)