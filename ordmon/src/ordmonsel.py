'''
Created on Mar 27, 2016
certain sites do not like being scraped, to get arround this python needs to pretend to be a browser.
need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as this app

@author: Noe
'''
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import selenium2libary
import time
import os

class ordmonsel:

    

# browser = webdriver.Chrome(executable_path=path_to_chromedriver)

# browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    def setupbrowser(self):
        path_to_chromedriver = 'chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--test-type')
        return webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=chrome_options)
    
    
    def loadcookies(self):
        if os.path.isfile('cookies.pkl'):
            cookies = pickle.load(open('cookies.pkl', 'rb'))
            for cookie in cookies:
                browser.add_cookie(cookie)
                
    def savecookies(self):
        pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
        
        
        
    
# broswer.Chrome(chrome_options=chrome_options)

# browser.create_options('test-type')

url = 'https://c-cex.com/?id=orders'



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
    time.sleep(10)
    browserconf.loadcookies()
    browser.get(url)
#     browser.find_element(browser.by.LINK_TEXT(url)).sendKeys()
#    browser.
    print 'loding page'
    time.sleep(5)
    print 'Login to C-Cex'
    time.sleep(60)
    browserconf.savecookies()
    print 'saving cookies'
#    browser.find_element_by_tag_name('h1')    
    
     
    pass