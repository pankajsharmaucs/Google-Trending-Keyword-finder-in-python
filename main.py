#Beautiful Soup 
from bs4 import BeautifulSoup 
import requests 

#Request URL to extract elements from
url= 'https://kreditaid.com/dev/'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

#Print title from webpage 
# title = soup.title
# print(title)

# for link in soup.find_all('link'):
#     print(link.get('rel'))
#     print(link.get('href'))
total_link=0
for link in soup.find_all('a'):
    if link.get('href'):
        total_link=total_link+1

print("total url: "+str(total_link))
