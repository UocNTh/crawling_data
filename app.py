from flask import Flask 
import requests, io
from bs4 import BeautifulSoup

app= Flask(__name__) 

@app.route('/')
def home(): 
    return "Home" 

@app.route('/page/<int:id>') 
def bs4(id) : 
    if id == 1 : url = 'https://viblo.asia/newest' 
    else : url = f"https://viblo.asia/newest?page={id}"
    response = requests.get(url)

    doc = response.text 

    soup = BeautifulSoup(doc, 'html.parser')

    urls = list()

    for link in soup.find_all('h3', {'class': 'word-break' }) : 

        link2 = link.find('a')

        urls.append('https://viblo.asia'+ link2['href'])
 
    return urls 


if __name__ == "__main__" : 
    app.run()
