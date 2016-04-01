'''
Created on Mar 30, 2016

@author: Noe
'''
import Tkinter
import ordmonsel


tsnames = ('C-cex','Bittrex')
msgvar=('Select the site you want to monitor trades on.', "Before getting started you will want to save your cookies after logging in.\n\nThis is so that you don't have to log in every time.\n\nIf you haven't used this app in a while you may have to save your cookies again.\n\nAfter saving your cookies. Click on the start button.")
cyclemsg=("You can still use the website you're if you open up a new tab and don't disturb the tab controlled by the app.","You can open up as many tabs as you want and use the broswer normally, as long as you don't distrub the app controlled tab,/n you will not effect the functioning of the Trade Monitor.")
url = 'https://c-cex.com/?id=h&fr=&offset=&f=3'

class Gormonsel(Tkinter.Tk):

    
    
# create Order Monitor Variable instance of StringVar for use with optionmenu widget     
    
    
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
    

def ffet(param):
    print(param)
        
class StartPage(Tkinter.Frame):
    
    
    def __init__(self, parent, controller):
        
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'Gui Order Monitory using Selenium and Chrome Driver')
#         label.pack(side='bottom', fill='x', pady=10)
        label.grid(row=0, column=4, columnspan=2)
        
#         button1 = Tkinter.Button(self, text='C-Cex',
#                                  command=lambda: controller.show_frame('Ccex'))
# 
#         button2 = Tkinter.Button(self, text='Bittrex',
#                                  command=lambda: ffet('Future Update'))
        omvar = Tkinter.StringVar()
        omvar.set('Trade Site')
        
        
        nameMenu = Tkinter.OptionMenu(self, omvar, ())
        nameMenu.grid(row=0, column=0, columnspan=2, sticky='w')
        nameMenu.config(width=20)
#         nameMenu.grid_columnconfigure(1, weight=1)
#        nameMenu.pack()
#         nameMenu.place(anchor='nw')
        menu = nameMenu.children['menu']
        menu.delete(0, "end")
        
        
        
        for name in tsnames:
            menu.add_command(label=name, command=lambda v=name: controller.show_frame(v.replace('-','')))
            
            
#         Message Widget

        
#         mvar = Tkinter.StringVar()
#         mvar.set('first value')
#         App output goes here
        MText = Tkinter.Text( self, width=40, height=20, wrap='word' )
#         mvar.text.set('testing'
        
        MText.insert('1.0', "Don't forget to log in if you haven't already: Click open Log Page button.")
#         MText.delete('0.0', 'end')
        MText.config(state='disabled')
        MText.grid(row=1, column=0, sticky='w')
#         notes to user goes here
        
        UMText = Tkinter.Text( self, width=40, height=10, wrap='word'  )
      
        
        UMText.insert('1.0', msgvar[0])
        UMText.config(state='disabled')
        UMText.grid(row=9, column=0, sticky='w')
        
#         olpbutton = Tkinter.Button(self, text='Open Log Page')
#         olpbutton.grid(row=1, column=2, sticky='n')
#         
#         scpbutton = Tkinter.Button(self, text='Save Cookies')
#         scpbutton.grid(row=2, column=2, sticky='n')
        
#         MText.config(state='normal')
        
#         MText.insert('0.0', 'here is the second message')
#         MText.config(state='disabled')
        
        
#         mvar.set('second value')
        
        
        

        
        
#         button1.pack()
#         button2.pack()
     
   
    
class Ccex(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'Gui Order Monitory using Selenium and Chrome Driver')
        label.grid(row=0, column=4, columnspan=2)
#         label.pack(side='top', fill='x', pady=10)
#         button = Tkinter.Button(self, text='Go to the start page',
#                                 command=lambda: controller.show_frame('StartPage'))

        print 'Ccex'
        omvar = Tkinter.StringVar()
        nameMenu = Tkinter.OptionMenu(self, omvar, ())
        
        omvar.set('C-Cex')
        nameMenu.grid(row=0, column=0, columnspan=2, sticky='w')
        nameMenu.config(width=20)
        menu = nameMenu.children['menu']
        menu.delete(0, "end")
        for name in tsnames:
            menu.add_command(label=name, command=lambda v=name: controller.show_frame(v.replace('-','')))
#         Top widgets    
        MText = Tkinter.Text( self, width=40, height=20, wrap='word' )

        
        MText.insert('1.0', "After logging into C-cex, click OPEN lOG PAGE, when you are on the Trade log page, Click start to start Monitoring trades")

        MText.config(state='disabled')
        MText.grid(row=1, column=0, sticky='w')
        
        
        
#         notes to user goes here
#         
        UMText = Tkinter.Text( self, width=40, height=11, wrap='word'  )
      
        
        UMText.insert('1.0', msgvar[1])
        UMText.config(state='disabled')
        UMText.grid(row=9, column=0, sticky='w')
        
        olpbutton = Tkinter.Button(self, text='Open Log Page', command=lambda u=url: browserconf.openlogpage(browser, browserconf))
        
        
        olpbutton.grid(row=1, column=2, sticky='n')
      
                
        strtbutton = Tkinter.Button(self, text='START MONITORING', command=lambda: browserconf.startmon(browser, browserconf))
        strtbutton.grid(row=1, column=3, sticky='n')
        
#         scpbutton = Tkinter.Button(self, text='Save Cookies', command=lambda: )
        
#         scpbutton.grid(row=3, column=2, sticky='n')
        
        stslabel = Tkinter.Label(self, text = 'Not currently Monitoring', bg='red')
        stslabel.grid(row=3, column=3, columnspan=2)
#         stslabel.destroy()
        
#         stslabel = Tkinter.Label(self, text = 'currently monitoring', bg='green')
#         stslabel.grid(row=3, column=3, columnspan=2)
        
#         rfreshText = Tkinter.Text( self, width=2, height=5, wrap='word'  )
#       
#         
#         rfreshText.insert('1.0', 'refreshing in ' + ' seconds')
#         rfreshText.config(state='disabled')
#         UMText.grid(row=2, column=4, sticky='w')

        rfreshlabel = Tkinter.Label(self, text = 'refreshing in ' + ' seconds')
        
        rfreshlabel.grid(row=1, column=4, columnspan=2, sticky='n')
        
        ltradelabel = Tkinter.Label(self, text = 'The last trade occurred at ')
        
        ltradelabel.grid(row=1, column=6, columnspan=2, sticky='n')
        
        
        

            
        
        
        
        
        
#         button.pack()
        
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
        
        
#         label.pack(side='top', fill='x', pady=10)
#         button = Tkinter.Button(self, text='Go to the start page',
#                                 command=lambda: controller.show_frame('StartPage'))
#         
#         
#         button.pack()
        
   


if __name__ == '__main__':
    
    
    browserconf = ordmonsel.ordmonsel()
    browser = browserconf.setupbrowser()
    
    
    app = Gormonsel()
    
    app.mainloop()
    
    
#     root = Tkinter.Tk()
#     mylabel = Tkinter.Label(root, text='I am a label widget')
#     mybutton = Tkinter.Button(root, text='I am a button')
#     
#     myplabel = Tkinter.Label(parent, text='Gui Order Monitor Using Selenium and WebDriver')
#     mypbutton = Tkinter.Button(parent, text='Open Log Page')
#     myEntry(parent, width=30)
#     myOptionMenu = OptionMenu(parent, var, 'C-Cex', 'Future Update') Scrollbar(parent, orient=VERTICAL, command=mytext.yview)
#     myMessageWiget = Tkinter.Message(parent, "Don't forget to Login to the site if you haven't already.")
#     MyScaleWidget = Tkinter.Scale(parent, 'minumum 60 seconds max 4hours on site refresh') 
#     
#     mylabel.pack()
#     mybutton.pack()
#     
#     root.mainloop()
    pass