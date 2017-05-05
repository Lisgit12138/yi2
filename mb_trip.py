from bs4 import BeautifulSoup
import requests
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
}
wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')

imgs = soup.select('#lazyload_-1377727580_1')
print(soup)