from turtle import bgcolor
import customtkinter as ctk

size = (800, 600)

app = ctk.CTk()
app.title("Program Fungsi")
app.geometry(f"{size[0]}x{size[1]}")
app.minsize(size[0], size[1])

main_frame = ctk.CTkFrame(master=app, fg_color="white", corner_radius=None)
main_frame.pack(expand=True, fill="both")


def front_page(parent):
    # half_color = ctk.CTkFrame(
    #     master=parent,
    #     height=size[1] / 2,
    #     fg_color="#2196f3",
    # )
    # half_color.pack(expand=True, fill="x", side="top", anchor="n")

    frame = ctk.CTkFrame(
        master=parent,
        width=400,
        height=300,
        corner_radius=None,
        border_width=None,
        border_color="#0d47a1",
        fg_color="#2196f3",
    )
    frame.place(x=size[0] / 2, y=(size[1] / 2), anchor="center")

    title = ctk.CTkLabel(
        master=parent,
        width=400,
        height=50,
        text="Program Fungsi",
        text_color="black",
        font=ctk.CTkFont(family="Helvetica", size=36, weight="bold"),
    )
    title.place(x=size[0] / 2, y=(size[1] / 2) - 200, anchor="center")


front_page(main_frame)

# class App(ctk.CTk):
#     def __init__(self, title, size):
#         super().__init__()
#         self.title(title)
#         self.geometry(f"{size[0]},{size[1]}")
#         self.minsize(size[0], size[1])

#         self.frame = MainFrame(self).pack(expand=True, fill="both")


# class MainFrame(ctk.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
#         # ctk.CTkLabel(self, anchor="n", fg_color="red").pack(expand=True, fill="both")
#         self.front_page(master=self).pack(expand=True, fill="both")

#     def front_page(self, master):
#         frame = ctk.CTkFrame(self).pack()
#         ctk.CTkLabel(master= frame, anchor="n", fg_color="blue").pack(expand=True, fill="both")
#         return frame


if __name__ == "__main__":
    app.mainloop()
