from Tkinter import *

root = Tk()

var = StringVar()
var.set("Site View")
names = ('C-cex','Bittrex')

def ffet(param):
    var.set(param)
    print(param)




# Appends names to names list and updates OptionMenu
#def createName(n):
#    names.append(n)
#    personName.delete(0, "end")
#    menu = nameMenu['menu']
 #   menu.delete(0, "end")
#    for name in names:
#        menu.add_command(label=name, command=lambda: ffet(name))

# what to run when a name is selected
#def selection(name):
#    var.set(name)
#   print "Running"  # For testing purposes to see when/if selection runs
#    print name

# Option Menu for names
nameMenu = OptionMenu(root, var, ())
nameMenu.grid(row=0, column=0, columnspan=2)
nameMenu.config(width=20)
menu = nameMenu.children['menu']
menu.delete(0, "end")
#mlabel = nameMenu.children['label']
#for name in names:
#    menu.add_command(label=name, command=lambda v=name: nameMenu.choice.set(v))

for name in names:
    menu.add_command(label=name, command=lambda v=name: ffet(v))


# Entry for user to submit name
#Label(root, text="Name").grid(row=1, column=0)
#personName = Entry(root, width=17)
#personName.grid(row=1, column=1)


# Add person Button
#Button(root, text="Add Person", width= 20, command=lambda: createName(personName.get())).grid(row=5, column=0, columnspan=2)


mainloop()