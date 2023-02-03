import requests, io
from bs4 import BeautifulSoup





response = requests.get('https://viblo.asia/newest')
doc = response.text 

soup = BeautifulSoup(doc, 'html.parser')

# for link in soup.find_all('a') : 
#     print(link.string)
#     print("url: " , link.get('class'))
#     for i in range(100): print('-', end='')
#     print()

j = 0 
for link in soup.find_all('div', {'class': 'post-feed-item'}): 
    j=j+1
    print('i= ', j)
    print('+++++')
    print(link)
    print('+++++')
    k = 1 
    for link2 in link.find_all('a') : 
        print('j=' , k ) 
        k = k + 1 
        print (link2) 
        print('......')
    
    for i in range(100): print('-', end='')
    print()

