'''
Created on Mar 27, 2016
certain sites do not like being scraped, to get arround this python needs to pretend to be a browser.
need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as this app
Instructions:
This has limited features and so requires some playing with at least until someone else or I make it more user friendly
You need to be logged in for it to work. Aster the first time you log in it should be able to run automatically,
you can open up a new tab and use the c-cex website normally but you don't want to work on the first tab the app opens
any questions or comments you can contact me at 
noe@stakeco.in 

@author: Noe
'''

import pickle
from selenium import webdriver


import time
import os
import winsound



class ordmonsel:

    


    def setupbrowser(self):
        

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
        


    def orderstatus(self, date, info):
        
        transdate = browser.find_element_by_xpath(date).text
        transinfo = browser.find_element_by_xpath(info).text
        return transdate + transinfo
        
    def ordalert(self):
        ostop = None
        while not ostop:
        
        
            winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP )
            ostop = raw_input('Press any key:')
            ostop = 'stop'
            winsound.PlaySound('SystemAsterisk', winsound.SND_PURGE)
            
            
            
        
        
        
        

url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'


if __name__ == '__main__':
    
        

    browserconf = ordmonsel()
    
    
      
    browser = browserconf.setupbrowser()
    
    

    browser.get(url)
    print 'loding page'
    print 'Login to C-Cex if you haven not logged in for awhile. Otherwise order page will load automatically'
    time.sleep(10)
    browserconf.loadcookies()
    browser.get(url)

    
    time.sleep(30)
    

    browserconf.savecookies()
    print 'saving cookies'

    orderstatustwo=None
    while True:
        browser.refresh()
        time.sleep(5)
        orderstatusone = browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]')
        
        if orderstatustwo:
            if not orderstatusone == orderstatustwo:
                print "an order has bee executed"
                browserconf.ordalert()
                
        time.sleep(60)
        browser.refresh()
        time.sleep(5)
        
        orderstatustwo = browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]')
        if not orderstatusone == orderstatustwo:
            print "an order has bee executed"
            browserconf.ordalert()
            
        time.sleep(60)
        
        
    
     
    pass