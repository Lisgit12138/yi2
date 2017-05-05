from bs4 import BeautifulSoup
import requests,pymongo
client = pymongo.MongoClient('localhost',27017)
test_database1 = client['test_database1']
CV1 = test_database1['CV1']

def get_urls_from(pages=0):
    '''http://jy.swmu.edu.cn/Job/Index/pager/0'''
    true_url = "http://jy.swmu.edu.cn/Job/Index/pager/{}".format(pages)
    wb_data = requests.get(true_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    trust = soup.select('table > tbody > tr > td')
    if trust:
        names = soup.select('tr > td:nth-of-type(1) > a')
        sexs = soup.select('tr > td:nth-of-type(2)')
        edus = soup.select('tr > td:nth-of-type(3)')
        pros = soup.select('tr > td:nth-of-type(4)')
        years = soup.select('tr > td:nth-of-type(5)')
        jobs = soup.select('tr > td:nth-of-type(6)')
        places = soup.select('tr > td:nth-of-type(7)')
        dates = soup.select('tr > td:nth-of-type(8)')
        for name,sex,edu,pro,year,job,place,date in zip(names,sexs,edus,pros,years,jobs,places,dates):
            data = {
                'name':name.get_text(),
                'sex':sex.get_text(),
                'edu':edu.get_text(),
                'pro':pro.get_text(),
                'year':year.get_text(),
                'job':job.get_text(),
                'place':place.get_text(),
                'date':date.get_text(),
                'url':'http://jy.swmu.edu.cn' + name.get('href')
            }
            CV1.insert_one(data)
    else:
        pass

for i in range(1,250):
    get_urls_from(i)
print("all done!")