'''
Created on Mar 27, 2016

@author: Noe
'''
import requests
import bs4

session = requests.session()

req = session.get('https://c-cex.com/?id=orders')

doc = bs4.BeautifulSoup(req.content,'lxml')
#firs param is tag name

print doc
# print doc.findAll('td', { "class" : "hand" })

if __name__ == '__main__':
    pass