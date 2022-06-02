import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGEFONT = ("Gulim", 35)


class tkinterApp(tk.Tk):
    def __init__(self, char, *args, **kwargs):
        tk.Tk.__init__(self, char, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page9):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="MBTI test with Python", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)


        button1 = ttk.Button(self, text="시작하기",
                             command=lambda: controller.show_frame(Page1))
        button1.grid(row=5, column=1, padx=10, pady=10)


class Page1(tk.Frame):
    def __init__(self, EorI, parent, controller):
        E = 0
        I = 0

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="1번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        q1 = tk.IntVar()
        r1a = Radiobutton(self, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", value=1, variable=q1)
        r1a.grid(row=2, column=1, padx=10, pady=10)
        r1b = Radiobutton(self, text="2. 나는 모르는 사람을 만나는 일이 곤하다.", value=2, variable=q1)
        r1b.grid(row=3, column=1, padx=10, pady=10)

        a1 = q1.get()
        if a1 == 1:
            E += 1
        elif a1 == 2:
            I += 1


        q2 = tk.IntVar()
        r1a = Radiobutton(self, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", value=3, variable=q2)
        r1a.grid(row=4, column=1, padx=10, pady=10)
        r1b = Radiobutton(self, text="2. 나는 모르는 사람을 만나는 일이 곤하다.", value=4, variable=q2)
        r1b.grid(row=5, column=1, padx=10, pady=10)

        a2 = q1.get()
        if a2 == 1:
            E += 1
        elif a2 == 2:
            I += 1

        q3 = tk.IntVar()
        r1a = Radiobutton(self, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", value=5, variable=q3)
        r1a.grid(row=6, column=1, padx=10, pady=10)
        r1b = Radiobutton(self, text="2. 나는 모르는 사람을 만나는 일이 곤하다.", value=6, variable=q3)
        r1b.grid(row=7, column=1, padx=10, pady=10)

        a3 = q3.get()
        if a3 == 1:
            E += 1
        elif a3 == 2:
            I += 1


        if E >= 2:
            EorI = E
        else:
            EorI = I


        button1 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page2))
        button1.grid(row=8, column=1, padx=10, pady=10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="2번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r2a = Radiobutton(self, text="1.어떠어떠한 성격", value=3)
        r2a.grid(row=2, column=1, padx=10, pady=10)
        r2b = Radiobutton(self, text="2.어떠어떠한 성격", value=4)
        r2b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page1))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page3))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="3번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r3a = Radiobutton(self, text="1.어떠어떠한 성격", value=5)
        r3a.grid(row=2, column=1, padx=10, pady=10)
        r3b = Radiobutton(self, text="2.어떠어떠한 성격", value=6)
        r3b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page2))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page4))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="4번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r4a = Radiobutton(self, text="1.어떠어떠한 성격", value=7)
        r4a.grid(row=2, column=1, padx=10, pady=10)
        r4b = Radiobutton(self, text="2.어떠어떠한 성격", value=8)
        r4b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page3))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page5))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="5번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r5a = Radiobutton(self, text="1.어떠어떠한 성격", value=9)
        r5a.grid(row=2, column=1, padx=10, pady=10)
        r5b = Radiobutton(self, text="2.어떠어떠한 성격", value=10)
        r5b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page4))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page6))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="6번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r6a = Radiobutton(self, text="1.어떠어떠한 성격", value=11)
        r6a.grid(row=2, column=1, padx=10, pady=10)
        r6b = Radiobutton(self, text="2.어떠어떠한 성격", value=12)
        r6b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page5))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page7))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="7번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r7a = Radiobutton(self, text="1.어떠어떠한 성격", value=13)
        r7a.grid(row=2, column=1, padx=10, pady=10)
        r7b = Radiobutton(self, text="2.어떠어떠한 성격", value=14)
        r7b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page6))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page8))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="8번 질문", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        r8a = Radiobutton(self, text="1.어떠어떠한 성격", value=15)
        r8a.grid(row=2, column=1, padx=10, pady=10)
        r8b = Radiobutton(self, text="2.어떠어떠한 성격", value=16)
        r8b.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page7))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page9))
        button2.grid(row=5, column=1, padx=10, pady=10)


class Page9(tk.Frame, Page1):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=EorI, font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page8))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="마치기",
                             command=lambda: controller.destroy())
        button2.grid(row=5, column=1, padx=10, pady=10)


def main():
    app = tkinterApp()
    app.mainloop()


if __name__ == "__main__":
    main()