'''
Created on Mar 30, 2016

@author: Noe
'''
import Tkinter

# omvar = Tkinter.StringVar()
# omvar.set('Trade Site')
# tsnames = ('C-cex','Bittrex')

class Gormonsel(Tkinter.Tk):
    
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        
        container = Tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, CCex, Bittrex):
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
        label = Tkinter.Label(self, text = 'This is the start page')
        label.pack(side='top', fill='x', pady=10)
        
        button1 = Tkinter.Button(self, text='C-Cex',
                                 command=lambda: controller.show_frame('CCex'))
#         button2 = Tkinter.Button(self, text='Go to Page Two',
#                                  command=lambda: controller.show_frame('Bittrex')
        button2 = Tkinter.Button(self, text='Bittrex',
                                 command=lambda: ffet('Future Update'))
        
        button1.pack()
        button2.pack()
     
   
    
class CCex(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'This is page 1')
        label.pack(side='top', fill='x', pady=10)
        button = Tkinter.Button(self, text='Go to the start page',
                                command=lambda: controller.show_frame('StartPage'))
        
        
        button.pack()
        
class Bittrex(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = 'This is page 2')
        label.pack(side='top', fill='x', pady=10)
        button = Tkinter.Button(self, text='Go to the start page',
                                command=lambda: controller.show_frame('StartPage'))
        
        
        button.pack()
        
   


if __name__ == '__main__':
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