from tkinter import * 
from tkinter.filedialog import *

def func_open() :
  filename = askopenfilename(parent= window, 
                           filetypes=(("GIF 파일","*.gif"),("모든파일","*.*")))
  photo = PhotoImage(file= filename)

#   print("photo.width(): ",str(photo.width()),"photo.height() : ", str(photo.height()))
#   print("0,0 있니? ", str(photo.get(359,479)))
  
  for i in range(0,photo.width()):
    for k in range(0,photo.height()):
      color = photo.get(i,k)
      colorList = list(color)
      for j in range(0,3) :
        colorList[j] = int((colorList[0] + colorList[1] + colorList[2]) / 3)
      colorTuple = tuple(colorList)
    #   print(colorTuple)
      photo.put("#%02x%02x%02x" % colorTuple,(i,k))

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
