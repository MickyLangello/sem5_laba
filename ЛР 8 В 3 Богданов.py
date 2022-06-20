'''
1.Создать простую программу, предусматривающую смену на экране в цикле
(период 5 сек.) фамилии студента, номера группы и номера в варианта.

2.Дополнить программу модулем парольного доступа.

Пароль на основе алгоритма - отображаются случайным образом 18 цифр
и букв, в ответ надо ввести по нечетным датам только буквы, а по
четным - цифры. При четырехкратном неправильном вводе автоматически
на 15 сек  программа блокируется, далее разрешается еще одни вход.
Если он неудачен – программа завершается. Логическая бомба срабатывает
по вторникам и создает в папке с программой текстовый файл с
названием в виде текущего дня недели, в который заносятся текущая
дата и время. 
'''

from tkinter import * 
from random import *
from datetime import *
from time import *

def cycle():
    
    label = Label(width = 16, font = "Arial 14")
    label.place(x = 105, y = 90)
    
    global iterator
    if iterator%3==0:
        label.config(text="Богданов")
    if iterator%3==1:
        label.config(text="19-ИЭ-1")
    if iterator%3==2:
        label.config(text="И-3")
    iterator+=1
    
    root.after(5000,cycle)

        
def inside():
    access.place_forget()
    password.place_forget()
    button.place_forget()

    root.after(100,cycle())


def enter():
    digits=[]
    letters=[]
    global error, parol

    for j in range(len(parol)):
        if parol[j].isdigit():
            digits+=parol[j]
        else:letters+=parol[j]
  
    digJ = "".join(digits) #пароль на чётные дни
    letJ = "".join(letters)#пароль на нечётные дни
    
    date=datetime.now()

    if date.day%2==0: #определение чётности текущего дня
        
        if password.get() == digJ:
            inside()
        else: error+=1
        
    else:
        
        if password.get() == letJ:
            inside()
        else: error+=1


    if error==4:
        password.place_forget()
        button.place_forget()
        
        root.update()
        sleep(15) #время блокировки программы
        
        password.place(x = 55, y = 110)
        button.place(x = 230, y = 110)

    if error==5:
        if date.isoweekday()==2: #определение дня недели (вторник-2)
            f = open('Вторник.txt', 'w')
            k=str(date.today())
            f.write(k)
            f.close()
        root.destroy()

def symbols():
    arr="qwertyuiopasdfghjklzxcvbnm1234567890"
    txt=""
    for i in range(18):
        txt+=choice(arr)
    return txt

root = Tk()
root.resizable(0, 0)
root.geometry('400x250')
root.title('Лабораторная работа №8')

error=0 #счётчик ошибок
iterator=0 #переменная для выбора отображаемого текста
parol = symbols() #генерация пароля

c = Canvas(width = 396, height = 246, bg = 'lightgrey')
c.place(x = 0, y = 0)

access = Label(width = 32, text = parol, font = "Arial 11")
access.place(x = 55, y = 70)

password = Entry(width = 20 ,show = "*", font = "Arial 11")
password.place(x = 55, y = 110)

button = Button(text = "Enter", command = enter)
button.place(x = 230, y = 110)

root.mainloop()

