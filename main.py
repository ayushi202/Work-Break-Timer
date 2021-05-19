from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timers=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=1
    window.after_cancel(timers)
    canvas.itemconfig(timer_text,text=f"00:00")
    timer["text"]="Timer"
    timer["foreground"]=GREEN
    tick["text"]=""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    Long_break_sec=LONG_BREAK_MIN*60
    if reps%2==1:
        count_down(work_sec)
        timer["text"]="Work Time"
        timer["foreground"]=GREEN
        tick["text"]="✓"*math.ceil(reps/2)
    elif reps==8:
        count_down(Long_break_sec)
        timer["text"]="Break"
        timer["foreground"]=RED
    elif reps%2==0 and reps<8:
        count_down(short_break_sec)
        timer["text"]="Break"
        timer["foreground"]=PINK
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    seconds=count%60
    minutes=count//60
    if seconds==0:
        seconds="00"
    elif len(str(seconds))==1:
        seconds="0"+str(seconds)
    if minutes<10:
        minutes="0"+str(minutes)
    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count>0:
        global timers
        timers=window.after(1000,count_down,count-1)
    if count==0 or count<0:
        reps+=1
        start_timer()
        if reps%2==1:
            tick["text"]="✓"*math.ceil(reps/2)
        

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Work-Break Timer")
window.config(padx=100,pady=100,bg=YELLOW)

timer=Label(text="Timer",foreground=GREEN,font=(FONT_NAME,28,"bold"),bg=YELLOW)
timer.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file=r"C:\Users\hp 840g2\Documents\python\timer\tomato.png")
canvas.create_image(100,112,image=img)

timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

start_button=Button(text="Start",font=(FONT_NAME,10),command=start_timer)
start_button.grid(row=2,column=0)

tick=Label(text="",foreground=GREEN,font=(15),bg=YELLOW)
tick.grid(row=3,column=1)

reset_button=Button(text="Reset",font=(FONT_NAME,10),command=reset_timer)
reset_button.grid(row=2,column=2)

window.mainloop()
