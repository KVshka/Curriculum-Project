from tkinter import *
from tkinter import font
import os as os

def Autorize():
    def StartGame(): #Создаём окно с игровым полем и открываем его
        class Tile():
            def __init__(self, number):
                self.number = number

            def Create(self):
                def b1(event):
                    global player

                if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    tile = Button(master=canvas, width=100, height=100, bg="#000000", anchor=N)
                    button_window = canvas.create_window(i*100, j*100, anchor=NW, window=tile)

                else:
                    tile = Button(master=canvas, width=100, height=100, bg="#FFFAFA", anchor=N)
                    button_window = canvas.create_window(i*100, j*100, anchor=NW, window=tile)
                    if j > 3:
                        tile["image"] = i1
                    elif j < 3:
                        tile["image"] = i3
                    tile.bind('<Button-1>', b1)
        global number
        root.destroy() #Закрываем лишние окна
        start.destroy()
        game = Tk()
        game.title("Игра")
        canvas = Canvas(game, height=700, width=800)
        canvas.grid()
        i1=PhotoImage(file="1b.gif")
        i2=PhotoImage(file="1bk.gif")
        i3=PhotoImage(file="1h.gif")
        i4=PhotoImage(file="1hk.gif")
        for i in range(8):
            for j in range(7):
                Tile.Create(number)
                number+=1
        game.mainloop()

    font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
    start = Tk()
    start.title("Начать игру")
    start.geometry("300x100")
    start.configure(background="#F8F8FF")
    message = Label(master=start, anchor=W, bg="#F8F8FF", text="Вы успешно авторизовались!", font=font1)  #Авторизуем пользователя
    message.pack(padx=6, pady=6)
    btn = Button(master=start, text="Начать игру", anchor=W, bg="#6A5ACD", fg="#FFFFFF", font=font1, command=StartGame)
    btn.pack(padx=6, pady=6) 
    if os.path.exists("register.txt"):
        file = open("register.txt", "r+") #Открываем файл с данными пользователей
        if not (login.get() or password.get()):
            message = Label(anchor=W, bg="#F8F8FF", text="Заполните все поля!", font=font1)
        else:
            if (login.get() and password.get()) in file.read().split(): #Если введённые данные уже есть
                start.mainloop()
            else:
                message["text"] = "Неверный логин или пароль!"
    else:  #Если данные введены впервые (файл данных пользователя отсутствует)
        message["text"] = "Неверный логин или пароль!"

def Register():
    global message
    if login.get()=='' or password.get()=='':
        message["text"] = "Заполните все поля!"
    elif os.path.exists("register.txt"):
        file = open("register.txt", "r+") #Открываем файл с данными пользователей
        if login.get() in file.read().split(): #Если введённые данные уже есть
            message["text"] = "Такой пользователь уже зарегистрирован!"
        else: #Если данные введены впервые
            file.write(login.get() + " " + password.get() + "\n") #Регистрируем пользователя
            file.close()
            message["text"] = "Вы успешно зарегистрировались!"
    else:
        file = open("register.txt", "w") #Создаём файл с данными пользователей
        file.write(login.get() + " " + password.get() + "\n") #Регистрируем пользователя
        file.close()
        message["text"] = "Вы успешно зарегистрировались!"
     
number = 0
player = 1

root = Tk()     # создаем корневой объект - окно
root.title("Лабораторная работа №9")     # устанавливаем заголовок окна
root.geometry("500x350")    # устанавливаем размеры окна
root.configure(background="#F8F8FF")
font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
hello = Label(font=font1, anchor=W, background="#F8F8FF", text="Добро пожаловать в игру 'Киммерийские шашки - поддавки!'\nДля продолжения авторизуйтесь") # создаем текстовую метку
hello.pack(padx=6, pady=6)
llogin = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш логин") # создаем текстовую метку
llogin.pack(padx=6, pady=6) # размещаем метку в окне
login=Entry(bd=2)
login.pack(padx=6, pady=6)
lpassword = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш пароль") 
lpassword.pack(padx=6, pady=6)
password=Entry(bd=2)
password.pack(padx=6, pady=6)
btn1 = Button(text="Войти", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=Autorize) #создаём кнопки и устанавливаем внутри окна
btn1.pack(padx=6, pady=6) 
plsreg = Label(font=font1, anchor=W, background="#F8F8FF", text="Нет профиля? Зарегистрируйтесь!") # создаем текстовую метку
plsreg.pack(padx=6, pady=6)
btn2 = Button(text="Зарегистрироваться", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=Register) #создаём кнопки и устанавливаем внутри окна
btn2.pack(padx=6, pady=6)
message = Label(anchor=W, bg="#F8F8FF", font=font1)
message.pack(padx=6, pady=6)
root.mainloop()




