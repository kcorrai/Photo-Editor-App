import customtkinter as ctk
from image_widgets import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry("1000x600")
        self.title('Photo Editor')
        self.minsize(800,500)
        
        # widgets
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        
        ImageImport(self, self.import_image)

        self.mainloop()
        
    def import_image(self, path):
        print(path)
        
App()