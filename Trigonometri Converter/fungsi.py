import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox as msgbox
from PIL import Image
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backend_bases import MouseButton
import matplotlib.ticker as ticker

from trigonometri import Trigonometri


# Variable
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

class FungsiPage(ctk.CTkFrame):
    """
    Halaman dari program trigonometri. Class berbentuk frame untuk base frame. Children
    berisi widgets berupa button untuk navigasi ke halaman lain.
    """

    def __init__(self, master=None):
        super().__init__(master)
        # Variable untuk mengontrol radio button
        self.trig_var = ctk.StringVar()

        # Variable untuk mengakses entry pilihan
        self.sin_l_entry = ctk.IntVar()
        self.sin_r_entry = ctk.IntVar()
        self.cos_l_entry = ctk.IntVar()
        self.cos_r_entry = ctk.IntVar()
        self.tan_l_entry = ctk.IntVar()
        self.tan_r_entry = ctk.IntVar()
        self.cosec_l_entry = ctk.IntVar()
        self.cosec_r_entry = ctk.IntVar()
        self.sec_l_entry = ctk.IntVar()
        self.sec_r_entry = ctk.IntVar()
        self.cotan_l_entry = ctk.IntVar()
        self.cotan_r_entry = ctk.IntVar()

        # Variable untuk menentukan range dari X-Axis
        self.x_ranges = (0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360)
        self.graph_x_ranges = np.radians(np.arange(0, 360, 0.1))

        # Default variables
        self.trig = Trigonometri()
        self.table_results = self.trig.table_sin(0, 0, self.x_ranges)
        self.graph_results = self.trig.graph_sin(0, 0, self.graph_x_ranges)
        self.func_title = "f(x) = "

        # Konfigurasi grid untuk 3 frame untuk parent FungsiPage
        self.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="a", minsize=380)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")

        self.configure(fg_color=COLORS[1])

        # Frame untuk menempatkan fungsi
        self.left_frame = ctk.CTkFrame(master=self, width=380, border_width=4, corner_radius=30, bg_color="transparent",
            fg_color="White", border_color=COLORS[4])
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_title = ctk.CTkLabel(master=self.left_frame, text="TRIGONOMETRI CONVERTER", text_color="black",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"))
        self.arrow_icon = ctk.CTkImage(dark_image=Image.open("Trigonometri Converter/Assets/arrow.png"), size=(40,20))
        self.back_button = ctk.CTkButton(master=self.left_frame, text=None, width=120, height=40, image=self.arrow_icon,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8],
            font=ctk.CTkFont(family=FONT, size=15, weight="normal"),
            command=lambda: master.show_page("FrontPage"))
        # self.enter_icon = ctk.CTkImage()
        self.enter_button = ctk.CTkButton(master=self.left_frame, text="Enter", width=120, height=40,
            text_color=COLORS[0], corner_radius=25, fg_color=COLORS[5], hover_color=COLORS[8],
            font=ctk.CTkFont(family=FONT, size=15, weight="bold"),
            command=lambda: self.enter_pressed())

        # Frame untuk menempatkan grafik
        self.graph_frame = ctk.CTkFrame(master=self, border_width=4, corner_radius=30, bg_color="transparent",
            fg_color="White", border_color=COLORS[4])
        self.graph_title = ctk.CTkLabel(master=self.graph_frame, text="GRAFIK FUNGSI", text_color="black",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"))

        # Frame untuk menempatkan tabel
        self.table_frame = ctk.CTkFrame(master=self, border_width=4, corner_radius=30, bg_color="transparent",
            fg_color="White", border_color=COLORS[4])
        self.table_title = ctk.CTkLabel(master=self.table_frame, text="TABEL SUDUT ISTIMEWA", text_color="black",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"))

        # Frame untuk menempatkan input
        self.input_frame = ctk.CTkFrame(master=self.left_frame, width=330, height=480, border_width=None,
            corner_radius=30, bg_color="transparent", fg_color="White", border_color=COLORS[4])
        self.pilih_text = ctk.CTkLabel(master=self.left_frame, text="Pilih fungsi Trigonometri:", text_color="black",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"))
            
        self.sin = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            name="Sinus",
            value="sin",
            equation="Sin",
        )
        self.sin.left_entry.configure(textvariable=self.sin_l_entry)
        self.sin.right_entry.configure(textvariable=self.sin_r_entry)
        self.cos = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            name="Cosinus",
            value="cos",
            equation="Cos",
        )
        self.cos.left_entry.configure(textvariable=self.cos_l_entry)
        self.cos.right_entry.configure(textvariable=self.cos_r_entry)
        self.tan = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            name="Tangen",
            value="tan",
            equation="Tan",
        )
        self.tan.left_entry.configure(textvariable=self.tan_l_entry)
        self.tan.right_entry.configure(textvariable=self.tan_r_entry)
        self.cosec = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            name="Cosecan",
            value="cosec",
            equation="Cosec",
        )
        self.cosec.left_entry.configure(textvariable=self.cosec_l_entry)
        self.cosec.right_entry.configure(textvariable=self.cosec_r_entry)
        self.sec = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            name="Secan",
            value="sec",
            equation="Secan",
        )
        self.sec.left_entry.configure(textvariable=self.sec_l_entry)
        self.sec.right_entry.configure(textvariable=self.sec_r_entry)
        self.cotan = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            name="Cotan",
            value="cotan",
            equation="Cotan",
        )
        self.cotan.left_entry.configure(textvariable=self.cotan_l_entry)
        self.cotan.right_entry.configure(textvariable=self.cotan_r_entry)

        self.coord_label = ctk.CTkLabel(
            master=self.graph_frame,
            font=ctk.CTkFont(family=FONT, size=13, weight="normal"),
        )

    def enter_pressed(self):
        """
        Method untuk menjalankan command ketika tombol enter ditekan. Menghandle event berdasarkan pilihan
        fungsi trigonometri yang dipilih.
        """

        if self.trig_var.get() != "":
            match self.trig_var.get():
                case "sin":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.sin_l_entry.get()} Sin {self.sin_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_sin(self.sin_l_entry.get(), self.sin_r_entry.get(), self.x_ranges)
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_sin(self.sin_l_entry.get(), self.sin_r_entry.get(), self.graph_x_ranges)
                case "cos":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.cos_l_entry.get()} Cos {self.cos_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_cos(self.cos_l_entry.get(), self.cos_r_entry.get(), self.x_ranges)
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_cos(self.cos_l_entry.get(), self.cos_r_entry.get(), self.graph_x_ranges)
                case "tan":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.tan_l_entry.get()} Tan {self.tan_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_tan(self.tan_l_entry.get(), self.tan_r_entry.get(), self.x_ranges)
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_tan(self.tan_l_entry.get(), self.tan_r_entry.get(), self.graph_x_ranges)

                case "cosec":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.cosec_l_entry.get()} Cosec {self.cosec_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_cosec( self.cosec_l_entry.get(), self.cosec_r_entry.get(), self.x_ranges)
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_cosec(self.cosec_l_entry.get(), self.cosec_r_entry.get(), self.graph_x_ranges)
                case "sec":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.sec_l_entry.get()} Sec {self.sec_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_sec(self.sec_l_entry.get(), self.sec_r_entry.get(), self.x_ranges)
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_sec(self.sec_l_entry.get(), self.sec_r_entry.get(), self.graph_x_ranges)
                case "cotan":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.cotan_l_entry.get()} Cotan {self.cotan_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_cotan(self.cotan_l_entry.get(), self.cotan_r_entry.get(), self.x_ranges)
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_cotan(self.cotan_l_entry.get(), self.cotan_r_entry.get(), self.graph_x_ranges)
            self.display_graph()
            self.display_table()
        else:
            msgbox.showinfo(title="Info", message="Pilih fungsi dahulu dengan menekan tombol lingkaran")

    def create_widgets(self):
        """
        Method dari class FungsiPage untuk memasang widgets dan frame
        """
        self.grid(column=0, row=0, sticky="nsew")
        self.left_frame.grid(column=0, row=0, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.table_frame.grid(column=1, row=2, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.graph_frame.grid(column=1, row=0, padx=10, pady=10, columnspan=3, rowspan=2, sticky="nsew")
        self.left_title.place(relx=0.5, y=40, anchor="center")
        self.back_button.place(relx=0.05, rely=0.95, anchor="w")
        self.enter_button.place(relx=0.95, rely=0.95, anchor="e")
        self.input_frame.grid(column=0, row=0, padx=20, pady=100, sticky="nsew")
        self.pilih_text.place(x=20, y=85, anchor="w")

        self.sin.pack(anchor="n", fill="x")
        self.cos.pack(anchor="n", fill="x")
        self.tan.pack(anchor="n", fill="x")
        self.cosec.pack(anchor="n", fill="x")
        self.sec.pack(anchor="n", fill="x")
        self.cotan.pack(anchor="n", fill="x")

    def on_mouse_hover(self, event):
        if event.inaxes:
            x, y = np.degrees(event.xdata), event.ydata
            self.coord_label.configure(text=f"Coordinates: ({x:.2f}°,{y:.2f})", text_color="black")
            self.coord_label.place(relx=0.5, y=460, anchor="n")

    def display_graph(self):
        """
        Method untuk menampilkan grafik trigonometri
        """
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()

        x = self.graph_x_ranges
        y = self.graph_results

        fig = Figure(figsize=(9, 4.8), dpi=100)
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)

        self.axes = fig.add_subplot(111, title=self.func_title, xlabel="α", ylabel="f(x)",)

        if self.trig_var.get() in ["tan", "cosec", "sec", "cotan"]:
            self.axes.set_ylim(-11, 11)
        else:
            self.axes.set_autoscaley_on = True

        # Mengubah radians menjadi derajat untuk label sumbu-x
        degree_formatter = ticker.FuncFormatter(lambda x, _: f"{int(np.degrees(x))}°")
        self.axes.xaxis.set_major_formatter(degree_formatter)

        # Memasang label untuk sumbu-x
        self.axes.set_xticks(np.radians(self.x_ranges))
        self.axes.set_xticklabels([f"{deg}°" for deg in self.x_ranges], rotation=45, ha="right")

        self.axes.plot(x, y)
        self.axes.grid(True)

        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0.5, y=65, anchor="n")
        self.canvas.mpl_connect("motion_notify_event", self.on_mouse_hover)

        self.graph_title.place(relx=0.5, y=40, anchor="center")

    def display_table(self):
        """
        Method untuk menampilkan tabel trigonometri dari sudut istimewa
        """
        if hasattr(self, "table"):
            self.table.destroy()

        value = [["α", "0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°", "210°", "225°",
            "240°", "270°", "300°", "315°", "330°", "360°"], self.table_results]


        self.table = CTkTable(
            master=self.table_frame,
            column=18,
            row=2,
            corner_radius=25,
            colors=[COLORS[3], COLORS[2]],
            text_color="black",
            bg_color="transparent",
            font=ctk.CTkFont(family="Helvetica", size=13, weight="normal"),
            values=value,
        )
        self.table.place(relx=0.5, y=85, relwidth=0.9, relheight=0.25, anchor="n")

        self.table_title.place(relx=0.5, y=40, anchor="center")


class TrigEquation(ctk.CTkFrame):
    def __init__(self, master: str = None, page: str = None, name: str = None, value: str = None,
        equation: str = None, **kwargs,):
        super().__init__(master, **kwargs)
        validate_cmd = self.register(self.validate_input)
        self.configure(fg_color="white", corner_radius=25, border_width=2, border_color=COLORS[3])

        self.button = ctk.CTkRadioButton(
            master=self,
            radiobutton_width=20,
            radiobutton_height=20,
            text=name,
            text_color='black',
            border_color=COLORS[4],
            hover_color=COLORS[5],
            value=value,
            variable=page.trig_var,
            font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
        )
        self.func_label = ctk.CTkLabel(
            master=self,
            width=100,
            height=30,
            text="f(x) = ",
            text_color="black",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.left_entry = ctk.CTkEntry(
            master=self,
            width=40,
            height=30,
            placeholder_text="0",
            text_color="black",
            placeholder_text_color="gray",
            fg_color="white",
            border_color="black",
            state="normal",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        self.equation = ctk.CTkLabel(
            master=self,
            width=100,
            height=30,
            text=equation,
            text_color="black",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.right_entry = ctk.CTkEntry(
            master=self,
            width=40,
            height=30,
            placeholder_text="0",
            text_color="black",
            placeholder_text_color="gray",
            fg_color="white",
            border_color="black",
            state="normal",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        self.x_label = ctk.CTkLabel(
            master=self,
            text="x",
            text_color="black",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.button.place(x=20, y=20, anchor="w")
        self.func_label.place(x=30, y=50, anchor="w")
        self.left_entry.place(x=80, y=50, anchor="w")
        self.equation.place(x=130, y=50, anchor="w")
        self.right_entry.place(x=190, y=50, anchor="w")
        self.x_label.place(x=240, y=50, anchor="w")

    def validate_input(self, new_value):
        if all(
            char.isdigit() or (char == "-" and new_value.count("-") == 1)
            for char in new_value
        ):
            return len(new_value) <= 3
        else:
            return False
