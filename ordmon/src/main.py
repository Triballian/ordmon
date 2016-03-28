'''
Created on Mar 27, 2016

@author: Noe
'''
import requests
import cookielib
import mechanize
import bs4

import cStringIO




if __name__ == '__main__':
    cj = mechanize.MSIECookieJar()
#     cj.load()
#    cj.load('C:\Users\Noe\AppData\Roaming\Microsoft\Windows\Cookies\Low\WMLL1AJE.txt')
    cj.load_from_registry()
#    cj.load_cookie_data('C:\\Users\\Noe\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\ECKENCD5.txt')
#    Hang on to this as a clue
#     netscapeHeader= "# HTTP Cookie File\n# http://www.netscape.com/newsref/std/cookie_spec.html\n# This is a generated file!  Do not edit.\n\n"

#     s = cStringIO.StringIO(netscapeHeader)
#     cj.revert('C:\\Users\\Noe\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\ECKENCD5.txt')
    

#     cj.load_from_registry() 
#     cj.load('ECKENCD5.txt')
    session = requests.session()

    req = session.get('https://c-cex.com/?id=orders')
    
    doc = bs4.BeautifulSoup(req.content,'lxml')
    #firs param is tag name
    
    print doc
# print doc.findAll('td', { "class" : "hand" })
    pass