from bs4 import BeautifulSoup
import requests

'''
url = 'http://xg.swmu.edu.cn:8089/WEB/NewsList-LJw34Jmu~aahaacad.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

titles = soup.select('#NewsList1_Content > li > a')

for title in titles:
    data = {
        'title':title.get_text(),
        'url':'http://xg.swmu.edu.cn:8089/WEB/' + title.get('href'),
    }
    print(data)
'''
url_of_text = 'http://xg.swmu.edu.cn:8089/WEB/ShowInfo-Gwtt464Jw~Gwtt464Jw~LJw34Jmu~aahaacad~M3~dad.html'
wb_data_text = requests.get(url_of_text)
soup_text = BeautifulSoup(wb_data_text.text,'lxml')

titles = soup_text.select('#ShowInfo1_NewsTitle')
texts = soup_text.select('#Right > div.InfoContext')

print(list(texts[0].stripped_strings))