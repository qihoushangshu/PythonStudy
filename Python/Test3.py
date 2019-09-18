import urllib.request

from bs4 import BeautifulSoup
'''
html = '<ul class=country><li>Area<li>Population</ul>'
'''
response = urllib.request.urlopen('http://www.baidu.com')
'''
print(response.read().decode('utf-8'))
'''
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'lxml')
print(soup.title.string)

