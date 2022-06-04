import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGEFONT = ("Gulim", 35)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="1번 질문")
        label.grid(row=0, column=0, padx=10, pady=10)

        q1 = tk.IntVar()
        r1a = Radiobutton(self, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", value=1, variable=q1)
        r1a.grid(row=0, column=1, padx=10, pady=10)
        r1b = Radiobutton(self, text="2. 나는 모르는 사람을 만나는 일이 곤하다.", value=2, variable=q1)
        r1b.grid(row=1, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="2번 질문")
        label.grid(row=2, column=0, padx=10, pady=10)

        q2 = tk.IntVar()
        r1c = Radiobutton(self, text="1. 나는 말하면서 생각하고 대화도중 결심할 때가 있다.", value=3, variable=q2)
        r1c.grid(row=2, column=1, padx=10, pady=10)
        r1d = Radiobutton(self, text="2. 나는 의견을 말하기에 앞서 신중히 생각하는 편이다.", value=4, variable=q2)
        r1d.grid(row=3, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="3번 질문")
        label.grid(row=4, column=0, padx=10, pady=10)

        q3 = tk.IntVar()
        r1e = Radiobutton(self, text="1. 일할때 적막한 것 보다는 어느정도의 소리가 도움이 된다.", value=5, variable=q3)
        r1e.grid(row=4, column=1, padx=10, pady=10)
        r1f = Radiobutton(self, text="2. 나는 소음이 있는 곳에서 일을 할 때 일하기가 힘들다.", value=6, variable=q3)
        r1f.grid(row=5, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page2))
        button1.grid(row=6, column=1, padx=10, pady=10)

        a1 = q1.get()
        a2 = q2.get()
        a3 = q3.get()

    # def EorI(self, a1, a2, a3):
    #     E = 0
    #     I = 0
    #
    #     if a1 == 1:
    #         E += 1
    #     elif a1 == 2:
    #         I += 1
    #
    #     if a2 == 3:
    #         E += 1
    #     elif a2 == 4:
    #         I += 1
    #
    #     if a3 == 5:
    #         E += 1
    #     elif a3 == 6:
    #         I += 1
    #
    #     if E >= 2:
    #         m = "E"
    #     else:
    #         I = "I"


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="4번 질문")
        label.grid(row=0, column=0, padx=10, pady=10)

        q4 = tk.IntVar()
        r2a = Radiobutton(self, text="1. 나는 경험으로 판단한다.", value=7, variable=q4)
        r2a.grid(row=0, column=1, padx=10, pady=10)
        r2b = Radiobutton(self, text="2. 나는 떠오르는 직관으로 판단한다.", value=8, variable=q4)
        r2b.grid(row=1, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="5번 질문")
        label.grid(row=2, column=0, padx=10, pady=10)

        q5 = tk.IntVar()
        r2a = Radiobutton(self, text="1. 나는 약도를 구체적으로 그린다.", value=9, variable=q5)
        r2a.grid(row=2, column=1, padx=10, pady=10)
        r2b = Radiobutton(self, text="2. 나는 약도를 구체적으로 그리기 어렵다.", value=10, variable=q5)
        r2b.grid(row=3, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="6번 질문")
        label.grid(row=4, column=0, padx=10, pady=10)

        q6 = tk.IntVar()
        r2a = Radiobutton(self, text="1. 나는 늘 다니던 길로 다니는 것이 좋다.", value=11, variable=q6)
        r2a.grid(row=4, column=1, padx=10, pady=10)
        r2b = Radiobutton(self, text="2. 나는 한번도 안가본 새로운 길로 다니는 것을 좋아한다.", value=12, variable=q6)
        r2b.grid(row=5, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page1))
        button1.grid(row=6, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page3))
        button2.grid(row=7, column=1, padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="7번 질문")
        label.grid(row=0, column=0, padx=10, pady=10)

        q7 = tk.IntVar()
        r3a = Radiobutton(self, text="1. 나는 슬픈영화를 볼때 쉽게 감정이입이 되지 않는다.", value=11, variable=q7)
        r3a.grid(row=0, column=1, padx=10, pady=10)
        r3b = Radiobutton(self, text="2. 나는 슬픈영화를 볼때 심하게 감정이입을 해서 쉽게 눈물이 난다.", value=12, variable=q7)
        r3b.grid(row=1, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="8번 질문")
        label.grid(row=2, column=0, padx=10, pady=10)

        q8= tk.IntVar()
        r3a = Radiobutton(self, text="1. 나는 능력있다는 소리를 듣기 좋아한다.", value=13, variable=q8)
        r3a.grid(row=2, column=1, padx=10, pady=10)
        r3b = Radiobutton(self, text="2. 나는 따뜻한 마음을 가졌다는 소리를 듣기 좋아한다.", value=14, variable=q8)
        r3b.grid(row=3, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="9번 질문")
        label.grid(row=4, column=0, padx=10, pady=10)

        q9 = tk.IntVar()
        r3a = Radiobutton(self, text="1. 나는 옳고 그름이 확실해서 직선적으로 말하는 편이다.", value=15, variable=q9)
        r3a.grid(row=4, column=1, padx=10, pady=10)
        r3b = Radiobutton(self, text="2. 나는 주로 남을 배려하는 말을 하는 편이다.", value=16, variable=q9)
        r3b.grid(row=5, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page2))
        button1.grid(row=6, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page4))
        button2.grid(row=7, column=1, padx=10, pady=10)


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="10번 질문")
        label.grid(row=0, column=0, padx=10, pady=10)

        q10 = tk.IntVar()
        r4a = Radiobutton(self, text="1. 나는 계획에 의해 일을 처리하는 편이다.", value=17, variable=q10)
        r4a.grid(row=0, column=1, padx=10, pady=10)
        r4b = Radiobutton(self, text="2. 나는 마지막에 임박했을때 일을 처리하는 편이다.", value=18, variable=q10)
        r4b.grid(row=1, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="11번 질문")
        label.grid(row=2, column=0, padx=10, pady=10)

        q11 = tk.IntVar()
        r4a = Radiobutton(self, text="1. 나는 평소에 정리정돈을 자주 하는 편이다.", value=19, variable=q11)
        r4a.grid(row=2, column=1, padx=10, pady=10)
        r4b = Radiobutton(self, text="2. 나는 날을 잡아서 한번에 몰아서 정리하는 편이다.", value=20, variable=q11)
        r4b.grid(row=3, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="12번 질문")
        label.grid(row=4, column=0, padx=10, pady=10)

        q12 = tk.IntVar()
        r4a = Radiobutton(self, text="1. 나는 일을 할 때 사람들과 친해지는 편이다.", value=21, variable=q12)
        r4a.grid(row=4, column=1, padx=10, pady=10)
        r4b = Radiobutton(self, text="2. 나는 놀면서 사람들과 친해지는 편이다.", value=22, variable=q12)
        r4b.grid(row=5, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page3))
        button1.grid(row=6, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="다음 페이지",
                             command=lambda: controller.show_frame(Page5))
        button2.grid(row=7, column=1, padx=10, pady=10)


class Page5(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="결과", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="이전 페이지",
                             command=lambda: controller.show_frame(Page4))
        button1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="마치기",
                             command=lambda: controller.destroy())
        button2.grid(row=5, column=1, padx=10, pady=10)


# mbti 결정 함수

# def mbti_test_EI(m, b, t, i):
#     print("\n당신의 MBTI는 {}{}{}{}입니다.\n".format(m,b,t,i))
#     if m == "E" and b == "S" and t == "T" and i == "J":
#         print("▷ ESTJ_사업가형 : 사무적, 실용적, 현실적인 스타일\n▷ 나와 가장 잘 맞는 MBTI는? : INFP\n▷ 나와 가장 잘 안맞는 MBTI는? : INFJ")
#     elif m == "E" and b == "N" and t == "T" and i == "J":
#         print("▷ ENTJ_지도자형 : 비전을 갖고 타인을 활력적으로 인도\n▷ 나와 가장 잘 맞는 MBTI는? : ISFP\n▷ 나와 가장 잘 안맞는 MBTI는? : ISFJ")
#     elif m == "E" and b == "N" and t == "T" and i == "P":
#         print("▷ ENTP_발명가형 : 풍부한 상상력으로 새로운 것에 도전\n▷ 나와 가장 잘 맞는 MBTI는? : ISFJ\n▷ 나와 가장 잘 안맞는 MBTI는? : ISFP")
#     elif m == "I" and b == "N" and t == "T" and i == "J":
#         print("▷ INTJ_과학자형 : 전체를 조합하여 비전을 제시하는 사람\n▷ 나와 가장 잘 맞는 MBTI는? : ESFP\n▷ 나와 가장 잘 안맞는 MBTI는? : ESFJ")
#     elif m == "I" and b == "N" and t == "T" and i == "P":
#         print("▷ INTP_아이디어형 : 비평적인 관점을 가진 뛰어난 전략가\n▷ 나와 가장 잘 맞는 MBTI는? : ESFJ\n▷ 나와 가장 잘 안맞는 MBTI는? : ESFP")
#     elif m == "E" and b == "S" and t == "F" and i == "J":
#         print("▷ ESFJ_친선도모형 : 친절, 현실감을 바탕으로 타인에게 봉사\n▷ 나와 가장 잘 맞는 MBTI는? : INTP\n▷ 나와 가장 잘 안맞는 MBTI는? : INTJ")
#     elif m == "I" and b == "S" and t == "T" and i == "J":
#         print("▷ ISTJ_소금형 : 한번 시작한 일은 끝까지 해내는 성격\n▷ 나와 가장 잘 맞는 MBTI는? : ENFP\n▷ 나와 가장 잘 안맞는 MBTI는? : ENFJ")
#     elif m == "I" and b == "S" and t == "F" and i == "J":
#         print("▷ ISFJ_권력형 : 성실하고 온화하며 협조를 잘하는 사람\n▷ 나와 가장 잘 맞는 MBTI는? : ENTP\n▷ 나와 가장 잘 안맞는 MBTI는? : ENTJ")
#     elif m == "E" and b == "N" and t == "F" and i == "J":
#         print("▷ ENFJ_언변능숙형 : 타인의 성장을 도모하고 협동하는 사람\n▷ 나와 가장 잘 맞는 MBTI는? : ISTP\n▷ 나와 가장 잘 안맞는 MBTI는? : ISTJ")
#     elif m == "E" and b == "N" and t == "F" and i == "P":
#         print("▷ ENFP_스파크형 : 열정적으로 새 관계를 만드는 사람\n▷ 나와 가장 잘 맞는 MBTI는? : ISTJ\n▷ 나와 가장 잘 안맞는 MBTI는? : ISTP")
#     elif m == "I" and b == "N" and t == "F" and i == "J":
#         print("▷ INFJ_예언자형 : 사람에 관한 뛰어난 통찰력을 가진 사람\n▷ 나와 가장 잘 맞는 MBTI는? : ESTP\n▷ 나와 가장 잘 안맞는 MBTI는? : ESTJ")
#     elif m == "I" and b == "N" and t == "F" and i == "P":
#         print("▷ INFP_잔다르크형 : 이상적인 세상을 만들어가는 사람들\n▷ 나와 가장 잘 맞는 MBTI는? : ESTJ\n▷ 나와 가장 잘 안맞는 MBTI는? : ESTP")
#     elif m == "E" and b == "S" and t == "T" and i == "P":
#         print("▷ ESTP_활동가형 : 친구, 운동, 음식 등 다양함을 선호\n▷ 나와 가장 잘 맞는 MBTI는? : INFJ\n▷ 나와 가장 잘 안맞는 MBTI는? : INFP")
#     elif m == "E" and b == "S" and t == "F" and i == "P":
#         print("▷ ESFP_사교형 : 분위기를 고조시키는 우호적인 성격\n▷ 나와 가장 잘 맞는 MBTI는? : INTJ\n▷ 나와 가장 잘 안맞는 MBTI는? : INTP")
#     elif m == "I" and b == "S" and t == "T" and i == "P":
#         print("▷ ISTP_백과사전형 : 논리적이고 뛰어난 상황 적응력\n▷ 나와 가장 잘 맞는 MBTI는? : ENFJ\n▷ 나와 가장 잘 안맞는 MBTI는? : ENFP")
#     elif m == "I" and b == "S" and t == "F" and i == "P":
#         print("▷ ISFP_성인군자형 : 따뜻한 감성을 가지고 있는 겸손한 사람\n▷ 나와 가장 잘 맞는 MBTI는? : ENTJ\n▷ 나와 가장 잘 안맞는 MBTI는? : ENTP")


def main():
    app = tkinterApp()
    app.mainloop()


if __name__ == "__main__":
    main()