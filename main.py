import customtkinter as ctk
from image_widgets import *
from PIL import Image, ImageTk
from menu import Menu

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry("1000x600")
        self.title('Photo Editor')
        self.minsize(800,500)
        
        # widgets
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        
        self.image_import = ImageImport(self, self.import_image)

        self.mainloop()
        
    def import_image(self, path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1] # width / height --> gives us image ratio
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self)
        
    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self, self.import_image)
        
    def resize_image(self, event):
        # current canvas ratio
        canvas_ratio = event.width / event.height
        
        # resize
        if canvas_ratio > self.image_ratio: # canvas is wider than the image
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else: # canvas is taller than the image
            image_width = int(event.width)
            image_height = int(image_width * self.image_ratio)
            
        
        self.image_output.delete('all')
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width / 2, event.height / 2, image=self.image_tk)
        
        
App()