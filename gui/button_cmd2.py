from tkinter import *

def click():
    en_text = entry.get()
    print(en_text + "님 환영합니다.")


root = Tk()
root.title("Hello~")
root.geometry("200x70+200+200")

frame = Frame(root)
frame.pack()

Label(frame, text="이름 : ").grid(row=0, column=0)
entry = Entry(frame, width=10)
entry.grid(row=0, column=1)
Button(frame, text="확인", command=click).grid(row=1, columnspan=2)
#def click ()생략한 이유는 버튼 누를때만 함수 작동, ()있으면 함수 생성시점에서 동작
#columnspan 2행 합침



root.mainloop()