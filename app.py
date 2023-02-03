from flask import Flask 
import requests, io
from bs4 import BeautifulSoup

app= Flask(__name__) 

@app.route('/')

def home(): 
    return "<h1> Home </h1>"

@app.route('/<name>') 
def user(name) : 
    return f"<h1> Hello {name}! </h1>" 


@app.route('/BeautifulSoup') 
def BeautifulSoup() : 
    response = requests.get('https://viblo.asia/newest')
    doc = response.text 

    file = io.open('text.txt', mode = 'w' , encoding= 'utf8') 
    file.write(doc)
    return doc 

if __name__ == "__main__" : 
    app.run()