import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox as msgbox
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from trigonometri import Trigonometri

# Variable
FONT = "Helvetica"

# BG_COLOR_1 =
# BG_COLOR_2 =
# BG_COLOR_3 =
ACCENT_COLOR_1 = "B3A5EF"
ACCENT_COLOR_2 = "#AC92EA"
ACCENT_COLOR_3 = "#967ADA"


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
        # self.x_ranges = np.arange(-5, 5, 0.01)
        self.x_ranges = (
            0,
            30,
            45,
            60,
            90,
            120,
            135,
            150,
            180,
            210,
            225,
            240,
            270,
            300,
            315,
            330,
            360,
        )
        self.graph_x_ranges = np.radians(np.arange(0, 360, 0.1))

        # Default variables
        self.trig = Trigonometri()
        self.table_results = self.trig.table_sin(0, 0, self.x_ranges)
        self.graph_results = self.trig.graph_sin(0, 0, self.graph_x_ranges)

        # Konfigurasi grid untuk 3 frame untuk parent FungsiPage
        self.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="a", minsize=380)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")

        # Frame untuk menempatkan fungsi
        self.left_frame = ctk.CTkFrame(
            master=self,
            width=380,
            border_width=None,
            corner_radius=None,
        )
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_title = ctk.CTkLabel(
            master=self.left_frame,
            text="TRIGONOMETRI CONVERTER",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
        )
        self.back_button = ctk.CTkButton(
            master=self.left_frame,
            text="Back",
            width=120,
            height=40,
            font=ctk.CTkFont(family=FONT, size=15, weight="normal"),
            command=lambda: master.show_page("FrontPage"),
        )
        self.enter_button = ctk.CTkButton(
            master=self.left_frame,
            text="Enter",
            width=120,
            height=40,
            font=ctk.CTkFont(family=FONT, size=15, weight="normal"),
            command=lambda: self.enter_pressed(),
        )

        # Frame untuk menempatkan grafik
        self.graph_frame = ctk.CTkFrame(
            master=self,
        )
        self.graph_title = ctk.CTkLabel(
            master=self.graph_frame,
            text="GRAFIK FUNGSI",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
        )
        # Frame untuk menempatkan tabel
        self.table_frame = ctk.CTkFrame(master=self)
        self.table_title = ctk.CTkLabel(
            master=self.table_frame,
            text="TABEL SUDUT ISTIMEWA",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
        )

        # Frame untuk menempatkan input
        self.input_frame = ctk.CTkFrame(
            master=self.left_frame,
            width=330,
            height=480,
            border_width=None,
            fg_color="#333333",
        )
        self.pilih_text = ctk.CTkLabel(
            master=self.left_frame,
            text="Pilih fungsi Trigonometri:",
            font=ctk.CTkFont(family=FONT, size=18, weight="normal"),
            fg_color=None,
            bg_color="transparent",
        )
        self.sin = TrigEquation(
            master=self.input_frame,
            page=self,
            width=250,
            height=73,
            border_width=2,
            corner_radius=None,
            fg_color="#333333",
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
            border_width=2,
            corner_radius=None,
            fg_color="#333333",
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
            border_width=2,
            corner_radius=None,
            fg_color="#333333",
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
            border_width=2,
            corner_radius=None,
            fg_color="#333333",
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
            border_width=2,
            corner_radius=None,
            fg_color="#333333",
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
            border_width=2,
            corner_radius=None,
            fg_color="#333333",
            name="Cotan",
            value="cotan",
            equation="Cotan",
        )
        self.cotan.left_entry.configure(textvariable=self.cotan_l_entry)
        self.cotan.right_entry.configure(textvariable=self.cotan_r_entry)

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
                    self.table_results = self.trig.table_sin(
                        self.sin_l_entry.get(), self.sin_r_entry.get(), self.x_ranges
                    )
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_sin(
                        self.sin_l_entry.get(),
                        self.sin_r_entry.get(),
                        self.graph_x_ranges,
                    )
                case "cos":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.cos_l_entry.get()} Cos {self.cos_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_cos(
                        self.cos_l_entry.get(), self.cos_r_entry.get(), self.x_ranges
                    )
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_cos(
                        self.sin_l_entry.get(),
                        self.sin_r_entry.get(),
                        self.graph_x_ranges,
                    )
                case "tan":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.tan_l_entry.get()} Tan {self.tan_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_tan(
                        self.tan_l_entry.get(), self.tan_r_entry.get(), self.x_ranges
                    )
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_tan(
                        self.sin_l_entry.get(),
                        self.sin_r_entry.get(),
                        self.graph_x_ranges,
                    )

                case "cosec":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.cosec_l_entry.get()} Cosec {self.cosec_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_cosec(
                        self.cosec_l_entry.get(),
                        self.cosec_r_entry.get(),
                        self.x_ranges,
                    )
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_cosec(
                        self.sin_l_entry.get(),
                        self.sin_r_entry.get(),
                        self.graph_x_ranges,
                    )
                case "sec":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.sec_l_entry.get()} Sec {self.sec_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_sec(
                        self.sec_l_entry.get(), self.sec_r_entry.get(), self.x_ranges
                    )
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_sec(
                        self.sin_l_entry.get(),
                        self.sin_r_entry.get(),
                        self.graph_x_ranges,
                    )
                case "cotan":
                    # Memasukkan judul fungsi
                    self.func_title = f"f(x) = {self.cotan_l_entry.get()} Cotan {self.cotan_r_entry.get()} x"
                    # Memasukkan nilai untuk argumen tabel
                    self.table_results = self.trig.table_cotan(
                        self.cotan_l_entry.get(),
                        self.cotan_r_entry.get(),
                        self.x_ranges,
                    )
                    # Memasukkan nilai untuk argumen grafik
                    self.graph_results = self.trig.graph_cotan(
                        self.sin_l_entry.get(),
                        self.sin_r_entry.get(),
                        self.graph_x_ranges,
                    )
            self.display_graph()
            self.display_table()
        else:
            msgbox.showinfo(
                title="Info",
                message="Pilih fungsi dahulu dengan menekan tombol lingkaran",
            )

    def create_widgets(self):
        """
        Method dari class FungsiPage untuk memasang widgets dan frame
        """
        self.grid(column=0, row=0, sticky="nsew")
        self.left_frame.grid(
            column=0, row=0, rowspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.table_frame.grid(
            column=1, row=2, columnspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.graph_frame.grid(
            column=1, row=0, padx=10, pady=10, columnspan=3, rowspan=2, sticky="nsew"
        )
        self.left_title.place(relx=0.5, y=40, anchor="center")
        self.graph_title.place(relx=0.5, y=40, anchor="center")
        self.table_title.place(relx=0.5, y=40, anchor="center")
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

    def display_graph(self):
        """
        Method untuk menampilkan grafik trigonometri
        """
        x = self.graph_x_ranges
        y = self.graph_results

        fig = Figure(figsize=(8, 4.3), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)

        # fig, ax = plt.subplots()

        self.axes = fig.add_subplot(
            111,
            title=self.func_title,
            xlabel="α",
            ylabel="f(x)",
            autoscaley_on=True,
        )
        self.axes.plot(x, y)
        self.axes.grid(True)
        if self.trig_var.get() == "tan" or "cosec" or "sec" or "cotan":
            print(self.trig_var.get())
            self.axes.set_ylim(-5,5, auto=True)

        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, y=85, anchor="n")

    def display_table(self):
        """
        Method untuk menampilkan tabel trigonometri dari sudut istimewa
        """
        value = [
            [
                "α",
                "0°",
                "30°",
                "45°",
                "60°",
                "90°",
                "120°",
                "135°",
                "150°",
                "180°",
                "210°",
                "225°",
                "240°",
                "270°",
                "300°",
                "315°",
                "330°",
                "360°",
            ],
            self.table_results,
        ]

        table = CTkTable(
            master=self.table_frame,
            column=18,
            row=2,
            corner_radius=None,
            font=ctk.CTkFont(family="Helvetica", size=15, weight="normal"),
            values=value,
        )
        table.place(relx=0.5, y=85, relwidth=0.9, relheight=0.25, anchor="n")


class TrigEquation(ctk.CTkFrame):
    def __init__(
        self,
        master: str = None,
        page: str = None,
        name: str = None,
        value: str = None,
        equation: str = None,
        **kwargs,
    ):
        super().__init__(master, **kwargs)
        validate_cmd = self.register(self.validate_input)

        self.button = ctk.CTkRadioButton(
            master=self,
            radiobutton_width=20,
            radiobutton_height=20,
            text=name,
            value=value,
            variable=page.trig_var,
            font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
        )
        self.func_label = ctk.CTkLabel(
            master=self,
            width=100,
            height=30,
            text="f(x) = ",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.left_entry = ctk.CTkEntry(
            master=self,
            width=40,
            height=30,
            placeholder_text="0",
            state="normal",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        self.equation = ctk.CTkLabel(
            master=self,
            width=100,
            height=30,
            text=equation,
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.right_entry = ctk.CTkEntry(
            master=self,
            width=40,
            height=30,
            placeholder_text="0",
            state="normal",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        self.x_label = ctk.CTkLabel(
            master=self,
            text="x",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.button.place(x=20, y=20, anchor="w")
        self.func_label.place(x=30, y=50, anchor="w")
        self.left_entry.place(x=80, y=50, anchor="w")
        self.equation.place(x=130, y=50, anchor="w")
        self.right_entry.place(x=190, y=50, anchor="w")
        self.x_label.place(x=240, y=50, anchor="w")

    def validate_input(self, new_value):
        if new_value.isdigit() or new_value == "":
            return len(new_value) <= 3
        else:
            return False
