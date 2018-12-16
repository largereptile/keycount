from tkinter import Tk, Label, Button, Canvas
from pynput import keyboard
import time


keypress_list = []

def on_press(key):
    keypress_list.append((key, time.time()))

class gui():
    def __init__(self, master):
        self.master = master
        master.title("Keycount Test")

        self.canvas = Canvas(master, width=300, height=200, highlightthickness=0, bg="green")
        self.canvas.pack()
        self.text = self.canvas.create_text(150, 100, fill="white", font="arial 100 bold", text="0 k/s")

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

        self.refresh()

    def refresh(self):
        for num, event in enumerate(keypress_list):
            if time.time() - event[1] > 1:
                del keypress_list[num]
        self.canvas.itemconfig(self.text, text="{} k/s".format(len(keypress_list)))
        self.master.after(200, self.refresh)

root = Tk()
root.overrideredirect(True)
my_gui = gui(root)
root.mainloop()
