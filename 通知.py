from bs4 import BeautifulSoup
import requests

def get_data():
    for url in get_urls():
        wb_data = requests.get('http://xg.swmu.edu.cn:8089/WEB/' + url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        data = {
            'title':soup.select('#ShowInfo1_NewsTitle')[0].text,
            'source':soup.select('#ShowInfo1_NewsFrom')[0].text,
            'views':soup.select('#ShowInfo1_ClickBate')[0].text,
            'time':soup.select('#ShowInfo1_InputDate')[0].text,
#            'article':soup.select('#Right > div.InfoContext')[0],
        }
        print(data)
def get_urls():
    url_outer = 'http://xg.swmu.edu.cn:8089/WEB/NewsList-LJw34Jmu~aahaacad.html'
    wb_data_outer = requests.get(url_outer)
    soup = BeautifulSoup(wb_data_outer.text,'lxml')
    urls = [url.get('href') for url in soup.select('#NewsList1_Content > li > a')]
    return urls
get_data()