# MBTI test with PYTHON
프로그래밍 원리와 실습 기말 과제
각 항마다 3개로 구성된, 총 12개의 양자택일형 문제를 통해 각 지표를 결정. 최종 mbti 결과와, 그 특성을 출력하는 것이 목표이다.
## 코드 설명
radiobutton 위젯 사용
```c
 self.q1 = IntVar()
        self.r1 = Radiobutton(self.top, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", variable=self.q1, value=1)
        self.r1.grid(row=1, column=1)
```
