from tkinter import *

class mbti():
    def results(self):
        self.result = Label(text=self.answer(self.q1, self.q2, self.q3, self.q4, self.q5,
                                             self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12))
        self.result.grid(row=26)

    def __init__(self):
        self.top = Tk()

        self.lb = Label(text="mbti 테스트")
        self.lb.grid(row=0)

        # 1)-----------------------------------------------------------------------------------

        self.lb1 = Label(text="1번 질문")
        self.lb1.grid(row=1, column=0)

        self.q1 = IntVar()
        self.r1 = Radiobutton(self.top, text="1.VPD", variable=self.q1, value=1)
        self.r1.grid(row=1, column=1)

        self.r2 = Radiobutton(self.top, text="2.DLI", variable=self.q1, value=2)
        self.r2.grid(row=2, column=1)

        # 2)-----------------------------------------------------------------------------------

        self.lb2 = Label(text="2번 질문")
        self.lb2.grid(row=3, column=0)

        self.q2 = IntVar()
        self.r3 = Radiobutton(self.top, text="3.GDD", variable=self.q2, value=3)
        self.r3.grid(row=3, column=1)

        self.r4 = Radiobutton(self.top, text="3.GDD", variable=self.q2, value=4)
        self.r4.grid(row=4, column=1)

        # 3)-----------------------------------------------------------------------------------

        self.lb3 = Label(text="3번 질문")
        self.lb3.grid(row=5, column=0)

        self.q3 = IntVar()
        self.r5 = Radiobutton(self.top, text="3.GDD", variable=self.q3, value=5)
        self.r5.grid(row=5, column=1)

        self.r6 = Radiobutton(self.top, text="3.GDD", variable=self.q3, value=6)
        self.r6.grid(row=6, column=1)

        # 4)-----------------------------------------------------------------------------------

        self.lb4 = Label(text="4번 질문")
        self.lb4.grid(row=7, column=0)

        self.q4 = IntVar()
        self.r7 = Radiobutton(self.top, text="3.GDD", variable=self.q4, value=7)
        self.r7.grid(row=7, column=1)

        self.r8 = Radiobutton(self.top, text="3.GDD", variable=self.q4, value=8)
        self.r8.grid(row=8, column=1)

        # 5)-----------------------------------------------------------------------------------

        self.lb5 = Label(text="5번 질문")
        self.lb5.grid(row=9, column=0)

        self.q5 = IntVar()
        self.r9 = Radiobutton(self.top, text="3.GDD", variable=self.q5, value=9)
        self.r9.grid(row=9, column=1)

        self.r10 = Radiobutton(self.top, text="3.GDD", variable=self.q5, value=10)
        self.r10.grid(row=10, column=1)

        # 6)-----------------------------------------------------------------------------------

        self.lb6 = Label(text="6번 질문")
        self.lb6.grid(row=11, column=0)

        self.q6 = IntVar()
        self.r11 = Radiobutton(self.top, text="3.GDD", variable=self.q6, value=11)
        self.r11.grid(row=11, column=1)

        self.r12 = Radiobutton(self.top, text="3.GDD", variable=self.q6, value=12)
        self.r12.grid(row=12, column=1)

        # 7)-----------------------------------------------------------------------------------

        self.lb7 = Label(text="7번 질문")
        self.lb7.grid(row=13, column=0)

        self.q7 = IntVar()
        self.r13 = Radiobutton(self.top, text="1.VPD", variable=self.q7, value=13)
        self.r13.grid(row=13, column=1)

        self.r14 = Radiobutton(self.top, text="2.DLI", variable=self.q7, value=14)
        self.r14.grid(row=14, column=1)

        # 8)-----------------------------------------------------------------------------------

        self.lb8 = Label(text="8번 질문")
        self.lb8.grid(row=15, column=0)

        self.q8 = IntVar()
        self.r15 = Radiobutton(self.top, text="3.GDD", variable=self.q8, value=15)
        self.r15.grid(row=15, column=1)

        self.r16 = Radiobutton(self.top, text="3.GDD", variable=self.q8, value=16)
        self.r16.grid(row=16, column=1)

        # 9)-----------------------------------------------------------------------------------

        self.lb9 = Label(text="9번 질문")
        self.lb9.grid(row=17, column=0)

        self.q9 = IntVar()
        self.r17 = Radiobutton(self.top, text="3.GDD", variable=self.q9, value=17)
        self.r17.grid(row=17, column=1)

        self.r18 = Radiobutton(self.top, text="3.GDD", variable=self.q9, value=18)
        self.r18.grid(row=18, column=1)

        # 10)-----------------------------------------------------------------------------------

        self.lb10 = Label(text="10번 질문")
        self.lb10.grid(row=19, column=0)

        self.q10 = IntVar()
        self.r19 = Radiobutton(self.top, text="3.GDD", variable=self.q10, value=19)
        self.r19.grid(row=19, column=1)

        self.r20 = Radiobutton(self.top, text="3.GDD", variable=self.q10, value=20)
        self.r20.grid(row=20, column=1)

        # 11)-----------------------------------------------------------------------------------

        self.lb11 = Label(text="11번 질문")
        self.lb11.grid(row=21, column=0)

        self.q11 = IntVar()
        self.r21 = Radiobutton(self.top, text="3.GDD", variable=self.q11, value=21)
        self.r21.grid(row=21, column=1)

        self.r22 = Radiobutton(self.top, text="3.GDD", variable=self.q11, value=22)
        self.r22.grid(row=22, column=1)

        # 12)-----------------------------------------------------------------------------------

        self.lb12 = Label(text="12번 질문")
        self.lb12.grid(row=23, column=0)

        self.q12 = IntVar()
        self.r23 = Radiobutton(self.top, text="3.GDD", variable=self.q12, value=23)
        self.r23.grid(row=23, column=1)

        self.r24 = Radiobutton(self.top, text="3.GDD", variable=self.q12, value=24)
        self.r24.grid(row=24, column=1)

        self.result_btn = Button(self.top, text="결과 보기", command=self.results)
        self.result_btn.grid(row=25, column=1)

        self.result = Label(text='')
        self.result.grid(row=26)

        self.explain = Label(text='')
        self.explain.grid(row=26)

    def answer(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12) -> str:
        E = 0
        I = 0
        N = 0
        S = 0
        F = 0
        T = 0
        P = 0
        J = 0

        mbti_text = ""

        a1 = q1.get()
        a2 = q2.get()
        a3 = q3.get()
        a4 = q4.get()
        a5 = q5.get()
        a6 = q6.get()
        a7 = q7.get()
        a8 = q8.get()
        a9 = q9.get()
        a10 = q10.get()
        a11 = q11.get()
        a12 = q12.get()

        if a1 == 1:
            E += 1
        elif a1 == 2:
            I += 1

        if a2 == 3:
            E += 1
        elif a2 == 4:
            I += 1

        if a3 == 5:
            E += 1
        elif a3 == 6:
            I += 1

        if E >= 2:
            mbti_text += "E"
        elif I >= 2:
            mbti_text += "I"

        if a4 == 7:
            N += 1
        elif a4 == 8:
            S += 1

        if a5 == 9:
            N += 1
        elif a5 == 10:
            S += 1

        if a6 == 11:
            N += 1
        elif a6 == 12:
            S += 1

        if N >= 2:
            mbti_text += "N"
        elif S >= 2:
            mbti_text += "S"

        if a7 == 13:
            F += 1
        elif a7 == 14:
            T += 1

        if a8 == 15:
            F += 1
        elif a8 == 16:
            T += 1

        if a9 == 17:
            F += 1
        elif a9 == 18:
            T += 1

        if F >= 2:
            mbti_text += "F"
        elif T >= 2:
            mbti_text += "T"

        if a10 == 19:
            P += 1
        elif a10 == 20:
            J += 1

        if a11 == 21:
            P += 1
        elif a11 == 22:
            J += 1

        if a12 == 23:
            P += 1
        elif a12 == 24:
            J += 1

        if P >= 2:
            mbti_text += "P"
        elif J >= 2:
            mbti_text += "J"

        return mbti_text

    def mbti_explain(self, mbti_text):
        explain = ""
        if mbti_text == "ESTJ":
            explain += "사업가형: 사무적, 실용적, 현실적인 스타일 ▷ 나와 가장 잘 맞는 MBTI는?: INFP ▷ 나와 가장 잘 안맞는 MBTI는?: INFJ"

        return explain

    def show(self):
        self.top.mainloop()


def main():
    MBTI = mbti()
    MBTI.show()


if __name__ == '__main__':
    main()

