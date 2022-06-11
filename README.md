# MBTI test with PYTHON
프로그래밍 원리와 실습 기말 과제
각 항마다 3개로 구성된 총 12개의 양자택일형 문제를 통해 각 지표를 결정, 최종 mbti 결과와 그 특성을 출력하는 것이 목표이다.
## 코드 설명
### radiobutton 위젯 사용
```c
 self.q1 = IntVar()
 self.r1 = Radiobutton(self.top, text="1. 나는 새로운 사람을 만나도 어색하지 않다.", variable=self.q1, value=1)
 self.r1.grid(row=1, column=1)
```
각 질문당 한개의 value를 설정하고, 두 문항중 결정된 하나의 value를 variable값으로 설정한다.

### MBTI 결정하기
```c
E = 0
I = 0
mbti_text = ''
a1 = q1.get()

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
```      
radiobutton 위젯에서 결정된 value값을 통해 3개중 다수의 항목을 결정, mbti_text 값에 넣은 후 출력한다.    

### MBTI 부연설명 출력하기
```c
explain=''

 if mbti_text == "ESTJ":
      explain += "▷ 사업가형: 사무적, 실용적, 현실적인 스타일 \n▷ 나와 가장 잘 맞는 MBTI는?: INFP \n▷ 나와 가장 잘 안맞는 MBTI는?: INFJ"
```           
결정된 mbti와 같은 설명문을 찾은 후, explain 값에 넣은 후 출력한다.
