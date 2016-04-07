'''
Created on Mar 30, 2016
certain sites do not like being scraped, to get around this python needs to pretend to be a browser.
You need to download the program chrome driver http://chromedriver.storage.googleapis.com/index.html
I use 2.9 win32
just place chromedriver.exe into the same directory as gormonsel.exe
Instructions:

You need to log in after clicking on the Open log Page button in order for it to work. After the first time you log in, it shouldn't have to log in again for awhile,
you can open up a new tab and use the c-cex website normally but you don't want to work on the first tab the app opens
any questions or comments you can contact me at: 
noe@stakeco.in
@author: Noe
'''
import Tkinter
import ordmonsel

import tkMessageBox
import threading
import time
import pygame


pygame.init()


alertmusic = pygame.mixer.music.load('air horn.wav')



tsnames = ('C-cex','Bittrex')
msgvar=('Select the site you want to monitor trades on.', "After logging in the first time you shouldn't have to login in again for awhile.\n\nIf you haven't used this app in a while you may have to login again.\n\nClick on the OPEN LOG PAGE , then START MONITORING button to start monitoring your trades.")
cyclemsg=("You can still use the website you're if you open up a new tab and don't disturb the tab controlled by the app.","You can open up as many tabs as you want and use the broswer normally, as long as you don't distrub the app controlled tab,/n you will not effect the functioning of the Trade Monitor.")
url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'


    

class Gormonsel(Tkinter.Tk):

    
    
  
    
    
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        
        container = Tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, Ccex, Bittrex):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky='nsew')
            
        
            
        self.show_frame("StartPage")
    

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


#

class Startlogmon(threading.Thread):
        
            def __init__(self,brwoser, browserconf):
                threading.Thread.__init__(self)
                self.browserconf = browserconf
                self.browser = browser
            
            def run(self):
#                 
                orderstatustwo=None
                while True:
                    
                    orderstatusone = logmon.getlog()
                    
                    if orderstatustwo:
                        
                        if not orderstatusone == orderstatustwo:
                            self.startalarm()
  
                    self.rfreshlabel['text']='Refreshing in 60 seconds' 
                    time.sleep(60)
                    self.browser.refresh()
                    self.rfreshlabel['text']=''  
                    time.sleep(5)
                    
                    orderstatustwo = logmon.getlog()
                    
                    if not orderstatusone == orderstatustwo:
                        self.startalarm()
                    self.rfreshlabel['text']='Refreshing in 60 seconds'
                     
                    time.sleep(60)
                    self.browser.refresh()
                    time.sleep(5)
                 
            
            def set(self, rfreshlabel, stopalarmbutton, talable, stslabel):
                self.rfreshlabel = rfreshlabel
                self.stopalarmbutton = stopalarmbutton
                self.talable = talable
                self.stslabel = stslabel
                
                
                
            def startalarm(self):  
                pygame.mixer.music.play(-1)
                self.talable['text']='A trade has Occured'
                self.talable['bg']='green'
                self.stopalarmbutton.config(state='normal',bg='yellow')
                
                  
            def endalarm(self):
                self.stopalarmbutton.config(state='disable',bg='grey')
                self.talable.config(text = 'No trades currently detected', bg='red')

                pygame.mixer.music.stop()         
                
                
                
            
    
   
    
        
class StartPage(Tkinter.Frame):

    
        
    
    def __init__(self, parent, controller):
        
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'Gui Order Monitor using Selenium and Chrome Driver')

        label.grid(row=0, column=4, columnspan=2)
        

        omvar = Tkinter.StringVar()
        omvar.set('Trade Site')
        
        
        nameMenu = Tkinter.OptionMenu(self, omvar, ())
        nameMenu.grid(row=0, column=0, columnspan=2, sticky='w')
        nameMenu.config(width=20)
#     
        menu = nameMenu.children['menu']
        menu.delete(0, "end")
        
        
        
        
        for name in tsnames:
            menu.add_command(label=name, command=lambda v=name: controller.show_frame(v.replace('-','')))
            
            
# 
        MText = Tkinter.Text( self, width=40, height=20, wrap='word' )
#  
        
        MText.insert('1.0', "Don't forget to log in if you haven't already: Click open Log Page button.")
#     
        MText.config(state='disabled')
        MText.grid(row=1, column=0, sticky='w')
#       
        
        UMText = Tkinter.Text( self, width=40, height=10, wrap='word'  )
      
        
        UMText.insert('1.0', msgvar[0])
        UMText.config(state='disabled')
        UMText.grid(row=9, column=0, sticky='w')
        
      
         
    
   
    
class Ccex(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'Gui Order Monitory using Selenium and Chrome Driver')
        label.grid(row=0, column=4, columnspan=2)
#

        
        omvar = Tkinter.StringVar()
        nameMenu = Tkinter.OptionMenu(self, omvar, ())
        
        omvar.set('C-Cex')
        nameMenu.grid(row=0, column=0, columnspan=2, sticky='w')
        nameMenu.config(width=20)
        menu = nameMenu.children['menu']
        menu.delete(0, "end")
        for name in tsnames:
            menu.add_command(label=name, command=lambda v=name: controller.show_frame(v.replace('-','')))
 
        MText = Tkinter.Text( self, width=40, height=20, wrap='word' )

        
        MText.insert('1.0', "After logging into C-cex, click OPEN lOG PAGE, when you are on the Trade log page, Click start to start Monitoring trades")

        MText.config(state='disabled')
        MText.grid(row=1, column=0, sticky='w')
     
        UMText = Tkinter.Text( self, width=40, height=11, wrap='word'  )
      
        
        UMText.insert('1.0', msgvar[1])
        UMText.config(state='disabled')
        UMText.grid(row=9, column=0, sticky='w')
        
        olpbutton = Tkinter.Button(self, text='Open Log Page', command=lambda u=url: browserconf.openlogpage(browser, browserconf, strtbutton))
        
        
        olpbutton.grid(row=1, column=2, sticky='n')
      
               
        strtbutton = Tkinter.Button(self, text='START MONITORING', command=lambda: slogmon.start())
        strtbutton.grid(row=1, column=3, sticky='n')
        
        strtbutton.config(state='disable')
        
        
        

        
        stslabel = Tkinter.Label(self, text = 'Not currently Monitoring', bg='red')
        stslabel.grid(row=3, column=3, columnspan=2, sticky='w')
        startlabelvar = Tkinter.StringVar()
        
        stopalarmbutton = Tkinter.Button(self, text='Stop Alarm', command=lambda: slogmon.endalarm())
        stopalarmbutton.grid(row=3, column=4, sticky='e')
        
        stopalarmbutton.config(state='disable', bg='grey')

        
        talable = Tkinter.Label(self, text = 'No trades currently detected', bg='red')
        talable.grid(row=3, column=5)
 
        rfreshlabel = Tkinter.Label(self)        
        rfreshlabel.grid(row=1, column=4, columnspan=2, sticky='n')
        
        ltradelabel = Tkinter.Label(self, text = '')
        
        ltradelabel.grid(row=1, column=6, columnspan=2, sticky='n')
        
        slogmon.set(rfreshlabel, stopalarmbutton, talable, stslabel)
  
        logmon.set_strtbutton(strtbutton, rfreshlabel, ltradelabel, stslabel)
 
    
    def amessage(self):
        tkMessageBox.showinfo("Trade has Just Occured" )

        
class Bittrex(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'Future Update')
        label.grid(row=0, column=4, columnspan=2)
        
        omvar = Tkinter.StringVar()
        nameMenu = Tkinter.OptionMenu(self, omvar, ())
        
        omvar.set('Bittrex')
        nameMenu.grid(row=0, column=0, columnspan=2)
        nameMenu.config(width=20)
        menu = nameMenu.children['menu']
        menu.delete(0, "end")
        for name in tsnames:
            menu.add_command(label=name, command=lambda v=name: controller.show_frame(v.replace('-','')))
        
    

class AlertPage(Tkinter.Frame):
     
    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller

        Abutton = Tkinter.Button(self, text='A trade has occured', command=lambda: self.killalert())
        Abutton.pack()
         
    def killalert(self):
        pygame.mixer.music.stop()
        self.controller.show_frame(Ccex)
        
        



if __name__ == '__main__':
    
    
    browserconf = ordmonsel.ordmonsel()
    browser = browserconf.setupbrowser()
    logmon = ordmonsel.LogMon(browser, browserconf)

    slogmon = Startlogmon(browser,browserconf)
    
    slogmon.daemon = True
    
     
    
    app = Gormonsel()
    

    app.mainloop()
    
    
  
    pass