import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky='news')
        self.import_func = import_func
        
        ctk.CTkButton(self, text='open image', command=self.open_dialog).pack(expand=True)
        
    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)
        
class ImageOutput(Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background=BACKGROUND_COLOR, bd=0, highlightthickness=0, relief='ridge')
        self.grid(row=0, column=1, sticky='news')
        
        