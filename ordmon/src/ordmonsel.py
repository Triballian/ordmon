'''
Created on Mar 27, 2016
certain sites do not like being scraped, to get arround this python needs to pretend to be a browser.
need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as this app
Instructions:
This has limited features and so requires some playing with at least until someone else or I make it more user friendly
You need to be logged in for it to work. After the first time you log in it should be able to run automatically,
you can open up a new tab and use the c-cex website normally but you don't want to work on the first tab the app opens
any questions or comments you can contact me at 
other requirements:
selenium
pip install selenium

noe@stakeco.in 

@author: Noe
'''
url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'
import pickle
from selenium import webdriver


import time
import os
import winsound
import threading
import re


url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'

class LogMon(threading.Thread):
    def __init__(self, browser, browserconf):
        threading.Thread.__init__(self)
        self.browser = browser
        self.browserconf = browserconf
        
    def set_strtbutton(self, strtbutton, stslabel, startlabelvar, rfreshlabel, ltradelabel, tradealtert):
        self.strtbutton = strtbutton
        self.stslabel = stslabel
        self.startlabelvar = startlabelvar
        self.rfreshlabel = rfreshlabel
        self.ltradelabel = ltradelabel
        self.tradealtert = tradealtert
        
     
     
        
    def run(self):
        
        self.strtbutton.config(state='disable')
        
           
#         self.stslabel = Tkinter.Label(self, text = 'currently monitoring', bg='green')
#         
#         self.stslabel.grid(row=3, column=3, columnspan=2)
#         self.startlabelvar.set("currently monitoring")
        self.stslabel['text']='currently monitoring'
        self.stslabel['bg']='green'
        print 'in startmon'
        while True:
            

            orderstatustwo=None
            
            self.browser.refresh()
            time.sleep(5)
            orderstatusone = self.browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]', self.browser, self.browserconf)
            self.ltradelabel['text']=str('Last trade accured on ' + str(re.findall('\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}',orderstatusone)).replace('u',''))
            if orderstatustwo:
                if not orderstatusone == orderstatustwo:
                    print "an order has bee executed"
                    self.browserconf.ordalert(self.tradealtert)
                    
                    
                    
#                     
                    
            self.rfreshlabel['text']='Refreshing in 60 seconds'        
            time.sleep(60)
            self.rfreshlabel['text']=''
            
            self.browser.refresh()
            time.sleep(5)
            
            orderstatustwo = self.browserconf.orderstatus('//*[@id="flog"]/table/tbody/tr[2]/td[1]', '//*[@id="flog"]/table/tbody/tr[2]/td[5]', self.browser, self.browserconf)
            if not orderstatusone == orderstatustwo:
                print "an order has bee executed"
                
                self.browserconf.ordalert(self.tradealtert)
            
        
        
        

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
        
    def ordalert(self, tradealtert):
        self.tradealert = tradealtert
        ostop = None
        while not ostop:
        
        
            winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP )
#             raw_input('Press any key:')
            self.tradealert.tradeoccured()
            ostop = 'stop'
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