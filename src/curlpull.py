'''
Created on Mar 27, 2016

@author: Noe
'''
from StringIO import StringIO    
import pycurl
import certifi

url = 'https://c-cex.com'



if __name__ == '__main__':
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(pycurl.CAINFO, certifi.where())
#     c.setopt(pycurl.URL, url)
    c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0) Gecko/20100101 Firefox/8.0')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    content = storage.getvalue()
    print content
    
    pass