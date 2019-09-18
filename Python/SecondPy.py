from bs4 import BeautifulSoup
import requests
import os
import time
headers = { 
'Accept-Encoding' : '',
'Referer': 'https://rtys6.com/ArtRB/',
'User-Agent:': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
}


for i in range(31,37): #37
    baseurl_page1 = 'https://rtys6.com/ArtRB/'
    baseurl_page2 = 'https://rtys6.com/ArtRB/list{}.html'.format(i)
    baseurl = ''
    mainurl = 'https://rtys6.com'
    html = ''
    if i == 31:
        baseurl = baseurl_page1
    else:
        baseurl = baseurl_page2
    response = requests.get(baseurl,headers, verify=False)
    print(response.headers['content-encoding'])
    if response.status_code == 200:
        html = response.text
        #print(html)
    soup = BeautifulSoup(html,'lxml')
    list = soup.find(class_='fzltp').find_all('li')
    urls=[]
    for item in list:

        url = item.find('a').get('href')
        newurl = mainurl+url
        #print(newurl)
        urls.append(newurl)
        response2 = requests.get(newurl, headers, verify=False)
        html = ''
        if response2.status_code == 200:
            html2 = response2.text
            #print(html2)
        soup2 = BeautifulSoup(html2, 'lxml')
        try:
            maxPage = int(soup2.find(class_='tpm02').find(class_='pagelist').find_all('a')[-2].text)
            #title = soup2.find(class_='tpm01').find_all('a')[-1].text
            list2 = soup2.find(class_='tpm02').find(class_='fzltp').find_all('li')
            # print(title)
            for j in range(1,maxPage):
                ct = time.time()
                local_time = time.localtime(ct)
                data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
                data_secs = (ct - int(ct)) * 1000
                time_stamp = "%s.%03d" % (data_head, data_secs)
                print(time_stamp)
                stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace(
                    '.', '')
                print(stamp)

                title = stamp
                os.makedirs(title)
                count = 0
                for item2 in list2:
                    count = count+1
                    imageUrl = item2.find('img').get('src')
                    #print(imageUrl)
                    name = '%s/%s.jpg' % (title,str(count))
                    # print(name)
                    with open(name,'wb') as f:
                        img = requests.get(imageUrl,headers).content
                        f.write(img)

        except IndexError:
            print('index out')
        # print('----------------------------start')
        # print(soup2.find(class_='tpm02').find(class_='pagelist').find_all('a'))
        # print(soup2.find(class_='tpm02').find(class_='pagelist').find_all('a')[-2].text)
        # print('----------------------------end')
        #list = soup2.find(class_='fzltp').find_all('li')




