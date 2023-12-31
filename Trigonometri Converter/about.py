import customtkinter as ctk
import sys, os
from PIL import Image

# Const
FONT = "Helvetica"
authors = """
    Authors:
    1. Pandu Dwi Ashidiqi (237006105)
    2. Isep Hidayattulah (237006101)
    3. Delvina Salma Hidayah (237006103)
    """
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
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

# Membaca LICENSE.txt
with open(resource_path("LICENSE.txt"), "r")as file:
    text_eula = file.read()


class AboutPage(ctk.CTkFrame):
    """
    Halaman dari About. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """
    def __init__(self, master):
        super().__init__(master)
        self.grid(column=(0), row=0, sticky="nsew")
        self.configure(fg_color=COLORS[1])

        # Header
        self.header_frame = ctk.CTkFrame(self, height=120, corner_radius=30, border_width=4, border_color=COLORS[4],
            fg_color="White")
        self.main_icon = ctk.CTkImage(dark_image=Image.open(resource_path("Assets\\icon_black.png")),size=(75, 75))
        self.main_icon_label = ctk.CTkLabel(self.header_frame, text=None, bg_color="transparent", image=self.main_icon)
        self.main_title = ctk.CTkLabel(self.header_frame, text="TRIGONOMETRI CONVERTER", justify="left", wraplength=300,
            text_color=COLORS[10], font=ctk.CTkFont(family=FONT, size=33, weight="bold"))
        self.page_title = ctk.CTkLabel(self.header_frame, text="TENTANG KAMI", justify="left", wraplength=300,
            text_color=COLORS[10], font=ctk.CTkFont(family=FONT, size=33, weight="bold"))

        # Middle frame
        self.middle_frame = ctk.CTkFrame(master=self, corner_radius=30, border_width=4, 
            border_color=COLORS[4], fg_color="White")
        self.middle_frame.grid_columnconfigure((0,1), weight=1)
        self.middle_frame.grid_rowconfigure(0, weight=1)

        # Authors sub frame
        self.authors_frame = ctk.CTkFrame(master=self.middle_frame, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.authors_label = ctk.CTkLabel(master=self.authors_frame, height=35, text="Authors", text_color="white", 
            corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.authors_icon = ctk.CTkImage(dark_image=Image.open(resource_path("Assets\\user_blue.png")), size=(55,55))
        self.authors_icon_label_1 = ctk.CTkLabel(master=self.authors_frame, image=self.authors_icon, text=None)
        self.authors_icon_label_2 = ctk.CTkLabel(master=self.authors_frame, image=self.authors_icon, text=None)
        self.authors_icon_label_3 = ctk.CTkLabel(master=self.authors_frame, image=self.authors_icon, text=None)
        self.authors_name_1 = ctk.CTkLabel(master=self.authors_frame, text="Pandu Dwi Ashidiqi",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"))
        self.authors_name_2 = ctk.CTkLabel(master=self.authors_frame, text="Isep Hidayattulah",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"))
        self.authors_name_3 = ctk.CTkLabel(master=self.authors_frame, text="Delvina Salma Hidayah",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"))
        self.authors_details_1 = ctk.CTkLabel(master=self.authors_frame, text="(237006105)",
            font=ctk.CTkFont(family=FONT, size=15, weight="bold"))
        self.authors_details_2 = ctk.CTkLabel(master=self.authors_frame, text="(237006101)",
            font=ctk.CTkFont(family=FONT, size=15, weight="bold"))
        self.authors_details_3 = ctk.CTkLabel(master=self.authors_frame, text="(237006103)",
            font=ctk.CTkFont(family=FONT, size=15, weight="bold"))

        # License sub frame
        self.license_frame = ctk.CTkFrame(master=self.middle_frame, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.license_label = ctk.CTkLabel(master=self.license_frame, height=35, text="EULA", text_color="white", 
            corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.license_text = ctk.CTkTextbox(master=self.license_frame, activate_scrollbars=True,
            font=ctk.CTkFont(family=FONT, size=13, weight="normal"))
        self.license_text.insert("0.0",text=text_eula)
        self.license_text.configure(state="disabled")

        self.arrow_icon = ctk.CTkImage(dark_image=Image.open(resource_path("Assets\\arrow.png")), size=(40,20))
        self.back_button = ctk.CTkButton(master=self.middle_frame, width=200, height=45, text=None,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon,
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: master.show_page("FrontPage"))
  
    def create_widgets(self):
        """
        Method dari class AboutPage untuk memasang widgets dan frame
        """
        self.header_frame.place(relx=0.5, y=20, relwidth=0.85, anchor="n")
        self.page_title.place(relx=0.05, rely=0.5, anchor="w")
        self.main_icon_label.place(relx=0.7, rely=0.5, anchor="center")
        self.main_title.place(relx=0.75, rely=0.5, anchor="w")

        self.middle_frame.place(relx=0.5, y=180, relwidth=0.85, relheight=0.7, anchor="n")

        self.authors_frame.grid(column=0, row=0, padx=10, pady=35, sticky="nsew")
        self.authors_label.place(relx=0.5, y=0, relwidth=0.95, anchor="n")
        self.authors_icon_label_1.place(x=50, y=105, anchor="center")
        self.authors_icon_label_2.place(x=50, y=205, anchor="center")
        self.authors_icon_label_3.place(x=50, y=305, anchor="center")
        self.authors_name_1.place(x=100, y=90, anchor="w")
        self.authors_name_2.place(x=100, y=190, anchor="w")
        self.authors_name_3.place(x=100, y=290, anchor="w")
        self.authors_details_1.place(x=100, y=115, anchor="w")
        self.authors_details_2.place(x=100, y=215, anchor="w")
        self.authors_details_3.place(x=100, y=315, anchor="w")
        
        self.license_frame.grid(column=1, row=0, padx=10, pady=35, sticky="nsew")
        self.license_label.place(relx=0.5, y=0, relwidth=0.95, anchor="n")
        self.license_text.place(relx=0.5, y=70, relwidth=0.9, relheight=0.95, anchor="n")

        self.back_button.place(relx=0.03, rely=0.90, anchor="w")
