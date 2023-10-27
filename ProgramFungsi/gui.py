import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]},{size[1]}")
        self.minsize(size[0],size[1])
        self.mainloop()

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text="Fungsi", fg_color="white", width=20).pack(expand=True, fill="both")
        app = App()
        self.pack(master=app, fill= "X")
    

if __name__ == "__main__":
    App(title="Program Fungsi", size=(600,600))

