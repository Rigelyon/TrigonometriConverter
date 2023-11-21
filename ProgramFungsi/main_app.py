import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from fungsi import FungsiPage
from about import AboutPage

# Const untuk size window dan font
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 675
FONT = "Helvetica"

class App(ctk.CTk):
    """
    Tampilan utama dari window. Window berisi base frame yang mempunyai children frame.
    Base frame digunakan untuk mengganti halaman. Sistem mengganti halaman adalah dengan menghancurkan
    halaman saat ini dan memasang kembali halaman yang akan ditampilkan.
    List dari Base Frame beberapa halaman:
    - FrontPage() = Class untuk halaman awal dari program. Berisi base frame dan children widgets
    - FungsiPage() = Class untuk halaman utama program. Berisi base frame dan children widgets
    - HelpPage() = Class untuk halaman How to Use. Berisi base frame dan children widgets
    - AboutPage() = Class untuk halaman About. Berisi base frame dan children widgets
    """
    def __init__(self):
        super().__init__()
        self.title("Trigonometri Converter")
        self.iconbitmap("icon_white.png")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
        self.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Halaman yang ingin ditampilkan pertama kali ketika program dijalankan
        self.current_page = FrontPage(self)
        self.current_page.create_widgets()
        
    def show_page(self, page_name):
        """
        Method dari Class App. berfungsi untuk berganti halaman. Menghancurkan base frame
        dari halaman saat ini dan memasang ulang halaman yang akan ditampilkan dengan memanggil
        method create_widgets dari masing-masing class halaman.
        """
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
    Halaman awal dari program. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """
    def __init__(self, master):
        super().__init__(master)
        self.logo_image = ctk.CTkImage(
            dark_image=Image.open("icon_white.png"), size=(150, 150)
        )
        self.front_frame = ctk.CTkFrame(
            master=self,
            width=350,
            height=470,
            border_width=3,
        )
        self.title = ctk.CTkLabel(
            master=self.front_frame,
            text="TRIGONOMETRI CONVERTER",
            wraplength=300,
            font=ctk.CTkFont(family=FONT, size=30, weight="bold"),
        )
        self.logo = ctk.CTkLabel(
            master=self.front_frame,
            image=self.logo_image,
            text=None,
            bg_color="transparent",
            fg_color=None,
        )
        self.start_button = ctk.CTkButton(
            master=self.front_frame,
            width=200,
            height=45,
            text="Mulai",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: App.show_page(master, "FungsiPage"),
        )
        self.help_button = ctk.CTkButton(
            master=self.front_frame,
            width=200,
            height=45,
            text="Materi",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
        )
        self.about_button = ctk.CTkButton(
            master=self.front_frame,
            width=200,
            height=45,
            text="Tentang Kami",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: App.show_page(master, "AboutPage"),
        )

    def create_widgets(self):
        """
        Method dari class FrontPage untuk memasang widgets dan frame
        """
        self.grid(column=0, row=0, sticky="nsew")
        self.front_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.title.place(relx=0.5, y=60, anchor="center")
        self.logo.place(relx=0.5, y=105, anchor="n")
        self.start_button.place(relx=0.5, y=320, anchor="s")
        self.help_button.place(relx=0.5, y=375, anchor="s")
        self.about_button.place(relx=0.5, y=430, anchor="s")


class HelpPage(ctk.CTkFrame):
    """
    Halaman dari How to Use. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """
    def __init__(self, master=App):
        super().__init__(master)
        pass

    def create_widgets(self):
        """
        Method dari class HelpPage untuk memasang widgets dan frame
        """
        pass


# Untuk menjalankan window
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()
