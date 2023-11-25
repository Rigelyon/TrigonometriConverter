import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import sys, os

from fungsi import FungsiPage
from about import AboutPage
from materi import MateriPage


# Const untuk size window dan font
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 675
FONT = "Helvetica"

COLORS = {
    0:"#f0f7ff",
    1:"#e0effe",
    2:"#badffd",
    3:"#7cc6fd",
    4:"#37a9f9",
    5:"#0d8eea",
    6:"#016cc1",
    7:"#0259a2",
    8:"#064c86",
    9:"#0c406e",
    10:"#082849"
    }

def resource_path(relative_path):
        """ Mendapatkan absolut path untuk resource, bisa untuk dev atau Pyinstaller """
        try:
            # PyInstaller membuat sebuah folder temp dan menyimpan path di _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

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
        self.iconbitmap(resource_path("icon.ico"))
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
            case "MateriPage":
                self.state("zoomed")
                self.current_page = MateriPage(self)
                self.current_page.create_widgets()
            case "AboutPage":
                self.state("zoomed")
                self.current_page = AboutPage(self)
                self.current_page.create_widgets()


class FrontPage(ctk.CTkFrame):
    """
    Halaman awal dari program. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """

    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=COLORS[1])
        # self.configure(bg_color="transparent")
        # self.bind("<Configure>", self.on_resize)
        # self.bg_image = ctk.CTkImage(light_image=Image.open("Trigonometri Converter/Assets/bg.png"),size=(1920, 1080))
        # # Background
        # self.bg_label = ctk.CTkLabel(self, text=None, image=self.bg_image)
        # self.bg_label.place(relwidth=1, relheight=1)

        # Header frame
        self.header_frame = ctk.CTkFrame(self, height=120, corner_radius=30, border_width=4, border_color=COLORS[4],
            fg_color="White")

        self.unsil_icon = ctk.CTkImage(dark_image=Image.open(resource_path("Assets\\unsil_icon.png")), size=(90, 90))
        self.unsil_icon_label = ctk.CTkLabel(self.header_frame, text=None, bg_color="transparent", image=self.unsil_icon)

        self.main_icon = ctk.CTkImage(dark_image=Image.open(resource_path("Assets\\icon_black.png")),size=(90, 90))
        self.main_icon_label = ctk.CTkLabel(self.header_frame, text=None, bg_color="transparent", image=self.main_icon)

        self.main_title = ctk.CTkLabel(self.header_frame, text="TRIGONOMETRI CONVERTER", wraplength=300,
            text_color=COLORS[10], font=ctk.CTkFont(family=FONT, size=33, weight="bold"))

        # 
        self.middle_frame = ctk.CTkFrame(self, width=383, height=400, corner_radius=30, border_width=4, border_color=COLORS[4],
            fg_color="White")
        self.greetings_label = ctk.CTkLabel(self.middle_frame, text="Hello There...!!", text_color="black",
            font=ctk.CTkFont(family=FONT, size=60, weight="bold"))
        self.user_name = ctk.CTkLabel(self.middle_frame, text=f"{os.getlogin()}", text_color="black",
            font=ctk.CTkFont(family=FONT, size=35, weight="bold"))
        self.welcome_text = ctk.CTkLabel(self.middle_frame, text="Selamat datang di Trigonometri Converter.\nSilahkan tekan tombol untuk memulai!", 
            text_color="black", justify="left", font=ctk.CTkFont(family=FONT, size=22, weight="normal"))
        self.start_button = ctk.CTkButton(self.middle_frame, width=280, height=65, text="Mulai", text_color="white", 
            corner_radius=30, fg_color=COLORS[5], hover_color=COLORS[8],
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
            command=lambda: App.show_page(master, "FungsiPage"))
        self.materi_button = ctk.CTkButton(self.middle_frame, width=280, height=65, text="Materi", text_color="white",
            corner_radius=30, fg_color=COLORS[5], hover_color=COLORS[8],
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"), 
            command=lambda: App.show_page(master, "MateriPage"))    
        self.about_button = ctk.CTkButton(self.middle_frame, width=280, height=65, text="Tentang Kami", text_color="white",
            corner_radius=30, fg_color=COLORS[5], hover_color=COLORS[8],
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
            command=lambda: App.show_page(master, "AboutPage"))    

    # def on_resize(self, event):
    #     new_size = (event.width, event.height)
    #     self.bg_image.configure(size=new_size)

    def create_widgets(self):
        """
        Method dari class FrontPage untuk memasang widgets dan frame
        """
        self.grid(column=0, row=0, sticky="nsew")

        self.header_frame.place(relx=0.5, y=20, relwidth=0.85, anchor="n")
        self.main_icon_label.place(relx=0.09, rely=0.5, anchor="center")
        self.unsil_icon_label.place(relx=0.91, rely=0.5, anchor="center")
        self.main_title.place(relx=0.5, rely=0.5, anchor="center")

        self.middle_frame.place(relx=0.5, y=230, relwidth=0.85, anchor="n")
        self.greetings_label.place(relx=0.5, y=50, anchor="nw")
        self.user_name.place(relx=0.5, y=135, anchor="nw")
        self.welcome_text.place(relx=0.5, y=190, anchor="nw")
        self.start_button.place(relx=0.15, rely=0.15, anchor="nw")
        self.materi_button.place(relx=0.15, rely=0.5, anchor="w")
        self.about_button.place(relx=0.15, rely=0.85, anchor="sw")


# Untuk menjalankan window
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    app = App()
    app.mainloop()
