
# 기본 창

# from tkinter import *

# window = Tk() 

# # 옵션 값 추가 
# window.title("윈도우창 연습")
# window.geometry("400x100")
# window.resizable(width = TRUE, height = TRUE)

# window.mainloop()



# 텍스트 뷰 라벨

# from tkinter import * 
# window = Tk() 

# window.title("윈도우창 연습")
# window.geometry("400x100")
# window.resizable(width = TRUE, height = TRUE)
# label1 = Label(window, text = "COOKBOOK, 데이터 분석을")
# label2 = Label(window, text = "열심히", font=("궁서체",30),fg="blue", bg="white")
# label3 = Label(window, text = "공부 중입니다.", bg="magenta", \
#   width=20, height=5, anchor=NW)

# label1.pack()
# label2.pack()
# label3.pack()

# window.mainloop()



#이미지

# from tkinter import *

# window = Tk()

# # .jpg 못 읽음. 
# photo1 = PhotoImage(file="sample_img/childLook.gif")
# photo2 = PhotoImage(file="sample_img/라바1.png")
# # photo3 = PhotoImage(file="sample_img/cherries.jpg")
# label1 = Label(window, image=photo1)
# label2 = Label(window, image=photo2)
# # label3 = Label(window, image=photo3)

# label1.pack(side=LEFT)
# label2.pack()
# # label3.pack()

# window.mainloop()


# 버튼

# from tkinter import * 
# window = Tk()

# button1 = Button(window, text="종료", fg="red", command=quit)

# button1.pack()

# window.mainloop()



# 버튼 이미지 ,

# from tkinter import * 
# from tkinter import messagebox


# def myFunc() :
#   messagebox.showinfo("창 잘 뜨나요?","잘 뜨는 군")
  
# window = Tk()

# photo = PhotoImage(file="sample_img/라바1.png")
# button1 = Button(window, image=photo, command=myFunc)

# button1.pack()

# window.mainloop()


# from tkinter import * 
# from tkinter import messagebox

# window = Tk()

# def myFunc() :
#   if chk.get() == 0:
#     messagebox.showinfo("","체크버튼이 꺼졌어요: "+str(chk.get()))
#   else :
#     messagebox.showinfo("","체크버튼이 켜졌어요: "+ str(chk.get()))

# chk = IntVar()
# cb1 = Checkbutton(window,text = "클릭하세요",variable = chk, 
#                   command =myFunc)

# cb1.pack()

# window.mainloop()
  
# from tkinter import *
# from tkinter import messagebox
# window = Tk()
# window.geometry("400x100")
# window.resizable(width = TRUE, height = TRUE)
# photo2 = PhotoImage(file="sample_img/라바1.png")

# def myFunc() :
#   if var.get() == 1:
#     label1.configure(text = "파이썬")
#   elif var.get() == 2:
#     label1.configure(text = "C++")
#   else :
#     label1.configure(text="Java")

# var = IntVar()
# rb1 = Radiobutton(window, text="파이썬",
#                   variable=var, value=1,command=myFunc)
# rb2 = Radiobutton(window, text="C++",
#                   variable=var, value=2,command=myFunc)
# rb3 = Radiobutton(window, text="Java",
#                   variable=var, value=3,command=myFunc)

    
# label1 = Label(window,text="선택한 언어 : ", fg ="red")

# rb1.pack()
# rb2.pack()
# rb3.pack()
# label1.pack()

# window.mainloop()

# from tkinter import *
# window = Tk()

# button1 = Button(window, text="버튼1")
# button2 = Button(window, text="버튼2")
# button3 = Button(window, text="버튼3")

# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)

# window.mainloop()


# from tkinter import * 
# window = Tk() 

# btnList = [None] * 3 

# for i in range(0,3) :
#   btnList[i] = Button(window, text="버튼" + str(i+1))
  
# for btn in btnList :
#   btn.pack(side = TOP,fill = X, padx = 10, pady = 10 ,ipadx = 10, ipady = 10)
  
# window.mainloop() 

# ====================
# from tkinter import * 
# window = Tk() 


# window.mainloop() 
# ====================

# 맥북에서 안보임.

# from tkinter import * 

# window = Tk() 
# mainMenu = Menu(window)
# window.config(menu=mainMenu)
# fileMenu = Menu(mainMenu)

# mainMenu.add_cascade(label="파일", menu = fileMenu)
# fileMenu.add_command(label="열기")
# fileMenu.add_separator()
# fileMenu.add_command(label="종료")

# window.mainloop()


# from tkinter import * 
# from tkinter import messagebox

# def func_open() :
#   messagebox.showinfo("메뉴 선택","열기 메뉴를 선택함")
  
# def func_exit() :
#   window.quit()
#   window.destroy()

# window = Tk() 

# mainMenu = Menu(window)
# window.config(menu=mainMenu)

# fileMenu = Menu(mainMenu)
# mainMenu.add_cascade(label="파일", menu = fileMenu)
# fileMenu.add_command(label="열기", command= func_open)
# fileMenu.add_separator()
# fileMenu.add_command(label="종료", command=func_exit)

# window.mainloop()

# from tkinter import * 
# from tkinter.simpledialog import *

# window = Tk() 
# window.geometry("400x100")

# label1 = Label(window, text="입력된 값")
# label1.pack()

# value = askinteger("확대배수","주사위 1~6 입력.", minvalue=1, maxvalue=6)

# label1.configure(text=str(value))
# window.mainloop()


# from tkinter import * 
# from tkinter.filedialog import *

# window = Tk() 
# window.geometry("400x100")

# label1 = Label(window, text="선택된 파일 이름")
# label1.pack()

# filename = askopenfilename(parent= window, 
#                            filetypes=(("GIF 파일","*.gif"),("모든파일","*.*")))



# label1.configure(text=str(filename))
# window.mainloop()



# from tkinter import * 
# from tkinter.filedialog import *

# window = Tk() 
# window.geometry("400x100")

# label1 = Label(window, text="선택된 파일 이름")
# label1.pack()

# saveFp = asksaveasfile(parent=window, mode="w",
#                        defaultextension=".jpg",
#                        filetypes=(("JPG 파일","*.jpg"),("모든 파일","*.*")))

# label1.configure(text=str(saveFp))
# window.mainloop()
# saveFp.close()


from tkinter import * 
from tkinter.filedialog import *

def func_open() :
  filename = askopenfilename(parent= window, 
                           filetypes=(("GIF 파일","*.gif"),("모든파일","*.*")))
  photo = PhotoImage(file= filename)
  
  print("photo.width(): ",str(photo.width()),"photo.height() : ", str(photo.height()))
  # print("0,0 있니? ", str(photo.get(0,0)))
  for i in range(0,photo.width()):
    for k in range(0,photo.height()):
     color = photo.get(i,k) / 3
     photo.put("#%02x%02x%02x" % color,(i,k))
      
  
  pLabel.configure(image = photo)
  pLabel.image = photo

def func_exit() :
  window.quit()
  window.destroy()


window = Tk() 
window.geometry("400x500")
window.title("사진 감상")

photo = PhotoImage()
pLabel = Label(window, image= photo)
pLabel.pack(expand=1, anchor= CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu = fileMenu)
fileMenu.add_command(label="열기", command= func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()
