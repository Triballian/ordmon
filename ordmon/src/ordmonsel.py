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
        
        
           
#         self.stslabel = Tkinter.Label(self, text = 'currently monitoring', bg='green')
#         
#         self.stslabel.grid(row=3, column=3, columnspan=2)
#         self.startlabelvar.set("currently monitoring")
        self.stslabel['text']='currently monitoring'
        self.stslabel['bg']='green'
        
        
            
            

        
        
         
        self.browser.refresh()
        time.sleep(5)
        orderstatus = self.browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]', self.browser, self.browserconf)
        self.ltradelabel['text']=str('Last trade accured at ' + str(re.findall('\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}',orderstatus)).replace('u',''))
        
        return orderstatus
#         oderstatusone = 'wrong'
#         if self.orderstatustwo:
#             if not orderstatusone == self.orderstatustwo:
#                 toccurred = True
#                 
#                 print 'should be returning a true form 1st ' 
#                 
#                 print "an order has bee executed"
#                 return toccurred, self.orderstatustwo
#                 
#         
#         
#                
#         
#         self.rfreshlabel['text']='Refreshing in 60 seconds' 
#         time.sleep(60)
#         self.rfreshlabel['text']=''
#         
#         self.browser.refresh()
#         time.sleep(5)
#         
#         self.orderstatustwo = self.browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]', self.browser, self.browserconf)
#         orderstatusone = 'wrong'
#         if not orderstatusone == self.orderstatustwo:
#             toccurred = True
#             
#             print "an order has bee executed"
#             print 'should be returning a true from second ' 
#             return toccurred, self.orderstatustwo
            
        
       
             
            
        
        
        

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
#             raw_input('Press any key:')
            
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
            
            
            
        
        
        
        




# if __name__ == '__main__':
#     
#         
# 
#     browserconf = ordmonsel()
#     
#     
#       
#     browser = browserconf.setupbrowser()
#     
#     
# 
#     browser.get(url)
#     print 'loding page'
#     print 'Login to C-Cex if you haven not logged in for awhile. Otherwise order page will load automatically'
#     time.sleep(10)
#     browserconf.loadcookies()
#     browser.get(url)
# 
#     
#     time.sleep(30)
#     
# 
#     browserconf.savecookies(browser)
#     print 'saving cookies'
# 
#     orderstatustwo=None
#     
#         
#         
#     
#      
#     pass