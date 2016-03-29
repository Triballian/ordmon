'''
Created on Mar 27, 2016
certain sites do not like being scraped, to get arround this python needs to pretend to be a browser.
need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as this app

@author: Noe
'''
import re
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import selenium2libary
import time
import os
#from distutils.tests.test_register import RawInputs

class ordmonsel:

    

# browser = webdriver.Chrome(executable_path=path_to_chromedriver)

# browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    def setupbrowser(self):
        
#         The follwing line is not necessary if you expect chromedriver to be in the current directory
#        path_to_chromedriver = 'chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--test-type')
        return webdriver.Chrome(chrome_options=chrome_options)
    
    
    def loadcookies(self):
        if os.path.isfile('cookies.pkl'):
            cookies = pickle.load(open('cookies.pkl', 'rb'))
            for cookie in cookies:
                browser.add_cookie(cookie)
                
    def savecookies(self):
        pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
        
    def orders(self):
#         pull using regular experssions
        regstring = re.compile(r'\d+.*[Buy|Sell]\s\d+\.?\d*\s\w*\s\d*\.?\d*\b')
#         neworders = re.findall(regstring, raworders )
        
#         create list of keys and list of definitions
        
        #print neworders
        
#         for order in neworders:
#             keylist = order[-3]
#             keylist = order.split(delimeter)[0]
#             print str(keylist)
#             print order
            
#             print order
    
# broswer.Chrome(chrome_options=chrome_options)

# browser.create_options('test-type')
    def orderstatus(self, date, info):
        
        transdate = browser.find_element_by_xpath(date).text
        transinfo = browser.find_element_by_xpath(info).text
        return transdate + transinfo
        
        

url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'


if __name__ == '__main__':
    
#     ordmons = ordmonsel
#     browserconf = ordmonsel
    browserconf = ordmonsel()
   
    browser = browserconf.setupbrowser()
    
    
#    browser.get('https://www.google.com')
#     open tab
#    time.sleep(30)
#    browserconf.loadcookies()
#    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    browser.get(url)
    print 'loding page'
    print 'Login to C-Cex if you haven not logged in for awhile. Otherwise order page will load automatically'
    time.sleep(10)
    browserconf.loadcookies()
    browser.get(url)
#     browser.find_element(browser.by.LINK_TEXT(url)).sendKeys()
#    browser.
    
    time.sleep(10)
    
#    time.sleep(60)
    browserconf.savecookies()
    print 'saving cookies'
#    orders = browser.find_element_by_xpath('//tr[contains(@class, "hand")]/text()/following::td').text
#    orders = browser.find_element_by_xpath('//tr[(@class = "hand")]').text
#     transdate = browser.find_element_by_xpath('//*[@id="flog"]/table/tbody/tr[2]/td[1]').text
#     transinfo = browser.find_element_by_xpath('//*[@id="flog"]/table/tbody/tr[2]/td[5]').text
#     oldtrans = transdate + transinfo
#     print type(oldtrans)
#     initial order status
    orderstatustwo=None
    while True:
        browser.refresh()
        time.sleep(5)
        orderstatusone = browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]')
        print 'in one'
        if orderstatustwo:
            if not orderstatusone == orderstatustwo:
                print "an order has bee executed"
                print "still in one"
        time.sleep(15)
        browser.refresh()
        time.sleep(5)
        print 'in two'
        orderstatustwo = browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]')
        if not orderstatusone == orderstatustwo:
            print "an order has bee executed"
            print 'still in two'
        time.sleep(15)
        
        
    
     
    pass