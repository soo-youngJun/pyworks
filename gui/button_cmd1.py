from tkinter import *

def click():
    print("Hello~ Python!!")


root = Tk()
root.title("Hello~")

frame = Frame(root)
frame.pack()

Button(frame, text="확인", command=click).grid(row=0, column=0)
#def click ()생략한 이유는 버튼 누를때만 함수 작동, ()있으면 함수 생성시점에서 동작



root.mainloop()