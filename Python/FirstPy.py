from bs4 import BeautifulSoup
import requests
import json
'''def get_page_urls():'''
headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1568393927,1568394046; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1568394885',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
}
for i in range(1,300):
    baseurl = 'https://www.52av.one/forum-64-{}.html'.format(i)
    mainurl = 'https://www.52av.one/'
    #https://www.52av.one/thread-131085-1-1.html
    html = ''
    response = requests.get(baseurl,headers)
    if response.status_code == 200:
        html = response.text
    print(html)
    soup = BeautifulSoup(html,'lxml')
    list = soup.find('ul',id='waterfall').find_all('li')
    urls=[]
    for item in list:
        url = item.find('a').get('href')
        newurl = mainurl+url
        print(newurl)
        #urls.append(newurl)
        with open('52av.csv', 'a', encoding='UTF-8') as f:
            f.write(newurl+'\n')
            f.close()





