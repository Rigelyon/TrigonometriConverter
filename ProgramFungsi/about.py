import customtkinter as ctk
from PIL import Image

# variable
FONT = "Helvetica"
authors = """
    Authors:
    1. Pandu Dwi Ashidiqi (237006105)
    2. Isep Hidayattulah (237006101)
    3. Delvina Salma Hidayah (237006103)
    """

with open("license", "r") as file:
    text_eula = file.read()


class AboutPage(ctk.CTkFrame):
    """
    Halaman dari About. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """
    def __init__(self, master):
        super().__init__(master)
        self.grid(column=0, row=0, sticky="nsew")
        self.logo_image = ctk.CTkImage(
            dark_image=Image.open("icon_white.png"), size=(70, 70)
        )
        self.about_frame = ctk.CTkFrame(
            master=self,
            width=500,
            height=600,
            border_width=3,
        )
        self.title = ctk.CTkLabel(
            master=self.about_frame,
            text="TRIGONOMETRI CONVERTER",
            wraplength=300,
            justify="left",
            font=ctk.CTkFont(family=FONT, size=30, weight="bold"),
        )
        self.authors_label = ctk.CTkLabel(
            master=self.about_frame,
            text=authors,
            justify="left",
            font=ctk.CTkFont(family=FONT, size=14, weight="normal"),
        )
        self.license_frame = ctk.CTkScrollableFrame(
            master=self.about_frame,
            width=400,
            height=200,
            label_text="EULA",
            label_font=ctk.CTkFont(family=FONT, size=12, weight="bold"),
        )
        self.license_text = ctk.CTkLabel(
            master=self.license_frame, text=text_eula, wraplength=400, justify="left"
        )
        self.back_button = ctk.CTkButton(
            master=self.about_frame,
            width=200,
            height=45,
            text="Back",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: master.show_page("FrontPage"),
        )
        self.logo = ctk.CTkLabel(
            master=self.about_frame, image=self.logo_image, text=None
        )

    def create_widgets(self):
        """
        Method dari class AboutPage untuk memasang widgets dan frame
        """
        self.about_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.logo.place(x=130, y=65, anchor="center")
        self.title.place(x=310, y=65, anchor="center")
        self.authors_label.place(x=50, y=130, anchor="nw")
        self.license_frame.place(relx=0.5, y=370, anchor="center")
        self.license_text.pack(fill="both")
        self.back_button.place(relx=0.5, rely=0.95, anchor="s")
