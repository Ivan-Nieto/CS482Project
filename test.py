import tkinter as tk
from tkinter import *
from tkinter import ttk


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
        self.logo = tk.PhotoImage(file='temp.gif')
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
        self.option1_button = ttk.Button(self, text='Delete Table', command=self.click_option1)
        self.option1_textbox = ttk.Entry(self, width=20, textvariable=self.option1_text_input)
        self.option1_button.grid(column=0, row=0)
        self.option1_textbox.grid(column=1, row=0)

        self.option2_text_input = StringVar()
        self.option2_button = ttk.Button(self, text='Retrieve all data from table', command=self.click_option2)
        self.option2_textbox = ttk.Entry(self, width=20, textvariable=self.option2_text_input)
        self.option2_button.grid(column=0, row=2)
        self.option2_textbox.grid(column=1, row=2)

        self.option3_text_input = StringVar()
        self.option3_button = ttk.Button(self, text='Average of column in table', command=self.click_option3)
        self.option3_textbox = ttk.Entry(self, width=20, textvariable=self.option3_text_input)
        self.option3_button.grid(column=0, row=3)
        self.option3_textbox.grid(column=1, row=3)


    # If a button is clicked, the text will change and a new page will be displayed
    def click_option1(self):
        self.option1_button.configure(text='Deleting Table ' + self.option1_text_input.get())
        self.option1_screen()

    def click_option2(self):
        self.option2_button.configure(text='Retrieving Data from table ' + self.option2_text_input.get() )
        self.option2_screen()

    def click_option3(self):
        self.option3_button.configure(text='Calculating Average of ' + self.option3_text_input.get() )
        self.option3_screen()

        # Display picture when button3 is pressed...or don't, what do I care
        # self.pic.grid(column=2, row=4)


    def main_screen(self):
        # Deleting main menu button on screen
        self.main_men.grid_forget()
        self.result.grid_forget()
        self.pic.grid_forget()

        # Displaying all option buttons and text boxes
        self.option1_button.configure(command=self.option1_screen)
        self.option1_button.grid(column=0,row=0)
        self.option1_textbox.grid(column=1,row=0)

        self.option2_button.configure(command=self.option2_screen)
        self.option2_button.grid(column=0,row=1)
        self.option2_textbox.grid(column=1, row=1)

        self.option3_button.configure(command=self.option3_screen)
        self.option3_button.grid(column=0, row=2)
        self.option3_textbox.grid(column=1, row=2)


    def option1_screen(self):
        # Deleting all previous buttons on screen
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()
        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()
        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()

        # Displaying main mem button and results box.
        self.result.grid(column=0, row=1)
        self.main_men.grid(column=0, row=0)
        
        # Input from input box for this button 
        # in variable self.option1_text_input
        
        # To change the text that is displayed in the results text box
        # do self.result.insert(tk.END, str)
        # where str is the string to be displayed.


    def option2_screen(self):
        # Deleting all previous buttons on screen
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()
        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()
        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()

        # Displaying main mem button and results box.
        self.result.grid(column=0, row=1)
        self.main_men.grid(column=0, row=0)

        # Input from input box for this button 
        # in variable self.option2_text_input
        
        # To change the text that is displayed in the results text box
        # do self.result.insert(tk.END, str)
        # where str is the string to be displayed.


    def option3_screen(self):
        # Deleting all previous buttons on screen
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()
        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()
        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()

        # Displaying main mem button and results box.
        self.result.grid(column=0, row=1)
        self.main_men.grid(column=0, row=0)

        # Input from input box for this button 
        # in variable self.option3_text_input
        
        # To change the text that is displayed in the results text box
        # do self.result.insert(tk.END, str)
        # where str is the string to be displayed.
        
        
root = RootinPutin()

# Running GUI loop
root.mainloop()
