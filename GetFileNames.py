# import modules
import os
import csv
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

directory_path = ""
file_path = ""

while not os.path.exists(directory_path):
    # directory path input dialog
    directory_path = simpledialog.askstring(title="Directory path",
                                prompt="Enter the path of the directory with the files:")

# file path input dialog
file_path = simpledialog.askstring(title="File path",
                                prompt="Enter the path of the file where you want to write the titles:")

# get the list of all files and directories
directory_list = os.listdir(directory_path)

# open the file in the write mode
file = open(file_path, 'w')

# create the csv writer
writer = csv.writer(file)

for file_name in directory_list:
    # write a file name in a row to the csv file except hidden files
    if not file_name.startswith('.'):
        writer.writerow([file_name])

tk.messagebox.showinfo(title="Success", message="The file names have been successfully written to your .csv file.")

# close the file
file.close()
