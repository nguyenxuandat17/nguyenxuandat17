import tkinter as tk

border_effects = {
    "First": tk.FLAT,
    "Secnod": tk.FLAT,
    "Third": tk.FLAT,
    "Click Me": tk.GROOVE,
    
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=4)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()