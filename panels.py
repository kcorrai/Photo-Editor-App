import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady=4, ipady=8)
        
class SliderPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent=parent)
        
        # layout
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1), weight=1)
        
        ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky='w', padx=5)
        ctk.CTkLabel(self, text='0.0').grid(column=1, row=0, sticky='e', padx=5)
        ctk.CTkSlider(self, fg_color=SLIDER_BG).grid(row=1, column=0, columnspan=2, sticky='ew', pady=5)
        