import requests
from bs4 import BeautifulSoup

def get_subscribers(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    return soup.select('#rawCount')[0].text
