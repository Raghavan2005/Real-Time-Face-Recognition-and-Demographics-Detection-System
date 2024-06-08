from create_dataset import start_capture
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, PhotoImage

names = set()

class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("Face Recognition Project By Priya Dharshini")
        self.resizable(False, False)
        self.geometry("690x380")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            self.destroy()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        render = PhotoImage(file='homepagepic.png')
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=1, rowspan=4, sticky="nsew")
        label = tk.Label(self, text="Face Recognition Project", font=self.controller.title_font, fg="#263942")
        label3 = tk.Label(self, text="Velalar Institution of Technology", font=self.controller.title_font, fg="#263942")
        label.grid(row=0, sticky="ew")
        label3.grid(row=1, sticky="ew")
        button1 = tk.Button(self, text="Face Recognition", fg="#ffffff", bg="#263942", command=lambda: self.controller.show_frame("PageThree"))
        button3 = tk.Button(self, text="Quit", fg="#263942", bg="#ffffff", command=self.on_closing)
        button1.grid(row=2, column=0, ipady=1, ipadx=1)
        button3.grid(row=3, column=0, ipady=7, ipadx=1)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do not leave me Alone?"):
            self.controller.destroy()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.numimglabel = tk.Label(self, text="Face Recognition", font='Helvetica 14 bold', fg="#263942")
        self.myname = tk.Label(self, text="Project By Priya Dharshini", font='Helvetica 12 bold', fg="#263942")
        self.numimglabel.grid(row=0, column=1, columnspan=2, sticky="ew", pady=10, padx=250)
        self.myname.grid(row=1, column=1, columnspan=2, sticky="ew", pady=10, padx=250)
        self.capturebutton = tk.Button(self, text="Start RealTime", fg="#ffffff", bg="#263942", command=self.capimg)
        self.button7 = tk.Button(self, text="Go to Home Page", fg="#ffffff", bg="#263942", command=lambda: self.controller.show_frame("StartPage"))
        self.capturebutton.grid(row=2, column=1, ipadx=5, ipady=4, padx=250, pady=70)
        self.button7.grid(row=3, column=1, ipadx=5, ipady=4, padx=250, pady=10)

    def capimg(self):
        self.numimglabel.config(text="Face Recognition Started on Live")
        messagebox.showinfo("INSTRUCTION", "process Started Pls wait")
        start_capture('none')
        self.numimglabel.config(text="Face Recognition Ended")

app = MainUI()
app.iconphoto(True, tk.PhotoImage(file='icon.ico'))
app.mainloop()
