import tkinter as tk
from tkinter import ttk, messagebox
import ProjectPhase2 as sql

choices = ['Games', 'Players', 'Plays', 'Teams']


def deletion():
    delete_window = tk.Toplevel()
    delete_window.title('Deletion of Table')
    delete_window.configure(bg='#2d3436')

    labelFrame = tk.LabelFrame(delete_window, text='Select the name of the table you wish to delete', bg='#2d3436', fg='#ff7675')
    labelFrame.pack(fill=tk.X)

    comboBox = ttk.Combobox(labelFrame, values=choices, state='readonly')
    comboBox.pack(fill=tk.X, padx=25, pady=10)
    comboBox.current(0)

    def MessageBoxShow(selection):
        st = sql.delete(selection)
        if st is not 'Success':
            messagebox.showerror(st, 'The deletion of ' + selection + ' was NOT successful!\n' + st)
        else:
            messagebox.showinfo(st, 'The deletion of ' + selection + ' was successful!')

    submitButton = tk.Button(delete_window, padx=50, text='Submit', command=lambda: MessageBoxShow(comboBox.get().lower()))
    submitButton.pack(fill=tk.X, side=tk.BOTTOM)
    
    delete_window.mainloop()
