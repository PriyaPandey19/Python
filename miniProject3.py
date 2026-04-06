import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

#create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helveltica",12)
)

text.pack(expand=True,fill=tk.BOTH)

#function to create file
def new_file():
    text.delete(1.0, tk.END)

#function to open file
def open_file():
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )    

root.mainloop()
