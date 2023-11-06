from turtle import bgcolor
import customtkinter as ctk

size = (800, 600)

app = ctk.CTk()
app.title("Program Fungsi")
# app.iconbitmap("ProgramFungsi\icon.png")
app.geometry(f"{size[0]}x{size[1]}")
app.minsize(size[0], size[1])
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

main_frame = ctk.CTkFrame(master=app, fg_color="white", corner_radius=None)
main_frame.pack(expand=True, fill="both")

def page_raise(page):
    pass

def about_page():
    frame_size = (800,600)
    frame = ctk.CTkFrame(
        master=main_frame,
        width=frame_size[0],
        height=frame_size[1],
        corner_radius=None,
        border_width=3,
        border_color="#1e88e5",
        fg_color="white",       
    )
    frame.pack()
    frame.lift()


def front_page(parent):
    main_frame.configure(fg_color="#2196f3")
    frame_size = (350,350)

    frame = ctk.CTkFrame(
        master=parent,
        width=frame_size[0],
        height=frame_size[1],
        corner_radius=None,
        border_width=3,
        border_color="#1e88e5",
        fg_color="white",
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = ctk.CTkLabel(
        master=frame,
        text="Program Fungsi",
        text_color="#2196f3",
        font=ctk.CTkFont(family="Helvetica", size=36, weight="bold"),
    )
    title.place(x=frame_size[0]/2,y=45, anchor="center")

    mulai_button = ctk.CTkButton(
        master=frame,
        width=200,
        height=45,
        fg_color="#64b5f6",
        text="Mulai",
        text_color="white",
        font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
    )
    mulai_button.place(x=frame_size[0]/2, y=(frame_size[1])-75, anchor="s")

    about_button = ctk.CTkButton(
        master=frame,
        width=200,
        height=45,
        fg_color="#64b5f6",
        text="About",
        text_color="white",
        font=ctk.CTkFont(family="Helvetica", size=18, weight="normal"),
        command=about_page
    )
    about_button.place(x=frame_size[0]/2, y=(frame_size[1])-20, anchor="s")

if __name__ == "__main__":
    front_page(main_frame)
    app.mainloop()
