###############################################################################
# 100 Days of Code - The Complete Python Pro Bootcamp for 2021                #
# Exercise 89 - Disappearing Text                                             #
# An online writing app where if you stop typing, your work will disappear.   #
# Based on https://www.squibler.io/dangerous-writing-prompt-app               #
# Course Instructor: Angela Yu                                                #
# Coded by: John Cupak, jcupak@acm.org                                        #
# History: 2021-08-16 UI Setup                                                #
#          2021-08-18 Add timer and count down code and                       #
###############################################################################

from tkinter import *  # Everything

# -------------------------------- CONSTANTS -------------------------------- #
YELLOW        = "#f7f5dd"          # Main window background color
WHITE         = "#ffffff"          # Text widget background color
PINK          = "#ffcccc"          # Text widget timeout background color
WINDOW_WIDTH  = 600                # Width of main window
WINDOW_HEIGHT = 350                # Height of main window
PADDINGS      =   5                # Internal spacing
MARGINS       =  10                # External spacing
HEIGHT_LINES  =  20                # Text widget height in lines
WIDTH_CHARS   =  80                # Text widget width in characters
INTERVAL      =   5                # Count down timer in seconds

# --------------------------------- GLOBALS --------------------------------- #
timer         = None               # Dynamically reassigned when starting


# ------------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets global timer"""
    start_timer()


# ------------------------------- TIMER START ------------------------------- #
def start_timer():
    """Starts count down 5 second timer"""
    count_down(INTERVAL)


# --------------------------- COUNTDOWN MECHANISM --------------------------- #
def count_down(count):
    """Set timer to count down seconds"""
    if count > 0:
        # Call count_down function after 1000ms with decremented count
        global timer                       # Give me access to modify
        timer = window.after(1000, count_down, count - 1)
    else:
        # count has been decremented to zero.
        window.after_cancel(timer)                    # Kill timer
        input_text.delete('1.0', END)                 # Erase all text
        input_text.config(background=PINK)            # Set Background Color to pink
        input_text.config(font=("Helvetica", 12))     # Larger font for message
        input_text.insert(END, "All your base are belong to us!\nThis window will disappear in 3 seconds!")
        window.after(3000, lambda: window.destroy())  # After 3 seconds


def key(event):
    """Resets timer if any key is pressed"""

    # print('key: {}'.format(event.char))  # Initial version - print key that was pressed
    window.after_cancel(timer)             # Kill timer
    reset_timer()                          # Reset timer to another 5 seconds


# --------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Disappearing Text")

# Center window calculations
screen_width  = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
start_x = int(screen_width/2 - WINDOW_WIDTH/2)
start_y = int(screen_height/2 - WINDOW_HEIGHT/2)
window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, start_x, start_y))

input_text = Text(window, bg=WHITE, height=HEIGHT_LINES, width=WIDTH_CHARS, wrap=WORD)
input_text.focus_set()         # Set the keyboard focus to the input text widget
input_text.bind("<Key>", key)  # Bind text field to any keypress
input_text.grid(row=0, column=0, padx=MARGINS, pady=MARGINS)

Label(text="Type your text in the window above.").grid(row=1, column=0)

window.configure(padx=10, pady=10, bg=YELLOW)

# --------------------------------- "ENGAGE!" -------------------------------- #
start_timer()      # Start 5-second count down timer
window.mainloop()  # Start main loop
