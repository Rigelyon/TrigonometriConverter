import customtkinter as ctk
import numpy as np
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

with open("license", "r") as file:
    text_eula = file.read()

ctk.set_appearance_mode("dark")

# Define root window
app = ctk.CTk()
WIDTH = 1200
HEIGHT = 675
app.title("Trigonometri Converter")
icon = ctk.CTkImage(dark_image=Image.open("icon_white.png"))
app.after(201, lambda: app.iconbitmap("icon_white.png"))
app.geometry(f"{WIDTH}x{HEIGHT}+0,0")
app.minsize(WIDTH, HEIGHT)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# Define front page
page_front = ctk.CTkFrame(master=app)
page_front.grid(column=0, row=0, sticky="nsew")
page_front.grid_columnconfigure(1, weight=1)
page_front.grid_rowconfigure(1, weight=1)

# Define about page
page_about = ctk.CTkFrame(master=app)
page_about.grid(column=0, row=0, sticky="nsew")

# Define fungsi page
page_fungsi = ctk.CTkFrame(master=app)
page_fungsi.grid(column=0, row=0, sticky="nsew")
page_fungsi.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="a", minsize=380)
page_fungsi.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")

current_page = None
current_formula = None
fungsi_choice = ctk.StringVar()


# Page Switching
def show_page(page_name):
    global current_page
    if current_page is not None:
        for widget in current_page.winfo_children():
            widget.destroy()
    if page_name == page_front:
        front_page()
    elif page_name == page_about:
        about_page()
    elif page_name == page_fungsi:
        fungsi_page()

    current_page = page_name
    page_name.lift()


# Front Page content
def front_page():
    frame = ctk.CTkFrame(
        master=page_front,
        width=350,
        height=470,
        border_width=3,
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = ctk.CTkLabel(
        master=frame,
        text="TRIGONOMETRI CONVERTER",
        wraplength=300,
        font=ctk.CTkFont(family="Helvetica", size=30, weight="bold"),
    )
    title.place(relx=0.5, y=60, anchor="center")

    logo_image = ctk.CTkImage(dark_image=Image.open("icon_white.png"), size=(150, 150))
    logo = ctk.CTkLabel(
        master=frame, image=logo_image, text=None, bg_color="transparent", fg_color=None
    )
    logo.place(relx=0.5, y=105, anchor="n")

    START_BUTTON_POS = (0.5, 320)
    HELP_BUTTON_POS = (0.5, 375)
    ABOUT_BUTTON_POS = (0.5, 430)

    start_button = ctk.CTkButton(
        master=frame,
        width=200,
        height=45,
        text="Start",
        font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        command=lambda: show_page(page_fungsi),
    )
    start_button.place(relx=START_BUTTON_POS[0], y=START_BUTTON_POS[1], anchor="s")

    help_button = ctk.CTkButton(
        master=frame,
        width=200,
        height=45,
        text="How to Use",
        font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
    )
    help_button.place(relx=HELP_BUTTON_POS[0], y=HELP_BUTTON_POS[1], anchor="s")

    about_button = ctk.CTkButton(
        master=frame,
        width=200,
        height=45,
        text="About",
        font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        command=lambda: show_page(page_about),
    )
    about_button.place(relx=ABOUT_BUTTON_POS[0], y=ABOUT_BUTTON_POS[1], anchor="s")


# About Page content
def about_page():
    about_frame = ctk.CTkFrame(
        master=page_about,
        width=500,
        height=600,
        border_width=3,
    )
    about_frame.place(relx=0.5, rely=0.5, anchor="center")

    logo_image = ctk.CTkImage(dark_image=Image.open("icon_white.png"), size=(70, 70))
    logo = ctk.CTkLabel(master=about_frame, image=logo_image, text=None)

    title = ctk.CTkLabel(
        master=about_frame,
        text="TRIGONOMETRI CONVERTER",
        wraplength=300,
        justify="left",
        font=ctk.CTkFont(family="Helvetica", size=30, weight="bold"),
    )

    authors = """
Authors:
1. Pandu Dwi Ashidiqi (237006105)
2. Isep Hidayattulah (237006101)
3. Delvina Salma Hidayah (237006103)"""

    authors_label = ctk.CTkLabel(
        master=about_frame,
        text=authors,
        justify="left",
        font=ctk.CTkFont(family="Helvetica", size=14, weight="normal"),
    )

    license_frame = ctk.CTkScrollableFrame(
        master=about_frame,
        width=400,
        height=200,
        label_text="EULA",
        label_font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"),
    )

    license_text = ctk.CTkLabel(
        master=license_frame, text=text_eula, wraplength=400, justify="left"
    )

    back_button = ctk.CTkButton(
        master=about_frame,
        width=200,
        height=45,
        text="Back",
        font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        command=lambda: show_page(page_front),
    )

    logo.place(x=130, y=65, anchor="center")
    title.place(x=310, y=65, anchor="center")
    authors_label.place(x=50, y=130, anchor="nw")
    license_frame.place(relx=0.5, y=370, anchor="center")
    license_text.pack(fill="both")
    back_button.place(relx=0.5, rely=0.95, anchor="s")


# Fungsi page content
def fungsi_page():
    global fungsi_choice
    app.state("zoomed")

    # Define left frame and title
    left_frame = ctk.CTkFrame(
        master=page_fungsi,
        width=380,
        border_width=None,
        corner_radius=None,
    )
    left_frame.grid(column=0, row=0, rowspan=3, padx=10, pady=10, sticky="nsew")
    left_frame.grid_columnconfigure(0, weight=1)
    left_frame.grid_rowconfigure(0, weight=1)
    left_title = ctk.CTkLabel(
        master=left_frame,
        text="TRIGONOMETRI CONVERTER",
        font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"),
    )
    left_title.place(relx=0.5, y=40, anchor="center")

    # Define graph frame and title
    graph_frame = ctk.CTkFrame(
        master=page_fungsi,
    )
    graph_frame.grid(
        column=1, row=0, padx=10, pady=10, columnspan=3, rowspan=2, sticky="nsew"
    )
    graph_title = ctk.CTkLabel(
        master=graph_frame,
        text="GRAFIK FUNGSI",
        font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"),
    )
    graph_title.place(relx=0.5, y=40, anchor="center")

    # Define table frame and title
    table_frame = ctk.CTkFrame(master=page_fungsi)
    table_frame.grid(column=1, row=2, columnspan=3, padx=10, pady=10, sticky="nsew")
    table_title = ctk.CTkLabel(
        master=table_frame,
        text="TABEL SUDUT ISTIMEWA",
        font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"),
    )
    table_title.place(relx=0.5, y=40, anchor="center")

    def enter_pressed():
        graph_widgets()
        table_widgets()

    def left_widgets():
        back_button = ctk.CTkButton(
            master=left_frame,
            text="Back",
            width=120,
            height=40,
            font=ctk.CTkFont(family="Helvetica", size=15, weight="normal"),
            command=lambda: show_page(page_front),
        )
        back_button.place(relx=0.05, rely=0.95, anchor="w")

        enter_button = ctk.CTkButton(
            master=left_frame,
            text="Enter",
            width=120,
            height=40,
            font=ctk.CTkFont(family="Helvetica", size=15, weight="normal"),
            command=lambda: enter_pressed(),
        )
        enter_button.place(relx=0.95, rely=0.95, anchor="e")

        def input_frame(parent):
            def radio_choice(radio_name):
                if radio_name == "Sin":
                    sin_entry.configure(state="normal", placeholder_text="0")
                    cos_entry.configure(state="disabled", placeholder_text=" ")
                    tan_entry.configure(state="disabled", placeholder_text=" ")
                    cosec_entry.configure(state="disabled", placeholder_text=" ")
                    sec_entry.configure(state="disabled", placeholder_text=" ")
                    cotan_entry.configure(state="disabled", placeholder_text=" ")
                    get_formula = sin_formula.cget("text")
                elif radio_name == "Cos":
                    sin_entry.configure(state="disabled", placeholder_text=" ")
                    cos_entry.configure(state="normal", placeholder_text="0")
                    tan_entry.configure(state="disabled", placeholder_text=" ")
                    cosec_entry.configure(state="disabled", placeholder_text=" ")
                    sec_entry.configure(state="disabled", placeholder_text=" ")
                    cotan_entry.configure(state="disabled", placeholder_text=" ")
                    get_formula = cos_formula.cget("text")
                elif radio_name == "Tan":
                    sin_entry.configure(state="disabled", placeholder_text=" ")
                    cos_entry.configure(state="disabled", placeholder_text=" ")
                    tan_entry.configure(state="normal", placeholder_text="0")
                    cosec_entry.configure(state="disabled", placeholder_text=" ")
                    sec_entry.configure(state="disabled", placeholder_text=" ")
                    cotan_entry.configure(state="disabled", placeholder_text=" ")
                    get_formula = tan_formula.cget("text")
                elif radio_name == "Cosec":
                    sin_entry.configure(state="disabled", placeholder_text=" ")
                    cos_entry.configure(state="disabled", placeholder_text=" ")
                    tan_entry.configure(state="disabled", placeholder_text=" ")
                    cosec_entry.configure(state="normal", placeholder_text="0")
                    sec_entry.configure(state="disabled", placeholder_text=" ")
                    cotan_entry.configure(state="disabled", placeholder_text=" ")
                elif radio_name == "Sec":
                    sin_entry.configure(state="disabled", placeholder_text=" ")
                    cos_entry.configure(state="disabled", placeholder_text=" ")
                    tan_entry.configure(state="disabled", placeholder_text=" ")
                    cosec_entry.configure(state="disabled", placeholder_text=" ")
                    sec_entry.configure(state="normal", placeholder_text="0")
                    cotan_entry.configure(state="disabled", placeholder_text=" ")
                elif radio_name == "Cotan":
                    sin_entry.configure(state="disabled", placeholder_text=" ")
                    cos_entry.configure(state="disabled", placeholder_text=" ")
                    tan_entry.configure(state="disabled", placeholder_text=" ")
                    cosec_entry.configure(state="disabled", placeholder_text=" ")
                    sec_entry.configure(state="disabled", placeholder_text=" ")
                    cotan_entry.configure(state="normal", placeholder_text="0")
                return get_formula

            input_frame = ctk.CTkFrame(
                master=parent,
                width=330,
                height=480,
                border_width=2,
                fg_color="#333333",
            )
            input_frame.grid(column=0, row=0, padx=20, pady=80, sticky="nsew")

            pilih_text = ctk.CTkLabel(
                master=input_frame,
                text="Pilih fungsi Trigonometri:",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Sinus
            sin_button = ctk.CTkRadioButton(
                master=input_frame,
                radiobutton_width=20,
                radiobutton_height=20,
                text="Sinus",
                value="Sin",
                variable=fungsi_choice,
                font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
                command=lambda: radio_choice("Sin"),
            )

            sin_formula = ctk.CTkLabel(
                master=input_frame,
                width=100,
                height=30,
                text="y = Sin",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            sin_entry = ctk.CTkEntry(
                master=input_frame,
                width=40,
                height=30,
                placeholder_text="0",
                state="normal",
            )

            sin_x_label = ctk.CTkLabel(
                master=input_frame,
                text="x",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Cosinus
            cos_button = ctk.CTkRadioButton(
                master=input_frame,
                radiobutton_width=20,
                radiobutton_height=20,
                text="Cosinus",
                value="Cos",
                variable=fungsi_choice,
                font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
                command=lambda: radio_choice("Cos"),
            )

            cos_formula = ctk.CTkLabel(
                master=input_frame,
                width=100,
                height=30,
                text="y = Cos",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            cos_entry = ctk.CTkEntry(
                master=input_frame,
                width=40,
                height=30,
                placeholder_text="0",
                state="normal",
            )

            cos_x_label = ctk.CTkLabel(
                master=input_frame,
                text="x",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Tangent
            tan_button = ctk.CTkRadioButton(
                master=input_frame,
                radiobutton_width=20,
                radiobutton_height=20,
                text="Tangent",
                value="Tan",
                variable=fungsi_choice,
                font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
                command=lambda: radio_choice("Tan"),
            )

            tan_formula = ctk.CTkLabel(
                master=input_frame,
                width=100,
                height=30,
                text="y = Tan",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            tan_entry = ctk.CTkEntry(
                master=input_frame,
                width=40,
                height=30,
                placeholder_text="0",
                state="normal",
            )

            tan_x_label = ctk.CTkLabel(
                master=input_frame,
                text="x",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Cosecan
            cosec_button = ctk.CTkRadioButton(
                master=input_frame,
                radiobutton_width=20,
                radiobutton_height=20,
                text="Cosecan",
                value="Cosec",
                variable=fungsi_choice,
                font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
                command=lambda: radio_choice("Cosec"),
            )

            cosec_formula = ctk.CTkLabel(
                master=input_frame,
                width=100,
                height=30,
                text="y = Cosec",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            cosec_entry = ctk.CTkEntry(
                master=input_frame,
                width=40,
                height=30,
                placeholder_text="0",
                state="normal",
            )

            cosec_x_label = ctk.CTkLabel(
                master=input_frame,
                text="x",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Secan
            sec_button = ctk.CTkRadioButton(
                master=input_frame,
                radiobutton_width=20,
                radiobutton_height=20,
                text="Secan",
                value="Sec",
                variable=fungsi_choice,
                font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
                command=lambda: radio_choice("Sec"),
            )

            sec_formula = ctk.CTkLabel(
                master=input_frame,
                width=100,
                height=30,
                text="y = Sec",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            sec_entry = ctk.CTkEntry(
                master=input_frame,
                width=40,
                height=30,
                placeholder_text="0",
                state="normal",
            )

            sec_x_label = ctk.CTkLabel(
                master=input_frame,
                text="x",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Cotangen
            cotan_button = ctk.CTkRadioButton(
                master=input_frame,
                radiobutton_width=20,
                radiobutton_height=20,
                text="Cotangen",
                value="Cotan",
                variable=fungsi_choice,
                font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
                command=lambda: radio_choice("Cotan"),
            )

            cotan_formula = ctk.CTkLabel(
                master=input_frame,
                width=100,
                height=30,
                text="y = Cotan",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            cotan_entry = ctk.CTkEntry(
                master=input_frame,
                width=40,
                height=30,
                placeholder_text="0",
                state="normal",
            )

            cotan_x_label = ctk.CTkLabel(
                master=input_frame,
                text="x",
                font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
            )

            # Label Placement
            pilih_text.place(x=20, y=25, anchor="w")

            # Sinus
            sin_button.place(x=20, y=65, anchor="w")
            sin_formula.place(x=30, y=100, anchor="w")
            sin_entry.place(x=130, y=100, anchor="w")
            sin_x_label.place(x=180, y=100, anchor="w")

            # Cosinus
            cos_button.place(x=20, y=145, anchor="w")
            cos_formula.place(x=30, y=180, anchor="w")
            cos_entry.place(x=130, y=180, anchor="w")
            cos_x_label.place(x=180, y=180, anchor="w")

            # Tangent
            tan_button.place(x=20, y=225, anchor="w")
            tan_formula.place(x=30, y=260, anchor="w")
            tan_entry.place(x=130, y=260, anchor="w")
            tan_x_label.place(x=180, y=260, anchor="w")

            # Cosecan
            cosec_button.place(x=20, y=305, anchor="w")
            cosec_formula.place(x=30, y=340, anchor="w")
            cosec_entry.place(x=130, y=340, anchor="w")
            cosec_x_label.place(x=180, y=340, anchor="w")

            # Secan
            sec_button.place(x=20, y=385, anchor="w")
            sec_formula.place(x=30, y=420, anchor="w")
            sec_entry.place(x=130, y=420, anchor="w")
            sec_x_label.place(x=180, y=420, anchor="w")

            # Cotangen
            cotan_button.place(x=20, y=465, anchor="w")
            cotan_formula.place(x=30, y=500, anchor="w")
            cotan_entry.place(x=130, y=500, anchor="w")
            cotan_x_label.place(x=180, y=500, anchor="w")

        return (input_frame(left_frame),)

    def graph_widgets():
        fig = Figure(figsize=(8, 4.5), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)

        # x_values = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
        # x = np.radians(x_values)
        x = np.arange(-3, 3, 0.01)
        print(x)
        y = np.sin(2 * np.pi * x)

        axes = fig.add_subplot(111)
        axes.plot(y)
        axes.set_xlabel("Sudut Istimewa")
        axes.grid(True)

        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")

    def table_widgets():
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
            ["Sin", 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
        ]
        # table = CTkTable(
        #     master=table_frame,
        #     column=17,
        #     row=2,
        #     corner_radius=None,
        #     font=ctk.CTkFont(family="Helvetica", size=15, weight="normal"),
        #     values=value,
        # )
        # table.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.35, anchor="center")

    return left_widgets()


if __name__ == "__main__":
    page_front.lift()
    front_page()
    app.mainloop()
