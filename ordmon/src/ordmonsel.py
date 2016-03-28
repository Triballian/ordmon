'''
Created on Mar 27, 2016
certain sites do not like being scraped, to get arround this python needs to pretend to be a browser.
need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as this app


@author: Noe
'''
from selenium import webdriver

path_to_chromedriver = 'chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--test-type')

# browser = webdriver.Chrome(executable_path=path_to_chromedriver)

# browser = webdriver.Chrome(executable_path=path_to_chromedriver)
browser = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=chrome_options)
# broswer.Chrome(chrome_options=chrome_options)

# browser.create_options('test-type')

url = 'https://c-cex.com/?id=orders'



if __name__ == '__main__':
    browser.get(url)
    
    pass