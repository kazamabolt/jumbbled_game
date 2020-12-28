from tkinter import *
import random
import tkinter.font as font
import time

running = True

while running == True:

    start_time = time.time()

    root = Tk()
    root.geometry('+100+0')
    root.configure(bg="#000000")
    root.iconphoto(True, PhotoImage(file="Sup.png"))
    root.title("JUMBLE WORDS")
    root.resizable(width=False, height=False)

    def random_word():
        words = ["RAIN", "CLOUD", "NATURE", "BEAUTIFUL", "HOUSE"]
        pick = random.choice(words)
        return pick

    def jumbled_word(word):
        word = random.sample(word, len(word))
        word_jumbled = "".join(word)
        return word_jumbled

    pick = random_word()

    jumbled = jumbled_word(pick)

    list1 = list(jumbled)
    len_list1 = len(list1)

    for i in range(len_list1):
        list1[i] = PhotoImage(file=str(list1[i]) + str("_P.png"))

    row_0 = 0
    col_0 = 0

    for i in range(len_list1):
        B = Label(root, image=list1[i])
        B.grid(row=row_0, column=col_0)
        col_0 = col_0 + 1

    root.grid_rowconfigure(1, minsize=10)

    myFont = font.Font(family='Calibri', weight='bold')

    your_choice = PhotoImage(file="YOUR_GUESS.png")
    surprise = PhotoImage(file="sup.png")
    win = PhotoImage(file="WINNN.png")
    lose = PhotoImage(file="LOSEEE.png")
    check = PhotoImage(file="CHECKK.png")
    close = PhotoImage(file="CLOSEE.png")


    label = Label(root, image=your_choice)
    label.grid(row=2, column=0, columnspan=len_list1)
    label["font"] = myFont

    root.grid_rowconfigure(3, minsize=10)

    e1 = Entry(root, bd=5, bg="#9ca1db", justify=CENTER, font=myFont, fg="#000000")
    e1.grid(row=4, column=0, columnspan=len_list1)

    root.grid_rowconfigure(5, minsize=10)

    answer = (e1.get()).upper()

    list2 = list(pick)

    for j in range(len(list2)):
        list2[j] = PhotoImage(file=str(list2[j]) + str("_P.png"))

    button = Button(root, image=check, command=lambda: result())
    button.grid(row=6, column=0)

    Btn = Button(root, image=close, command=lambda: reset())
    Btn.grid(row=6, column=len_list1 - 1)

    root.grid_rowconfigure(7, minsize=10)

    label2 = Label(root, image=surprise)
    label2.grid(row=8, column=0, columnspan=len_list1)

    root.grid_rowconfigure(9, minsize=10)

    myFont = font.Font(family='Comic Sans MS', weight='bold')

    label3 = Label(root, text="TIME : ", width=12, bg="#f5ab55", justify=CENTER, font=myFont, fg="#000000",
                   relief=RAISED)
    label3.grid(row=12, column=0, columnspan=len_list1)

    def result():

        answer = (e1.get()).upper()

        if answer == pick:

            time_taken = time.time() - start_time
            time_taken = int(time_taken)

            label3.configure(text="TIME : " + str(time_taken) + " Sec")

            label2.configure(image=win)

            col_2 = 0
            row_2 = 10

            for i in range(len_list1):
                B = Label(root, image=list2[i])
                B.grid(row=row_2, column=col_2)
                col_2 = col_2 + 1

            root.grid_rowconfigure(11, minsize=10)

            root.update_idletasks()
            root.after(3000)
            root.destroy()

        else:

            label2.configure(image=lose)

            root.update_idletasks()
            root.after(500)
            label2.configure(image=surprise)

            e1.delete(0, "end")


    def reset():
        global running
        running = False

        root.destroy()

    root.mainloop()
