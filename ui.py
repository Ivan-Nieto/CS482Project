from tkinter import *
from tkinter import ttk, messagebox
import ProjectPhase2 as sql

choices = ['Games', 'Players', 'Plays', 'Teams']


class LabeledEntryBox(Entry):

    def __init__(self, master=None, label='Default', **kwargs):
        Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, END)
            self.configure(fg='black')

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)
            self.configure(fg='grey')


def MessageBoxShow(selection):
    print(sql.delete(selection))
    if sql.delete(selection) is not 'Success':
        messagebox.showerror('Error', 'The deletion of ' + selection + ' was NOT successful!')
    else:
        messagebox.showinfo('Success', 'The deletion of ' + selection + ' was successful!')


# Delete Window Configurations
def OpenDeleteWindow():
    delete_window = Toplevel()
    delete_window.configure(bg='#2d3436')

    leftFrame = Frame(delete_window)
    leftFrame.configure(bg='#2d3436')
    leftFrame.pack(side=LEFT)

    rightFrame = Frame(delete_window)
    rightFrame.pack(side=RIGHT)

    label = Label(leftFrame, text='Select the name of the table you wish to delete', bg='#2d3436', fg='#ff7675')
    label.pack(fill=X)

    comboBox = ttk.Combobox(leftFrame, values=choices, state='readonly')
    comboBox.pack(fill=X)
    comboBox.current(0)

    resultText = Text(rightFrame, height=10, width=85, wrap=NONE)
    resultText.pack(fill=BOTH)

    submitButton = Button(leftFrame, text='Submit', command=lambda: MessageBoxShow(comboBox.get().lower()))
    submitButton.pack(fill=X)


def OpenRetrieveWindow():
    retrieve_window = Toplevel()
    retrieve_window.configure(bg='#2d3436')

    leftFrame = Frame(retrieve_window)
    leftFrame.configure(bg='#2d3436')
    leftFrame.pack(side=LEFT)

    rightFrame = Frame(retrieve_window)
    rightFrame.pack(side=RIGHT)

    Label(retrieve_window, text='Select the name of the table you wish to display', bg='#2d3436',
          fg='#ff7675').pack(fill=X)

    resultText = Text(rightFrame, height=10, width=85, wrap=NONE)
    resultText.pack(fill=BOTH)

    ttk.Combobox(retrieve_window, values=choices, state='readonly').pack(side=LEFT, padx=10, expand=True)
    Button(retrieve_window, text='Submit', command=retrieve_window.destroy).pack(side=LEFT, ipadx=15, expand=True)


root = Tk()

average_window = Toplevel()
average_window.withdraw()

load_window = Toplevel()
load_window.withdraw()

root.title('CS 482 Project UI')
root.configure(bg='#2d3436')
root.minsize(300, 210)
root.maxsize(300, 210)

deleteTableLabel = Label(root, text='Deletion of a Table', bg='#2d3436', fg='#ff7675')
deleteTableLabel.pack(fill=X)

deleteTableButton = Button(root, text='Delete Table', command=OpenDeleteWindow)
deleteTableButton.pack(fill=X)

retrieveDataLabel = Label(root, text='Retrieve data from the given table', bg='#2d3436', fg='#ff7675')
retrieveDataLabel.pack(fill=X)

retrieveDataButton = Button(root, text='Retrieve Data', command=OpenRetrieveWindow)
retrieveDataButton.pack(fill=X)

averageColumnLabel = Label(root, text='Get the average of a column from Table', bg='#2d3436', fg='#ff7675')
averageColumnLabel.pack(fill=X)

averageColumnButton = Button(root, text='Average', command=average_window.deiconify)
averageColumnButton.pack(fill=X)

loadDataLabel = Label(root, text='Load data from a specified file', bg='#2d3436', fg='#ff7675')
loadDataLabel.pack(fill=X)

loadDataButton = Button(root, text='Load Data', command=load_window.deiconify)
loadDataButton.pack(fill=X)

root.mainloop()
