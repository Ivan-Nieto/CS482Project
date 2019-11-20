import tkinter as tk
from tkinter import filedialog, messagebox
import ProjectPhase2 as sql
import os

fileName = ''


def insertion():
    insert_window = tk.Toplevel()
    insert_window.configure(bg='#2d3436')

    def GetMethod(selection):
        print(selection)
        if selection is '1':
            st = 'Data-Insert'
        if selection is '2':
            st = 'Single-Insert'
        if selection is '3':
            st = 'Multiple-Row'

        methodLabel.config(text='Method: ' + st)

    def GetFile():
        global fileName
        insert_window.filename = filedialog.askopenfilename(title='Select A File')
        insert_window.title('File Loaded: ' + os.path.basename(insert_window.filename))
        fileName = insert_window.filename

    def SubmitFile(selection):
        fName = fileName
        if selection is '1':
            st = sql.LoadDataInsert(fName)
            if st is 'Success':
                messagebox.showinfo('Success', 'You successfully imported ' + os.path.basename(fName))
            else:
                messagebox.showerror(st, os.path.basename(fName) + ' was NOT successfully imported!')
        if selection is '2':
            st = sql.SingleInsert(fName)
            if st is 'Success':
                messagebox.showinfo('Success', 'You successfully imported ' + os.path.basename(fName))
            else:
                messagebox.showerror(st, os.path.basename(fName) + ' was NOT successfully imported!')
        if selection is '3':
            st = sql.MultiRowInsert(fName)
            if st is 'Success':
                messagebox.showinfo('Success', 'You successfully imported ' + os.path.basename(fName))
            else:
                messagebox.showerror(st, os.path.basename(fName) + ' was NOT successfully imported!')

    stepOneFrame = tk.LabelFrame(insert_window, text='1. Select option', bg='#2d3436', fg='#ff7675')
    stepOneFrame.grid(row=0, column=0)

    stepTwoFrame = tk.Frame(insert_window, bg='#2d3436')
    stepTwoFrame.grid(row=0, column=1)

    stepThreeFrame = tk.LabelFrame(insert_window, text='3.Submit', bg='#2d3436', fg='#ff7675')
    stepThreeFrame.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W+tk.E)

    submitButton = tk.Button(stepThreeFrame, text='Submit', command=lambda: SubmitFile(v.get()))
    submitButton.pack(fill=tk.BOTH)

    stepTwo = tk.LabelFrame(stepTwoFrame, text='2. Load File', bg='#2d3436', fg='#ff7675')
    stepTwo.pack(expand=True, side=tk.TOP)

    methodLabel = tk.Label(stepTwoFrame, text='Method: ', width=20,bg='#2d3436', fg='#ff7675')
    methodLabel.pack(side=tk.BOTTOM)

    fileButton = tk.Button(stepTwo, padx=50, text='Load', command=GetFile)
    fileButton.pack()
    
    v = tk.StringVar(insert_window)

    values = {'Data-Insert Method': '1',
              'Single-Insert Method': '2',
              'Multiple-Row Method': '3'}

    for (text, value) in values.items():
        tk.Radiobutton(stepOneFrame, text=text, fg='#ff7675', variable=v, value=value, indicator=0, bg='#2d3436',
                       command=lambda: GetMethod(v.get())).pack(anchor=tk.W, padx=10, fill=tk.X)

    insert_window.mainloop()
