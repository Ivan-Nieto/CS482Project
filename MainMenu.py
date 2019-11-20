import tkinter as tk
import DeleteUI
import RetrieveUI
import AverageUI
import InsertUI

root = tk.Tk()

deleteTableLabel = tk.Label(root, text='Deletion of a Table', bg='#2d3436', fg='#ff7675')
deleteTableLabel.pack(fill=tk.X)

deleteTableButton = tk.Button(root, text='Delete Table', command=DeleteUI.deletion)
deleteTableButton.pack(fill=tk.X)

retrieveDataLabel = tk.Label(root, text='Retrieve data from the given table', bg='#2d3436', fg='#ff7675')
retrieveDataLabel.pack(fill=tk.X)

retrieveDataButton = tk.Button(root, text='Retrieve Data', command=RetrieveUI.retrieval)
retrieveDataButton.pack(fill=tk.X)

averageColumnLabel = tk.Label(root, text='Get the average of a column from Table', bg='#2d3436', fg='#ff7675')
averageColumnLabel.pack(fill=tk.X)

averageColumnButton = tk.Button(root, text='Average', command=AverageUI.average)
averageColumnButton.pack(fill=tk.X)

loadDataLabel = tk.Label(root, text='Load data from a specified file', bg='#2d3436', fg='#ff7675')
loadDataLabel.pack(fill=tk.X)

loadDataButton = tk.Button(root, text='Load Data', command=InsertUI.insertion)
loadDataButton.pack(fill=tk.X)

root.mainloop()
