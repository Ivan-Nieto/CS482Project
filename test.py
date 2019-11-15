import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import ProjectPhase2

# Using examples from YouTube videos by Parwiz Forogh

class RootinPutin(Tk):

    def __init__(self):
        super(RootinPutin, self).__init__()

        ttk.Style().configure('TButton', padding=6, relief='flat', background='#891216')
        # Name of window
        self.title('CS482 Project GUI')

        # Min size of window
        self.minsize(800, 450)

        # Giving window a background color
        # NMSU color is #891216 FYI
        self.configure(background='#2C3E50')

        # Variable holds the text to go in the result text box
        str = '\"Thunderbolt and lightning very very frightening me\"\n-Galileo'

        # Test picture settings
        self.logo = tk.PhotoImage(file='/Users/acruz_42/Desktop/CS482Project/temp.gif')
        self.pic = tk.Label(self, image=self.logo)
        self.main_men = ttk.Button(self, text='<- Go back to main menu', command=self.main_screen)

        # Using https://www.python-course.eu/tkinter_text_widget.php
        # Creating text box to print the results of the query
        self.result = tk.Text(self, height=10, width=75)
        self.scroll = tk.Scrollbar(self)
        self.scroll.config(command=self.result.yview)
        self.result.config(yscrollcommand=self.scroll.set)
        self.result.insert(tk.END, str)

        # Creating buttons with text boxes next to them and displaying them with grid
        self.option1_text_input = StringVar()
        self.option1_button = ttk.Button(self, text='Delete Table', command=self.option1_screen)
        self.option1_textbox = ttk.Entry(self, width=20, textvariable=self.option1_text_input)
        self.option1_button.grid(column=0, row=0)
        self.option1_textbox.grid(column=1, row=0)
        self.option1_textbox.insert(0,'Table Name')
        self.option1_textbox.config(foreground='#B3B2B2')

        self.option2_text_input = StringVar()
        self.option2_button = ttk.Button(self, text='Retrieve all data from table', command=self.option2_screen)
        self.option2_textbox = ttk.Entry(self, width=20, textvariable=self.option2_text_input)
        self.option2_button.grid(column=0, row=2)
        self.option2_textbox.grid(column=1, row=2)
        self.option2_textbox.insert(0, 'Table Name')
        self.option2_textbox.config(foreground='#B3B2B2')

        self.option3_text_input = StringVar()
        self.option3_text_input2 = StringVar()
        self.option3_button = ttk.Button(self, text='Average of column in table', command=self.option3_screen)
        self.option3_textbox = ttk.Entry(self, width=20, textvariable=self.option3_text_input)
        self.option3_textbox2 = ttk.Entry(self, width=20, textvariable=self.option3_text_input2)
        self.option3_button.grid(column=0, row=3)
        self.option3_textbox.grid(column=1, row=3)
        self.option3_textbox2.grid(column=2, row=3)
        self.option3_textbox.insert(0, 'Table name')
        self.option3_textbox.config(foreground='#B3B2B2')
        self.option3_textbox2.insert(0, 'Column name')
        self.option3_textbox2.config(foreground='#B3B2B2')

        self.option4_text_input = StringVar()
        self.option4_button = ttk.Button(self, text='Load Data Insert through file', command=self.option4_screen)
        self.option4_textbox = ttk.Entry(self, width=20, textvariable=self.option4_text_input)
        self.option4_button.grid(column=0, row=4)

        # Secondary screen buttons for choosing what method of insertion to use
        self.option4b_button1 = ttk.Button(self, text='Load Data Insert Method', command=self.callLDI)
        self.option4b_button2 = ttk.Button(self, text='Single Insertion Method', command=self.callSIM)
        self.option4b_button3 = ttk.Button(self, text='Multiple-row Insertion ', command=self.callMRI)


    def main_screen(self):
        # Deleting main menu button on screen
        self.main_men.grid_forget()
        self.result.grid_forget()
        self.pic.grid_forget()

        # Displaying all option buttons and text boxes
        self.option1_button.configure(command=self.option1_screen)
        self.option1_button.grid(column=0,row=0)
        self.option1_textbox.grid(column=1,row=0)
        self.option1_textbox.delete(0, 'end')
        self.option1_textbox.insert(0, 'Table Name')

        self.option2_button.configure(command=self.option2_screen)
        self.option2_button.grid(column=0,row=1)
        self.option2_textbox.grid(column=1, row=1)
        self.option2_textbox.delete(0, 'end')
        self.option2_textbox.insert(0, 'Table Name')

        self.option3_button.configure(command=self.option3_screen)
        self.option3_button.grid(column=0, row=2)
        self.option3_textbox.grid(column=1, row=2)
        self.option3_textbox2.grid(column=2, row=2)
        self.option3_textbox.delete(0, 'end')
        self.option3_textbox.insert(0, 'Table Name')
        self.option3_textbox2.delete(0, 'end')
        self.option3_textbox2.insert(0, 'Column Name')

        self.option4_button.configure(command=self.option4_screen)
        self.option4_button.grid(column=0, row=3)

    def option1_screen(self):
        # Deleting all previous buttons on screen
        self.deleteMainMenButtons()

        # Displaying main menu button
        self.main_men.grid(column=0, row=0)

        # Getting query results
        str = ProjectPhase2.delete(self.option1_text_input.get())

        # Clearing text box before redefining its contents
        self.result.delete('1.0', END)
        self.result.insert(tk.END, str)

        # Displaying results box.
        self.result.grid(column=0, row=1)

    def option2_screen(self):
        # Deleting all previous buttons on screen
        self.deleteMainMenButtons()

        # Displaying main menu button
        self.main_men.grid(column=0, row=0)

        # Getting query results
        str = ProjectPhase2.retrieve(self.option2_text_input.get())

        # Clearing text box before redefining its contents
        self.result.delete('1.0', END)
        self.result.insert(tk.END, str)

        # Displaying results box.
        self.result.grid(column=0, row=1)

    def option3_screen(self):
        # Deleting all previous buttons on screen
        self.deleteMainMenButtons()

        # Displaying main menu button
        self.main_men.grid(column=0, row=0)

        # Getting query results
        str = ProjectPhase2.average(self.option3_text_input.get(),self.option3_text_input2.get())

        # Clearing text box before redefining its contents
        self.result.delete('1.0', END)
        self.result.insert(tk.END, str)

        # Displaying results box.
        self.result.grid(column=0, row=1)

    def option4_screen(self):
        # Deleting all previous buttons on screen
        self.deleteMainMenButtons()

        # Displaying option buttons
        self.option4b_button1.grid(column=0, row=0)
        self.option4b_button2.grid(column=0, row=1)
        self.option4b_button3.grid(column=0, row=2)

    def deleteMainMenButtons(self):

        # Deleting all previous buttons on screen
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()
        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()
        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()
        self.option3_textbox2.grid_forget()
        self.option4_button.grid_forget()

    def callLDI(self):

        # Deleting option buttons from screen
        self.option4b_button1.grid_forget()
        self.option4b_button2.grid_forget()
        self.option4b_button3.grid_forget()

        # Displaying main menu button
        self.main_men.grid(column=0, row=0)

        file_name = askopenfilename()
        # Getting query results
        str = ProjectPhase2.LoadDataInsert(file_name, self.option4_text_input.get())

        # Clearing text box before redefining its contents
        self.result.delete('1.0', END)
        self.result.insert(tk.END, str)

        # Displaying results box.
        self.result.grid(column=0, row=1)

    def callMRI(self):

        # Deleting option buttons from screen
        self.option4b_button1.grid_forget()
        self.option4b_button2.grid_forget()
        self.option4b_button3.grid_forget()

        # Displaying main menu button
        self.main_men.grid(column=0, row=0)

        file_name = askopenfilename()
        # Getting query results
        str = ProjectPhase2.MultiRowInsert(file_name, self.option4_text_input.get())

        # Clearing text box before redefining its contents
        self.result.delete('1.0', END)
        self.result.insert(tk.END, str)

        # Displaying results box.
        self.result.grid(column=0, row=1)

    def callSIM(self):

        # Deleting option buttons from screen
        self.option4b_button1.grid_forget()
        self.option4b_button2.grid_forget()
        self.option4b_button3.grid_forget()

        # Displaying main menu button
        self.main_men.grid(column=0, row=0)

        file_name = askopenfilename()
        # Getting query results
        str = ProjectPhase2.SingleInsert(file_name, self.option4_text_input.get())

        # Clearing text box before redefining its contents
        self.result.delete('1.0', END)
        self.result.insert(tk.END, str)

        # Displaying results box.
        self.result.grid(column=0, row=1)


root = RootinPutin()

# Running GUI loop
root.mainloop()
