import customtkinter as ctk
from PIL import Image

from fungsi import FungsiPage
from about import AboutPage

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 675
FONT = "Helvetica"

class App(ctk.CTk):
    """
    Tampilan utama dari window
    """
    def __init__(self):
        super().__init__()
        self.title("Trigonometri Converter")
        self.iconbitmap("icon_white.png")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
        self.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_page = FungsiPage(self)
        self.current_page.create_widgets()
        
    def show_page(self, page_name):
        if self.current_page is not None:
            self.current_page.destroy()

        match page_name:
            case "FrontPage":
                self.current_page = FrontPage(self)
                self.current_page.create_widgets()
            case "FungsiPage":
                self.state("zoomed")
                self.current_page = FungsiPage(self)
                self.current_page.create_widgets()
            case "HelpPage":
                self.current_page = HelpPage(self)
                self.current_page.create_widgets()
            case "AboutPage":
                self.current_page = AboutPage(self)
                self.current_page.create_widgets()
    

class FrontPage(ctk.CTkFrame):
    """
    Halaman awal
    """
    def __init__(self, master):
        super().__init__(master)
        self.logo_image = ctk.CTkImage(
            dark_image=Image.open("icon_white.png"), size=(150, 150)
        )
        self.front_frame = ctk.CTkFrame(
            self,
            width=350,
            height=470,
            border_width=3,
        )
        self.title = ctk.CTkLabel(
            self.front_frame,
            text="TRIGONOMETRI CONVERTER",
            wraplength=300,
            font=ctk.CTkFont(family=FONT, size=30, weight="bold"),
        )
        self.logo = ctk.CTkLabel(
            self.front_frame,
            image=self.logo_image,
            text=None,
            bg_color="transparent",
            fg_color=None,
        )
        self.start_button = ctk.CTkButton(
            self.front_frame,
            width=200,
            height=45,
            text="Start",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: App.show_page(master, "FungsiPage"),
        )
        self.help_button = ctk.CTkButton(
            self.front_frame,
            width=200,
            height=45,
            text="How to Use",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            # command=lambda: App.show_page(master, "HelpPage"),
        )
        self.about_button = ctk.CTkButton(
            self.front_frame,
            width=200,
            height=45,
            text="About",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: App.show_page(master, "AboutPage"),
        )

    def create_widgets(self):
        self.grid(column=0, row=0, sticky="nsew")
        self.front_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.title.place(relx=0.5, y=60, anchor="center")
        self.logo.place(relx=0.5, y=105, anchor="n")
        self.start_button.place(relx=0.5, y=320, anchor="s")
        self.help_button.place(relx=0.5, y=375, anchor="s")
        self.about_button.place(relx=0.5, y=430, anchor="s")


class HelpPage(ctk.CTkFrame):
    def __init__(self, master=App):
        super().__init__(master)
        pass

    def create_widgets(self):
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()
