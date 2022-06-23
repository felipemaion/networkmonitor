import tkinter as tk
from tkinter import Frame, Label
import time


class DigitalClock:
    def __init__(self, frame) -> None:
        self.frame = frame
        self.frame_pc = Frame(self.frame, highlightbackground="black", highlightthickness=2)
        self.label = Label(text="OLA", font=("digital-7", 40))
        self.label.grid()
        self.update()
        
    
    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        """ update the label every 1 second """

        self.label.configure(text=self.time_string())

        # schedule another timer
        self.label.after(1000, self.update)
        


if __name__ == "__main__":
    pass