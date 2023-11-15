import customtkinter as ctk
from CTkTable import CTkTable
import numpy as np
from tksheet import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

FONT = "Helvetica"

# BG_COLOR_1 = 
# BG_COLOR_2 = 
# BG_COLOR_3 = 
ACCENT_COLOR_1 = "B3A5EF"
ACCENT_COLOR_2 = "#AC92EA"
ACCENT_COLOR_3 = "#967ADA"


class FungsiPage(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.trig = ctk.StringVar()
        self.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="a", minsize=380)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")
        self.left_frame = ctk.CTkFrame(
            master=self,
            width=380,
            border_width=None,
            corner_radius=None,
        )
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.graph_frame = ctk.CTkFrame(
            master=self,
        )
        self.table_frame = ctk.CTkFrame(master=self)
        self.left_title = ctk.CTkLabel(
            master=self.left_frame,
            text="TRIGONOMETRI CONVERTER",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
        )
        self.graph_title = ctk.CTkLabel(
            master=self.graph_frame,
            text="GRAFIK FUNGSI",
            font=ctk.CTkFont(family=FONT, size=22, weight="bold"),
        )
        self.table_title = ctk.CTkLabel(
            master=self.table_frame,
            text="TABEL SUDUT ISTIMEWA",
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
            equation="y = Sin",
        )
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
            equation="y = Cos",
        )
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
            equation="y = Tan",
        )
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
            equation="y = Cosec",
        )
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
            equation="y = Secan",
        )
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
            equation="y = Cotan",
        )

    def enter_pressed(self):
        self.display_graph()
        self.display_table()

    def create_widgets(self):
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
        fig = Figure(figsize=(8, 4.3), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)

        # x_values = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
        # x = np.radians(x_values)
        x = np.arange(-3, 3, 0.01)
        y = np.sin(4 * x)

        axes = fig.add_subplot(111)
        axes.plot(y)
        axes.set_xlabel("Sudut Istimewa")
        axes.grid(True)

        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, y=85, anchor="n")
        print("Pressed")

    def display_table(self):
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
            ["Sin", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
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
        
        # table.place(relx=0.5, y=85, anchor="n")
        # table = Sheet(
        #     self.table_frame,
        #     width=700,
        #     height=150,
        #     show_header=False,
        #     show_row_index=False,
        #     show_top_left=False,
        #     show_x_scrollbar=False,
        #     show_y_scrollbar=False,
        #     header_height=30,
        #     column_width=60,
        #     row_height=30,
        #     align="center",
        #     font=("Arial", 12, "normal"),
        #     outline_thickness=2,
        #     horizontal_grid_to_end_of_window=True,
        #     vertical_grid_to_end_of_window=True,
        #     show_vertical_grid=True,
        #     show_horizontal_grid=True,

        #     frame_bg="black",
        #     data=value,
        # )
        # table.place(relx=0.5, y=85, relwidth=0.8, anchor="n")


class TrigEquation(ctk.CTkFrame):
    def __init__(
        self,
        master: str = None,
        page: str = None,
        name: str = None,
        value: str = None,
        equation: str = None,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self.button = ctk.CTkRadioButton(
            master=self,
            radiobutton_width=20,
            radiobutton_height=20,
            text=name,
            value=value,
            variable=page.trig,
            font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
            command=lambda: self.entry_unlock(),
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
        self.entry = ctk.CTkEntry(
            master=self,
            width=40,
            height=30,
            placeholder_text="0",
            state="disabled",
        )
        self.x_label = ctk.CTkLabel(
            master=self,
            text="x",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        )
        self.button.place(x=20, y=20, anchor="w")
        self.equation.place(x=30, y=50, anchor="w")
        self.entry.place(x=120, y=50, anchor="w")
        self.x_label.place(x=170, y=50, anchor="w")

    def entry_unlock(self):
        self.entry.configure(state="normal")
