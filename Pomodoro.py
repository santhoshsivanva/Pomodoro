import math
from tkinter import *
import playsound

# CONSTANTS
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
resett = False

#--TIMER START--#
def reset():
    window.destroy()


#--TIMER START--#
def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    playsound.playsound('jarvis.mp3')
    if reps % 8 == 0:
        count_down(long_break_sec)
        Label_time.config(text="   Long Break")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        Label_time.config(text="   Short Break")

    else:
        count_down(work_sec)
        Label_time.config(text="   Work")
        butt_start.config(state=DISABLED)
    
#---COUNTDOWN MECHANISM---#


def count_down(count):
    count_min = math.floor(count/60)  # 5 minutes
    count_sec = count % 60  # 6
    if count_sec < 10:  # for value less than 10 which is singular value
        count_sec = "0"+str(count_sec)
    if count_min == 0:
        count_min = "00"  # for time-convention
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
            window.after(1000, count_down, count-1)
    else:
        timer()


# ---UI SETUP--- #
window = Tk()
window.title("Pomodoro")
window.maxsize(400, 530)
p1 = PhotoImage(file = 'Images/front1.png') 
window.iconphoto('False',p1)

# Label
Label_time = Label(text="  Timer", font=("Arial", 20, "bold"), fg=RED)
Label_time.grid(column=1, row=0)


# For importing the image we need to use the canvas into it
# for setting the color in the canvas and window we need touse the (bg)
canvas = Canvas(width=400, height=400, bg=YELLOW,
                highlightthickness=0)  # seperate canvas
ironM = PhotoImage(file="Images/iron.png")  # adding a image into it
canvas.create_image(190, 220, image=ironM)  # image size
canvas.create_rectangle(320, 270, 120, 180, fill="black")
time_text = canvas.create_text(
    220, 225, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


butt_start = Button(font=("Arial", 10, "bold"), text="Start",
                    width=15, bg=RED, command=timer)
butt_end = Button(font=("Arial", 10, "bold"), text="End",
                  width=15, bg=RED, command=reset)

butt_start.grid(column=1, row=3)
butt_end.grid(column=1, row=4)
# for close inches we need to do the highlightthickness

End = Label(text="End restart the whole process again", font=("Arial", 10, "bold"))
End.grid(column=1, row=5)

# Exits
window.mainloop()