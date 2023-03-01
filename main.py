import PIL
from PIL import Image, ImageTk
import pytesseract
import cv2 as cv2
import tkinter as tk
from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk
from socket import *

# Create the window and camera
width, height = 1920, 1080  # 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
root = Tk()
root.geometry("1920x1080")  # adc isso
root.attributes("-fullscreen", True)
root['bg'] = '#1f1f1f'  ##1f1f1f
# root.attributes('-alpha',0.5) deixa transpartente
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()

# Cria a aba dos botões
canvas = tk.Canvas(root, width=900, height=100, background="#1f1f1f", highlightbackground="#1f1f1f",
                   highlightcolor="#1f1f1f")
canvas.pack()

# O círculo que compõe o botão de movimento
#bgImage = ImageTk.PhotoImage(Image.open("fundomovimento.png"))
#bg = canvas.create_image(50, 5, image=bgImage, anchor=tk.NW)  # 5,5


# As funções dos botões
###########################
def sairtelacheia(event):
    root.attributes("-fullscreen", False)


def entrartelacheia(event):
    root.attributes("-fullscreen", True)

###########################

def quitGame(event):
    root.destroy()


def btn(event):
    print("neutro")



def btf(event):
    print("feliz")



def bts(event):
    print("surpreso")



def btd(event):
    print("duvida")



def btt(event):
    print("triste")


def btm(event):
    print('Mutar mic')


def btc(event):
    print('Desligar câmera')


def bt(event):
    print('Apertado')


def btww(event):
    print('Frente')


def btss(event):
    print('trás')


def btdd(event):
    print('direita')


def btaa(event):
    print('esquerda')


# Os botões
telaImage = ImageTk.PhotoImage(Image.open("t1.png"))
telaButton = canvas.create_image(220, 25, image=telaImage)
canvas.tag_bind(telaButton, "<Button-1>", entrartelacheia)

tela2Image = ImageTk.PhotoImage(Image.open("t2.png"))
tela2Button = canvas.create_image(320, 25, image=tela2Image)
canvas.tag_bind(tela2Button, "<Button-1>", sairtelacheia)

micImage = ImageTk.PhotoImage(Image.open("mic.png"))
Button3 = canvas.create_image(520, 25, image=micImage)
canvas.tag_bind(Button3, "<Button-1>", btm)

telefoneImage = ImageTk.PhotoImage(Image.open("telefone.png"))
telButton = canvas.create_image(420, 25, image=telefoneImage)
canvas.tag_bind(telButton, "<Button-1>", quitGame)

camImage = ImageTk.PhotoImage(Image.open("cam.png"))
camButton = canvas.create_image(620, 25, image=camImage)
canvas.tag_bind(camButton, "<Button-1>", btc)

neutroImage = ImageTk.PhotoImage(Image.open("neutro.png"))
b5 = canvas.create_image(220, 75, image=neutroImage)
canvas.tag_bind(b5, "<Button-1>", btn)

felizImage = ImageTk.PhotoImage(Image.open("feliz.png"))
b6 = canvas.create_image(320, 75, image=felizImage)
canvas.tag_bind(b6, "<Button-1>", btf)

surpresoImage = ImageTk.PhotoImage(Image.open("surpreso.png"))
b7 = canvas.create_image(420, 75, image=surpresoImage)
canvas.tag_bind(b7, "<Button-1>", bts)

duvidaImage = ImageTk.PhotoImage(Image.open("duvida.png"))
b8 = canvas.create_image(520, 75, image=duvidaImage)
canvas.tag_bind(b8, "<Button-1>", btd)

tristeImage = ImageTk.PhotoImage(Image.open("triste.png"))
b8 = canvas.create_image(620, 75, image=tristeImage)
canvas.tag_bind(b8, "<Button-1>", btt)

m1Image = ImageTk.PhotoImage(Image.open("m1.png"))
m1 = canvas.create_image(94, 25, image=m1Image)
canvas.tag_bind(m1, "<Button-1>", btww)

m2Image = ImageTk.PhotoImage(Image.open("m2.png"))
m2 = canvas.create_image(94, 78, image=m2Image)
canvas.tag_bind(m2, "<Button-1>", btss)

m3Image = ImageTk.PhotoImage(Image.open("m3.png"))
m3 = canvas.create_image(63, 50, image=m3Image)
canvas.tag_bind(m3, "<Button-1>", btaa)

m4Image = ImageTk.PhotoImage(Image.open("m4.png"))
m4 = canvas.create_image(125, 50, image=m4Image)
canvas.tag_bind(m4, "<Button-1>", btdd)


# A barra de giro
def print_value(val):
    print (val)


scale = Scale(root, command=print_value, from_=0, to=180, orient=HORIZONTAL, length=170, bg="#909090",
              activebackground="#1f1f1f", fg='#1f1f1f', troughcolor='#1f1f1f')
scale.place(x=910, y=630)

scale = Scale(root, command=print_value, from_=0, to=180, orient=VERTICAL, length=170, bg="#909090",
              activebackground="#1f1f1f", fg='#1f1f1f', troughcolor='#1f1f1f')
scale.place(x=1090, y=520)


# Botões teclas

root.bind('<Escape>', sairtelacheia)

root.bind('<w>', btww)
root.bind('<s>', btss)
root.bind('<d>', btdd)
root.bind('<a>', btaa)

root.bind('<Up>', btww)
root.bind('<Down>', btss)
root.bind('<Right>', btdd)
root.bind('<Left>', btaa)


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame1 = cv2.resize(frame, (800, 600))  # 1000,700  #dimensões proporcionais a câmera
    cv2image = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


show_frame()
root.mainloop()
