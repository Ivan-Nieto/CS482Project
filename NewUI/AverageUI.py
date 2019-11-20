import tkinter as tk
from tkinter import ttk, messagebox
import ProjectPhase2 as sql

choices = ['Games', 'Players']
options_games = ['Attendance', 'TicketRevenue']
options_players = ['Salary', 'Touchdowns', 'TotalYards']

choices.sort()
options_games.sort()
options_players.sort()


def average():
    average_window = tk.Toplevel()
    average_window.title('Average')
    average_window.configure(bg='#2d3436')

    def ComputeAverage():
        tableName = str(comboBox.get().lower())
        colName = str(comboBox2.get())

        if tableName is not '' and colName is not '':
            label.config(text=sql.average(tableName, colName))
        else:
            messagebox.showerror('Error', 'No value can be NULL!')

    submitButton = tk.Button(average_window, padx=50, text='Submit', command=ComputeAverage)
    submitButton.pack(fill=tk.X, side=tk.BOTTOM)

    bottomFrame = tk.LabelFrame(average_window, text='3. Result', bg='#2d3436', fg='#ff7675')
    bottomFrame.pack(fill=tk.X, side=tk.BOTTOM, padx=50, pady=10)

    label = tk.Label(bottomFrame, text='---', bg='#2d3436', fg='#ff7675')
    label.pack(fill=tk.BOTH)

    leftFrame = tk.LabelFrame(average_window, text='1. Select the name of the table', bg='#2d3436',
                              fg='#ff7675')
    leftFrame.pack(side=tk.LEFT)
    
    rightFrame = tk.LabelFrame(average_window, text='2. Select the column of the table', bg='#2d3436', fg='#ff7675')
    rightFrame.pack(side=tk.RIGHT)

    def UpdateComboBox(event=None):
        comboBox2.set('')
        if comboBox.get() == 'Players':
            comboBox2.configure(values=options_players)
        elif comboBox.get() == 'Games':
            comboBox2.configure(values=options_games)

    comboBox = ttk.Combobox(leftFrame, values=choices, state='readonly')
    comboBox.pack(fill=tk.X, padx=25, pady=10)
    comboBox.bind('<<ComboboxSelected>>', UpdateComboBox)

    comboBox2 = ttk.Combobox(rightFrame, values=[], state='readonly')
    comboBox2.pack(fill=tk.X, padx=25, pady=10)

    average_window.mainloop()