import requests
from bs4 import BeautifulSoup

def get_subscribers(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    return soup.select('#rawCount')[0].text

# to run the code 
# get_subscribers('https://socialblade.com/youtube/user/pewdiepie/realtime')
# and
# get_subscribers('https://socialblade.com/youtube/user/tseries/realtime')


