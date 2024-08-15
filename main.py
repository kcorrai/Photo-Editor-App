import customtkinter as ctk
from image_widgets import *
from PIL import Image, ImageTk

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
        
        self.image_import = ImageImport(self, self.import_image)

        self.mainloop()
        
    def import_image(self, path):
        self.image = Image.open(path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self)
        
        self.resize_image()
        
    def resize_image(self):
        self.image_output.create_image(x=0, y=0, image=self.image_tk)
        
App()