import tkinter as tk
from tkinter import *
from tkinter import ttk


# Using examples from YouTube videos by Parwiz Forogh

class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()

        # Name of window
        self.title('CS482 Project Thing')

        # Min size of window
        self.minsize(800, 450)

        # Giving window a background color
        # NMSU color is #891216
        self.configure(background='#2C3E50')

        self.logo = tk.PhotoImage(file='temp.gif')
        self.pic = tk.Label(self, image=self.logo)
        self.main_men = ttk.Button(self, text='Go back to main menu', command=self.main_screen())

        # Creating buttons with labels next to them and printing them with grid
        self.option1_text_input = StringVar()
        self.option1_button = ttk.Button(self, text='Delete Table', command=self.click_option1)
        self.option1_textbox = ttk.Entry(self, width=20, textvariable=self.option1_text_input)
        self.option1_button.grid(column=0, row=0)
        self.option1_textbox.grid(column=1, row=0)

        self.option2_text_input = StringVar()
        self.option2_button = ttk.Button(self, text='Retreve all data from table', command=self.click_option2)
        self.option2_textbox = ttk.Entry(self, width=20, textvariable=self.option2_text_input)
        self.option2_button.grid(column=0, row=2)
        self.option2_textbox.grid(column=1, row=2)

        self.option3_text_input = StringVar()
        self.option3_button = ttk.Button(self, text='Average of column in table', command=self.click_option3)
        self.option3_textbox = ttk.Entry(self, width=20, textvariable=self.option3_text_input)
        self.option3_button.grid(column=0, row=3)
        self.option3_textbox.grid(column=1, row=3)

    # If a button is clicked the text will change
    def click_option1(self):
        self.option1_button.configure(text='Deleting Table ' + self.option1_text_input.get())
        self.option1_screen()
    def click_option2(self):
        self.option2_button.configure(text='Retrieving Data from table ' + self.option2_text_input.get() )
        self.option2_screen()

    def click_option3(self):
        self.option3_button.configure(text='Calculating Average of ' + self.option3_text_input.get() )
        self.option3_screen()

        # Display picture when button3 is pressed
        #self.pic.grid(column=2, row=4)

    def main_screen(self):
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
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()

        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()

        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()

        self.option1_button.grid(column=0,row=0)
        self.option1_button.configure(command=self.main_screen)

    def option2_screen(self):
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()

        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()

        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()

        self.option2_button.grid(column=0, row=0)
        self.option2_button.configure(command=self.main_screen)

    def option3_screen(self):
        self.option1_button.grid_forget()
        self.option1_textbox.grid_forget()

        self.option2_button.grid_forget()
        self.option2_textbox.grid_forget()

        self.option3_button.grid_forget()
        self.option3_textbox.grid_forget()

        self.option3_button.grid(column=0, row=0)
        self.option3_button.configure(command=self.main_screen)
root = Root()

root.mainloop()
