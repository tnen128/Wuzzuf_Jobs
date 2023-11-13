import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
jobtitle=[]
companyname=[]
location=[]
result = requests.get("https://wuzzuf.net/search/jobs/?q=data+engineer&a=hpb")
src = result.content
soup= BeautifulSoup(src,"lxml")

jobtitles=soup.find_all("h2",{"class":"css-m604qf"})
companynames=soup.find_all("a",{"class":"css-17s97q8"})
locations= soup.find_all("span", {"class":"css-5wys0k"})

for i in range (len(locations)):
    jobtitle.append(jobtitles[i].text)
    companyname.append(companynames[i].text)
    location.append(locations[i].text)


all_values=[jobtitle,companyname,location]
q=zip_longest(*all_values)
with open("/Users/mohamed/Desktop/x/new.csv","w") as myFile:
 z=csv. writer(myFile)
 z.writerow(["Job Tiltle","Company Names","Locations"])
 z.writerows(q)
