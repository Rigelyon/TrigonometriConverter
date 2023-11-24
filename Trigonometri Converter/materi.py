import customtkinter as ctk
from PIL import Image

# variable
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

with open("license", "r") as file:
    text_eula = file.read()



class MateriPage(ctk.CTkFrame):
    """
    Halaman dari Materi. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """
    def __init__(self, master):
        super().__init__(master)
        self.grid(column=0, row=0, sticky="nsew")
        self.configure(fg_color=COLORS[1])
        self.master = master

        # Header
        self.header_frame = ctk.CTkFrame(self, height=120, corner_radius=30, border_width=4, border_color=COLORS[4],
            fg_color="White")
        self.main_icon = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/icon_black.png"),size=(75, 75))
        self.main_icon_label = ctk.CTkLabel(self.header_frame, text=None, bg_color="transparent", image=self.main_icon)
        self.main_title = ctk.CTkLabel(self.header_frame, text="TRIGONOMETRI CONVERTER", justify="left", wraplength=300,
            text_color=COLORS[10], font=ctk.CTkFont(family=FONT, size=33, weight="bold"))
        self.page_title = ctk.CTkLabel(self.header_frame, text="MATERI TRIGONOMETRI", justify="left", wraplength=300,
            text_color=COLORS[10], font=ctk.CTkFont(family=FONT, size=33, weight="bold"))

        self.current_page = PageOne(self, app=self.master)
        self.current_page.create_widgets()
        
    def show_page(self, page_name):
        """
        Method dari Class MateriPage. berfungsi untuk berganti halaman. Menghancurkan base frame
        dari halaman saat ini dan memasang ulang halaman yang akan ditampilkan dengan memanggil
        method create_widgets dari masing-masing class halaman.
        """
        if self.current_page is not None:
            self.current_page.destroy()

        match page_name:
            case "PageOne":
                self.current_page = PageOne(self, app=self.master)
                self.current_page.create_widgets()
            case "PageTwo":
                self.current_page = PageTwo(self)
                self.current_page.create_widgets()
            case "PageThree":
                self.current_page = PageThree(self)
                self.current_page.create_widgets()

    def create_widgets(self):
        """
        Method dari class AboutPage untuk memasang widgets dan frame
        """
        self.header_frame.place(relx=0.5, y=20, relwidth=0.85, anchor="n")
        self.page_title.place(relx=0.05, rely=0.5, anchor="w")
        self.main_icon_label.place(relx=0.7, rely=0.5, anchor="center")
        self.main_title.place(relx=0.75, rely=0.5, anchor="w")


class PageOne(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.configure(corner_radius=30, border_width=4, border_color=COLORS[4], fg_color="White")

        trigonometri_text = """Trigonometri adalah cabang ilmu dalam Matematika yang mempelajari hubungan antara sisi dan sudut pada segitiga. Hubungan itu biasanya dinyatakan sebagai perbandingan sinus, kosinus, dan tangen. 

Jenis-jenis Trigonometri:

Dengan:
x = AB = panjang sisi mendatar segitiga;
y = BC = panjang sisi tegak segitiga;
r = AC = panjang sisi miring atau sisi terpanjang segitiga; 
dan = besarnya sudut yang dibentuk oleh sisi-sisi segitiga.
        """

        self.trigonometri_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.trigonometri_label = ctk.CTkLabel(master=self.trigonometri_frame, width=550, height=35, text="Trigonometri", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.trigonometri_text = ctk.CTkLabel(master=self.trigonometri_frame, text=trigonometri_text, wraplength=560, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.triangle_image = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/triangle_image.png"), size=(300,280))
        self.triangle_image_label = ctk.CTkLabel(master=self, image=self.triangle_image, text=None)

        self.arrow_icon = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow.png"), size=(40,20))
        self.arrow_icon_flip = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow_flip.png"), size=(40,20))
        self.back_button = ctk.CTkButton(master=self, width=200, height=45, text=None,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon,
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: app.show_page("FrontPage"))
        self.next_button = ctk.CTkButton(master=self, width=200, height=45, text=None,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon_flip,
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: master.show_page("PageTwo"))

    def create_widgets(self):
        self.place(relx=0.5, y=180, relwidth=0.85, relheight=0.7, anchor="n")

        self.trigonometri_frame.place(relx=0.97, rely=0.5, relheight=0.87, anchor="e")
        self.trigonometri_label.place(relx=0.5, y=0, anchor="n")
        self.trigonometri_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.triangle_image_label.place(x=300, y=220, anchor="center")
    
        self.back_button.place(relx=0.03, rely=0.90, anchor="w")
        self.next_button.place(relx=0.97, rely=0.90, anchor="e")


class PageTwo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=30, border_width=4, border_color=COLORS[4], fg_color="White")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        sin_text = """Sinus atau bisa disingkat sin adalah perbandingan antara panjang sisi di depan sudut dan panjang sisi miring. Secara matematis, dirumuskan sebagai berikut.
        """
        cos_text = """Kosinus atau biasa disebut cos adalah perbandingan antara panjang sisi di samping sudut dan panjang sisi miring. Secara matematis, dirumuskan sebagai berikut.
        """
        tan_text = """Tangen atau biasa disebut tan adalah perbandingan antara panjang sisi di depan sudut dan panjang sisi di samping sudut. Secara matematis, dirumuskan sebagai berikut.
        """

        self.sin_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.sin_label = ctk.CTkLabel(master=self.sin_frame, width=550, height=35, text="Sinus", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.sin_text = ctk.CTkLabel(master=self.sin_frame, text=sin_text, wraplength=300, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.sin_equation = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/sin_equation.png"), size=(160*1.3,60*1.3))
        self.sin_equation_label = ctk.CTkLabel(master=self.sin_frame, image=self.sin_equation, text=None)

        self.cos_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.cos_label = ctk.CTkLabel(master=self.cos_frame, width=550, height=35, text="Cosinus", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.cos_text = ctk.CTkLabel(master=self.cos_frame, text=cos_text, wraplength=300, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.cos_equation = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/cos_equation.png"), size=(160*1.3,60*1.3))
        self.cos_equation_label = ctk.CTkLabel(master=self.cos_frame, image=self.cos_equation, text=None)

        self.tan_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.tan_label = ctk.CTkLabel(master=self.tan_frame, width=550, height=35, text="Tangen", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.tan_text = ctk.CTkLabel(master=self.tan_frame, text=tan_text, wraplength=300, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.tan_equation = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/tan_equation.png"), size=(160*1.3,60*1.3))
        self.tan_equation_label = ctk.CTkLabel(master=self.tan_frame, image=self.tan_equation, text=None)
        


        self.arrow_icon = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow.png"), size=(40,20))
        self.arrow_icon_flip = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow_flip.png"), size=(40,20))
        self.back_button = ctk.CTkButton(master=self, width=200, height=45, text=None,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon,
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: master.show_page("PageOne"))
        self.next_button = ctk.CTkButton(master=self, width=200, height=45, text=None,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon_flip,
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: master.show_page("PageThree"))

    def create_widgets(self):
        self.place(relx=0.5, y=180, relwidth=0.85, relheight=0.7, anchor="n")

        self.sin_frame.grid(column=0, row=0, padx=10, pady=35, sticky="nsew")
        self.sin_label.place(relx=0.5, y=0, relwidth=0.8, anchor="n")
        self.sin_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.sin_equation_label.place(relx=0.5, y=300, anchor="center")

        self.cos_frame.grid(column=1, row=0, padx=10, pady=35, sticky="nsew")
        self.cos_label.place(relx=0.5, y=0, relwidth=0.8, anchor="n")
        self.cos_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.cos_equation_label.place(relx=0.5, y=300, anchor="center")

        self.tan_frame.grid(column=2, row=0, padx=10, pady=35, sticky="nsew")
        self.tan_label.place(relx=0.5, y=0, relwidth=0.8, anchor="n")
        self.tan_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.tan_equation_label.place(relx=0.5, y=300, anchor="center")

        self.back_button.place(relx=0.03, rely=0.90, anchor="w")
        self.next_button.place(relx=0.97, rely=0.90, anchor="e")


class PageThree(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=30, border_width=4, border_color=COLORS[4], fg_color="White")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        cosec_text = """Kosekan adalah perbandingan antara panjang sisi miring segitiga dan panjang sisi di depan sudut. Dengan kata lain, kosekan merupakan kebalikan dari sinus. Secara matematis, dirumuskan sebagai berikut.
        """
        sec_text = """Sekan adalah perbandingan antara panjang sisi miring segitiga dan panjang sisi di samping sudut. Dengan kata lain, sekan merupakan kebalikan dari kosinus. Secara matematis, dirumuskan sebagai berikut.
        """
        cotan_text = """Kotangen adalah perbandingan antara panjang sisi di samping sudut dan panjang sisi di depan sudut. Kotangen merupakan kebalikan dari tangen yang secara matematis, dirumuskan sebagai berikut.
        """

        self.cosec_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.cosec_label = ctk.CTkLabel(master=self.cosec_frame, width=550, height=35, text="Cosecan", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.cosec_text = ctk.CTkLabel(master=self.cosec_frame, text=cosec_text, wraplength=300, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.cosec_equation = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/cosec_equation.png"), size=(160*1.3,65*1.3))
        self.cosec_equation_label = ctk.CTkLabel(master=self.cosec_frame, image=self.cosec_equation, text=None)

        self.sec_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.sec_label = ctk.CTkLabel(master=self.sec_frame, width=550, height=35, text="Secan", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.sec_text = ctk.CTkLabel(master=self.sec_frame, text=sec_text, wraplength=300, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.sec_equation = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/sec_equation.png"), size=(160*1.3,65*1.3))
        self.sec_equation_label = ctk.CTkLabel(master=self.sec_frame, image=self.sec_equation, text=None)

        self.cotan_frame = ctk.CTkFrame(master=self, width=600,
            corner_radius=30, border_width=None, border_color=COLORS[4], fg_color="white")
        self.cotan_label = ctk.CTkLabel(master=self.cotan_frame, width=550, height=35, text="Cotangen", 
            text_color="white", corner_radius=25, fg_color=COLORS[4],
            font=ctk.CTkFont(family=FONT, size=18, weight="bold"))
        self.cotan_text = ctk.CTkLabel(master=self.cotan_frame, text=cotan_text, wraplength=300, justify="left",
            anchor="n", font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
        self.cotan_equation = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/cotan_equation.png"), size=(160*1.3,65*1.3))
        self.cotan_equation_label = ctk.CTkLabel(master=self.cotan_frame, image=self.cotan_equation, text=None)

        self.arrow_icon = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow.png"), size=(40,20))
        self.arrow_icon_flip = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow_flip.png"), size=(40,20))
        self.back_button = ctk.CTkButton(master=self, width=200, height=45, text=None,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon,
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            command=lambda: master.show_page("PageTwo"))
        # self.next_button = ctk.CTkButton(master=self, width=200, height=45, text=None,
        #     text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8], image=self.arrow_icon_flip,
        #     font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
        #     command=lambda: master.show_page("PageOne"))

    def create_widgets(self):
        """
        Method dari class AboutPage untuk memasang widgets dan frame
        """
        self.place(relx=0.5, y=180, relwidth=0.85, relheight=0.7, anchor="n")

        self.cosec_frame.grid(column=0, row=0, padx=10, pady=35, sticky="nsew")
        self.cosec_label.place(relx=0.5, y=0, relwidth=0.8, anchor="n")
        self.cosec_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.cosec_equation_label.place(relx=0.5, y=300, anchor="center")

        self.sec_frame.grid(column=1, row=0, padx=10, pady=35, sticky="nsew")
        self.sec_label.place(relx=0.5, y=0, relwidth=0.8, anchor="n")
        self.sec_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.sec_equation_label.place(relx=0.5, y=300, anchor="center")

        self.cotan_frame.grid(column=2, row=0, padx=10, pady=35, sticky="nsew")
        self.cotan_label.place(relx=0.5, y=0, relwidth=0.8, anchor="n")
        self.cotan_text.place(relx=0.5, y=65, relwidth=0.95, relheight=0.7, anchor="n")
        self.cotan_equation_label.place(relx=0.5, y=300, anchor="center")

        self.back_button.place(relx=0.03, rely=0.90, anchor="w")
        # self.next_button.place(relx=0.97, rely=0.90, anchor="e")