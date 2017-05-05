from bs4 import BeautifulSoup
import requests,time
from multiprocessing import Process

def get_urls_from(pages=0):
    '''http://jy.swmu.edu.cn/News/Index/2002/pager/0'''
    url = 'http://jy.swmu.edu.cn/News/Index/2002/pager/{}'.format(pages)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.select('div.list a'):
        host = 'http://jy.swmu.edu.cn'
        url_list = [host + url.get('href') for url in soup.select('div.list a.roll')]
        return url_list
    else:
        return []
def get_info_from(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    data = {
        'title':soup.select('p.blue')[0].text,
        'time':soup.select('span')[1].text,
        'author':soup.select('span')[2].text,
#        'cates':soup.select('span')[3].text,
        'job':soup.select('p.brief')[0].text.strip(),
        'url':url,
#        'others':soup.select('div.clear p')[1:] if len(soup.select('div.clear p')) > 1 else soup.select('div.clear a'),
    }
    print(data)
urls = []
def get_urls_whole(start=0,stop=300):
    global urls
    for i in range(start,stop):
        urls.extend(get_urls_from(i))

def get_info_whole():
    for i in urls:
        get_info_from(i)
def main():
    get_urls_whole()
    get_info_whole()
    print("all done!")
if __name__ == '__main__':
    main()