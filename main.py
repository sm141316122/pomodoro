from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
repeat = 1
check = ""
timer = None


def reset():
    global repeat, check
    window.after_cancel(timer)
    repeat = 1
    canvas.itemconfig(time, text=f"00:00")
    title_label.config(text="Timer", fg=GREEN)
    check = ""


def start_count():
    global repeat
    count_time = WORK_MIN * 60
    title_label.config(text="Work", fg=RED)
    if repeat == 8:
        count_time = LONG_BREAK_MIN
        title_label.config(text="Break", fg=GREEN)
    elif repeat % 2 == 0:
        count_time = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg=GREEN)

    count_down(count_time)


def count_down(count_time):
    global check, repeat
    count_min = count_time // 60
    count_sec = count_time % 60
    if count_time < 60:
        count_min = "00"
        count_sec = int(count_sec)
        if count_sec < 10:
            count_sec = f"0{count_sec}"

    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count_time < 0:
        if repeat % 2 != 0:
            check += "✔"
        check_label.config(text=check)
        repeat += 1
        if repeat == 9:
            repeat = 1
            canvas.itemconfig(time, text=f"00:00")
            title_label.config(text="Timer", fg=GREEN)
            check = ""
        else:
            start_count()
    else:
        global timer
        timer = window.after(1000, count_down, count_time - 1)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.config(bg=YELLOW)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
time = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)
check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
check_label.grid(row=3, column=1)

start_button = Button(text="Start", command=start_count, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
