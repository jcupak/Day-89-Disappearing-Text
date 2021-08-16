###############################################################################
# 100 Days of Code - The Complete Python Pro Bootcamp for 2021                #
# Exercise 89 - Disappearing Text                                             #
# An online writing app where if you stop typing, your work will disappear.   #
# Based on https://www.squibler.io/dangerous-writing-prompt-app               #
# Course Instructor: Angela Yu                                                #
# Coded by: John Cupak, jcupak@acm.org                                        #
# History: 2021-08-16 UI Setup                                                #
###############################################################################

from tkinter import *  # Everything

# -------------------------------- CONSTANTS -------------------------------- #
YELLOW        = "#f7f5dd"          # Main window background color
WHITE         = "#ffffff"
WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 350
PADDINGS      =   5                # Internal spacing
MARGINS       =  10                # External spacing

# --------------------------------- GLOBALS --------------------------------- #

# ------------------------------- TIMER RESET ------------------------------- #

# ------------------------------- TIMER START ------------------------------- #

# --------------------------- COUNTDOWN MECHANISM --------------------------- #

# --------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Disappearing Text")

# Center window calculations
screen_width  = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
start_x = int(screen_width/2 - WINDOW_WIDTH/2)
start_y = int(screen_height/2 - WINDOW_HEIGHT/2)
window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, start_x, start_y))

input_text = Text(window, bg=WHITE, height=20, width=80, wrap=WORD)
input_text.grid(row=0, column=0, padx=MARGINS, pady=MARGINS)

start_button = Button(text="Start", padx=PADDINGS, pady=PADDINGS)  # command=start_timer
start_button.grid(row=1, column=0, padx=MARGINS, pady=MARGINS)

window.configure(padx=10, pady=10, bg=YELLOW)

window.mainloop()
