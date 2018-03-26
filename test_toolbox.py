import tkinter as tk
from toolbox import Toolbox
from tool import Tool


class ToolCircle(Tool):
    text = "Circle"

    def on_click_down(self, event):
        self.target.create_oval((event.x-4, event.y-4, event.x+4, event.y+4))


class ToolSquare(Tool):
    text = "Square"

    def on_click_down(self, event):
        self.target.create_rectangle(
            (event.x-4, event.y-4, event.x+4, event.y+4))


root = tk.Tk()
canvas = tk.Canvas(root, bg="white")
canvas.bind("<Button-1>", lambda e: print("First binding"), "+")
toolbox = Toolbox(root, canvas, [ToolCircle, ToolSquare])
toolbox.pack()
canvas.pack()
root.mainloop()
