'''
Created on Mar 27, 2016

@author: Noe
'''
import requests
import selenium


import bs4

session = requests.session()

req = session.get('https://c-cex.com/?id=orders')
cookies = requests.utils.dict_from_cookiejar
driver = requests.webdriver
doc = bs4.BeautifulSoup(req.content,'lxml')
#firs param is tag name

print doc
# print doc.findAll('td', { "class" : "hand" })

if __name__ == '__main__':
    pass