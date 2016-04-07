'''
Created on Mar 27, 2016
certain sites do not like being scraped, to get around this python needs to pretend to be a browser.
You need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as this app
Instructions:
This has limited features and so requires some playing with at least until someone else or I make it more user friendly
You need to be logged in order for it to work. After the first time you log in, it should be able to run automatically,
you can open up a new tab and use the c-cex website normally but you don't want to work on the first tab the app opens
any questions or comments you can contact me at: 
noe@stakeco.in 
other requirements:
selenium
pip install selenium



@author: Noe
'''
from multiprocessing.managers import State
url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'
import pickle
from selenium import webdriver


import time
import os
import winsound

import re


url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'

class LogMon():
    def __init__(self, browser, browserconf):
        self.browser = browser
        self.browserconf = browserconf
   
        
        
    def set_strtbutton(self, strtbutton, rfreshlabel, ltradelabel, stslabel):
        self.strtbutton = strtbutton
        self.rfreshlabel = rfreshlabel
        self.ltradelabel = ltradelabel
        self.stslabel = stslabel
        
    def set_orderstatus(self, _orderstatustwo=None):
        self.orderstatustwo = _orderstatustwo
  
     
        
    def getlog(self):
        
        self.strtbutton.config(state='disable')
 
        self.stslabel['text']='currently monitoring'
        self.stslabel['bg']='green'
        
  
         
        self.browser.refresh()
        time.sleep(5)
        orderstatus = self.browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]', self.browser, self.browserconf)
        self.ltradelabel['text']=str('Last trade accured at ' + str(re.findall('\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}',orderstatus)).replace('u',''))
        
        return orderstatus

class ordmonsel:
    

    


    def setupbrowser(self):
        

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--test-type')
        return webdriver.Chrome(chrome_options=chrome_options)
    
    
    def loadcookies(self, browser):
        _browser=browser
        if os.path.isfile('cookies.pkl'):
            cookies = pickle.load(open('cookies.pkl', 'rb'))
            for cookie in cookies:
                _browser.add_cookie(cookie)
                
    def savecookies(self, browser):
        _browser=browser
        pickle.dump( _browser.get_cookies() , open("cookies.pkl","wb"))
        


    def orderstatus(self, date, info, browser, browserconf):
        _browser =browser
        
        _browserconf = browserconf
        
        _browserconf.savecookies(browser)
        transdate = browser.find_element_by_xpath(date).text
        transinfo = browser.find_element_by_xpath(info).text
        return transdate + transinfo
        
    def ordalert(self):
        
        ostop = None
        while not ostop:
        
        
            winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP )

            
            ostop = 'stop'
            winsound.PlaySound('SystemAsterisk', winsound.SND_PURGE)
            
    def alertstop(self):
        winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP )
    
    def alertstart(self):
        winsound.PlaySound('SystemAsterisk', winsound.SND_PURGE)
            
    
        
    def openlogpage(self, browser, browserconf, strtbutton):
        _strtbutton =strtbutton
        _strtbutton.config(state='normal')
        _browser = browser
        _browserconf = browserconf
        _browser.get(url)
        _browserconf.loadcookies(_browser)
        _browser.get(url)
 
