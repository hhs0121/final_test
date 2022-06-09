from tkinter import *


class Mbti:
    LARGEFONT = ("Gulim", 20)

    def results(self):
        self.result = Label(text=self.answer(self.q1, self.q2, self.q3, self.q4, self.q5,
                                             self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12),
                            font=self.LARGEFONT)
        self.result.grid(row=38, column=1)

        self.explain = Label(text=self.mbti_explain(self.mbti_text))
        self.explain.grid(row=39, column=1)

    def __init__(self):
        self.top = Tk()

        self.lb = Label(text="MBTI test with PYTHON", font=self.LARGEFONT)
        self.lb.grid(row=0, column=1)

        # 1)-----------------------------------------------------------------------------------

        self.lb1 = Label(text="1번 질문")
        self.lb1.grid(row=1, column=0)

        self.q1 = IntVar()
        self.r1 = Radiobutton(self.top, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", variable=self.q1, value=1)
        self.r1.grid(row=1, column=1)

        self.r2 = Radiobutton(self.top, text="2. 나는 모르는 사람을 만나는 일이 곤하다.", variable=self.q1, value=2)
        self.r2.grid(row=2, column=1)

        self.line1 = Label(text="-----------------------------------------------------------------------------------")
        self.line1.grid(row=3, column=1)

        # 2)-----------------------------------------------------------------------------------

        self.lb2 = Label(text="2번 질문")
        self.lb2.grid(row=4, column=0)

        self.q2 = IntVar()
        self.r3 = Radiobutton(self.top, text="1. 나는 말하면서 생각하고 대화도중 결심할 때가 있다.", variable=self.q2, value=3)
        self.r3.grid(row=4, column=1)

        self.r4 = Radiobutton(self.top, text="2. 나는 의견을 말하기에 앞서 신중히 생각하는 편이다.", variable=self.q2, value=4)
        self.r4.grid(row=5, column=1)

        self.line2 = Label(text="-----------------------------------------------------------------------------------")
        self.line2.grid(row=6, column=1)

        # 3)-----------------------------------------------------------------------------------

        self.lb3 = Label(text="3번 질문")
        self.lb3.grid(row=7, column=0)

        self.q3 = IntVar()
        self.r5 = Radiobutton(self.top, text="1. 일할때 적막한 것 보다는 어느정도의 소리가 도움이 된다.", variable=self.q3, value=5)
        self.r5.grid(row=7, column=1)

        self.r6 = Radiobutton(self.top, text="2. 나는 소음이 있는 곳에서 일을 할 때 일하기가 힘들다.", variable=self.q3, value=6)
        self.r6.grid(row=8, column=1)

        self.line3 = Label(text="-----------------------------------------------------------------------------------")
        self.line3.grid(row=9, column=1)

        # 4)-----------------------------------------------------------------------------------

        self.lb4 = Label(text="4번 질문")
        self.lb4.grid(row=10, column=0)

        self.q4 = IntVar()
        self.r7 = Radiobutton(self.top, text="1. 나는 경험으로 판단한다.", variable=self.q4, value=7)
        self.r7.grid(row=10, column=1)

        self.r8 = Radiobutton(self.top, text="2. 나는 떠오르는 직관으로 판단한다.", variable=self.q4, value=8)
        self.r8.grid(row=11, column=1)

        self.line4 = Label(text="-----------------------------------------------------------------------------------")
        self.line4.grid(row=12, column=1)

        # 5)-----------------------------------------------------------------------------------

        self.lb5 = Label(text="5번 질문")
        self.lb5.grid(row=13, column=0)

        self.q5 = IntVar()
        self.r9 = Radiobutton(self.top, text="1. 나는 약도를 구체적으로 그린다.", variable=self.q5, value=9)
        self.r9.grid(row=13, column=1)

        self.r10 = Radiobutton(self.top, text="2. 나는 약도를 구체적으로 그리기 어렵다.", variable=self.q5, value=10)
        self.r10.grid(row=14, column=1)

        self.line5 = Label(text="-----------------------------------------------------------------------------------")
        self.line5.grid(row=15, column=1)

        # 6)-----------------------------------------------------------------------------------

        self.lb6 = Label(text="6번 질문")
        self.lb6.grid(row=16, column=0)

        self.q6 = IntVar()
        self.r11 = Radiobutton(self.top, text="1. 나는 늘 다니던 길로 다니는 것이 좋다.", variable=self.q6, value=11)
        self.r11.grid(row=16, column=1)

        self.r12 = Radiobutton(self.top, text="2. 나는 한번도 안가본 새로운 길로 다니는 것을 좋아한다.", variable=self.q6, value=12)
        self.r12.grid(row=17, column=1)

        self.line6 = Label(text="-----------------------------------------------------------------------------------")
        self.line6.grid(row=18, column=1)

        # 7)-----------------------------------------------------------------------------------

        self.lb7 = Label(text="7번 질문")
        self.lb7.grid(row=19, column=0)

        self.q7 = IntVar()
        self.r13 = Radiobutton(self.top, text="1. 나는 슬픈영화를 볼때 쉽게 감정이입이 되지 않는다.", variable=self.q7, value=13)
        self.r13.grid(row=19, column=1)

        self.r14 = Radiobutton(self.top, text="2. 나는 슬픈영화를 볼때 심하게 감정이입을 해서 쉽게 눈물이 난다.", variable=self.q7, value=14)
        self.r14.grid(row=20, column=1)

        self.line7 = Label(text="-----------------------------------------------------------------------------------")
        self.line7.grid(row=21, column=1)

        # 8)-----------------------------------------------------------------------------------

        self.lb8 = Label(text="8번 질문")
        self.lb8.grid(row=22, column=0)

        self.q8 = IntVar()
        self.r15 = Radiobutton(self.top, text="1. 나는 능력있다는 소리를 듣기 좋아한다.", variable=self.q8, value=15)
        self.r15.grid(row=22, column=1)

        self.r16 = Radiobutton(self.top, text="2. 나는 따뜻한 마음을 가졌다는 소리를 듣기 좋아한다.", variable=self.q8, value=16)
        self.r16.grid(row=23, column=1)

        self.line8 = Label(text="-----------------------------------------------------------------------------------")
        self.line8.grid(row=24, column=1)

        # 9)-----------------------------------------------------------------------------------

        self.lb9 = Label(text="9번 질문")
        self.lb9.grid(row=25, column=0)

        self.q9 = IntVar()
        self.r17 = Radiobutton(self.top, text="1. 나는 옳고 그름이 확실해서 직선적으로 말하는 편이다.", variable=self.q9, value=17)
        self.r17.grid(row=25, column=1)

        self.r18 = Radiobutton(self.top, text="2. 나는 주로 남을 배려하는 말을 하는 편이다.", variable=self.q9, value=18)
        self.r18.grid(row=26, column=1)

        self.line9 = Label(text="-----------------------------------------------------------------------------------")
        self.line9.grid(row=27, column=1)

        # 10)-----------------------------------------------------------------------------------

        self.lb10 = Label(text="10번 질문")
        self.lb10.grid(row=28, column=0)

        self.q10 = IntVar()
        self.r19 = Radiobutton(self.top, text="1. 나는 계획에 의해 일을 처리하는 편이다.", variable=self.q10, value=19)
        self.r19.grid(row=28, column=1)

        self.r20 = Radiobutton(self.top, text="2. 나는 마지막에 임박했을때 일을 처리하는 편이다.", variable=self.q10, value=20)
        self.r20.grid(row=29, column=1)

        self.line10 = Label(text="-----------------------------------------------------------------------------------")
        self.line10.grid(row=30, column=1)

        # 11)-----------------------------------------------------------------------------------

        self.lb11 = Label(text="11번 질문")
        self.lb11.grid(row=31, column=0)

        self.q11 = IntVar()
        self.r21 = Radiobutton(self.top, text="1. 나는 평소에 정리정돈을 자주 하는 편이다.", variable=self.q11, value=21)
        self.r21.grid(row=31, column=1)

        self.r22 = Radiobutton(self.top, text="2. 나는 날을 잡아서 한번에 몰아서 정리하는 편이다.", variable=self.q11, value=22)
        self.r22.grid(row=32, column=1)

        self.line11 = Label(text="-----------------------------------------------------------------------------------")
        self.line11.grid(row=33, column=1)

        # 12)-----------------------------------------------------------------------------------

        self.lb12 = Label(text="12번 질문")
        self.lb12.grid(row=34, column=0)

        self.q12 = IntVar()
        self.r23 = Radiobutton(self.top, text="1. 나는 일을 할 때 사람들과 친해지는 편이다.", variable=self.q12, value=23)
        self.r23.grid(row=34, column=1)

        self.r24 = Radiobutton(self.top, text="2. 나는 놀면서 사람들과 친해지는 편이다.", variable=self.q12, value=24)
        self.r24.grid(row=35, column=1)

        self.blank = Label(text="")
        self.blank.grid(row=36)

        self.result_btn = Button(self.top, text="결과 보기", command=self.results)
        self.result_btn.grid(row=37, column=1)

        self.result = Label(text='')
        self.result.grid(row=38)

        self.explain = Label(text='')
        self.explain.grid(row=39)

    def answer(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12) -> str:
        E = 0
        I = 0
        N = 0
        S = 0
        F = 0
        T = 0
        P = 0
        J = 0

        self.mbti_text = ""

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
            self.mbti_text += "E"
        elif I >= 2:
            self.mbti_text += "I"

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
            self.mbti_text += "N"
        elif S >= 2:
            self.mbti_text += "S"

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
            self.mbti_text += "F"
        elif T >= 2:
            self.mbti_text += "T"

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
            self.mbti_text += "P"
        elif J >= 2:
            self.mbti_text += "J"

        return self.mbti_text

    def mbti_explain(self, mbti_text):
        explain = ""

        if mbti_text == "ESTJ":
            explain += "▷ 사업가형: 사무적, 실용적, 현실적인 스타일 \n▷ 나와 가장 잘 맞는 MBTI는?: INFP \n▷ 나와 가장 잘 안맞는 MBTI는?: INFJ"
        elif mbti_text == "ENFP":
            explain += "▷ 스파크형 : 열정적으로 새 관계를 만드는 사람 \n▷ 나와 가장 잘 맞는 MBTI는? : ISTJ \n▷ 나와 가장 잘 안맞는 MBTI는? : ISTP"
        elif mbti_text == "ENTJ":
            explain += "▷ 지도자형 : 비전을 갖고 타인을 활력적으로 인도 \n▷ 나와 가장 잘 맞는 MBTI는? : ISFP \n▷ 나와 가장 잘 안맞는 MBTI는? : ISFJ"
        elif mbti_text == "ENTP":
            explain += "▷ 발명가형 : 풍부한 상상력으로 새로운 것에 도전 \n▷ 나와 가장 잘 맞는 MBTI는? : ISFJ \n▷ 나와 가장 잘 안맞는 MBTI는? : ISFP"
        elif mbti_text == "INTJ":
            explain += "▷ 과학자형 : 전체를 조합하여 비전을 제시하는 사람 \n▷ 나와 가장 잘 맞는 MBTI는? : ESFP \n▷ 나와 가장 잘 안맞는 MBTI는? : ESFJ"
        elif mbti_text == "INTP":
            explain += "▷ 아이디어형 : 비평적인 관점을 가진 뛰어난 전략가 \n▷ 나와 가장 잘 맞는 MBTI는? : ESFJ \n▷ 나와 가장 잘 안맞는 MBTI는? : ESFP"
        elif mbti_text == "ESFJ":
            explain += "▷ 친선도모형 : 친절, 현실감을 바탕으로 타인에게 봉사 \n▷ 나와 가장 잘 맞는 MBTI는? : INTP \n▷ 나와 가장 잘 안맞는 MBTI는? : INTJ"
        elif mbti_text == "ISTJ":
            explain += "▷ 소금형 : 한번 시작한 일은 끝까지 해내는 성격 \n▷ 나와 가장 잘 맞는 MBTI는? : ENFP \n▷ 나와 가장 잘 안맞는 MBTI는? : ENFJ"
        elif mbti_text == "ISFJ":
            explain += "▷ 권력형 : 성실하고 온화하며 협조를 잘하는 사람 \n▷ 나와 가장 잘 맞는 MBTI는? : ENTP \n▷ 나와 가장 잘 안맞는 MBTI는? : ENTJ"
        elif mbti_text == "ENFJ":
            explain += "▷ 언변능숙형 : 타인의 성장을 도모하고 협동하는 사람 \n▷ 나와 가장 잘 맞는 MBTI는? : ISTP \n▷ 나와 가장 잘 안맞는 MBTI는? : ISTJ"
        elif mbti_text == "INFJ":
            explain += "▷ 예언자형 : 사람에 관한 뛰어난 통찰력을 가진 사람 \n▷ 나와 가장 잘 맞는 MBTI는? : ESTP \n▷ 나와 가장 잘 안맞는 MBTI는? : ESTJ"
        elif mbti_text == "INFP":
            explain += "▷ 잔다르크형 : 이상적인 세상을 만들어가는 사람들 \n▷ 나와 가장 잘 맞는 MBTI는? : ESTJ \n▷ 나와 가장 잘 안맞는 MBTI는? : ESTP"
        elif mbti_text == "ESTP":
            explain += "▷ 활동가형 : 친구, 운동, 음식 등 다양함을 선호 \n▷ 나와 가장 잘 맞는 MBTI는? : INFJ \n▷ 나와 가장 잘 안맞는 MBTI는? : INFP"
        elif mbti_text == "ISTP":
            explain += "▷ 백과사전형 : 논리적이고 뛰어난 상황 적응력 \n▷ 나와 가장 잘 맞는 MBTI는? : ENFJ \n▷ 나와 가장 잘 안맞는 MBTI는? : ENFP"
        elif mbti_text == "ISFP":
            explain += "▷ 성인군자형 : 따뜻한 감성을 가지고 있는 겸손한 사람 \n▷ 나와 가장 잘 맞는 MBTI는? : ENTJ \n▷ 나와 가장 잘 안맞는 MBTI는? : ENTP"
        elif mbti_text == "ESFP":
            explain += "▷ 사교형 : 분위기를 고조시키는 우호적인 성격 \n▷ 나와 가장 잘 맞는 MBTI는? : INTJ \n▷ 나와 가장 잘 안맞는 MBTI는? : INTP"

        return explain

    def show(self):
        self.top.mainloop()


def main():
    mbti = Mbti()
    mbti.show()


if __name__ == '__main__':
    main()

