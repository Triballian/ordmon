'''
Created on Mar 27, 2016

@author: Noe
'''
import requests
import bs4

session = requests.session()

req = session.get('http://stackoverflow.com/questions/10807081/script-to-extract-data-from-web-page')

doc = bs4.BeautifulSoup(req.content)

print doc.findAll('a', { "class" : "gp-share" })

if __name__ == '__main__':
    pass