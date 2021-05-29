import tkinter as tk
from typing import Text

window = tk.Tk()
window.destroy()
text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "Name: Nguyễn Xuân Đạt ")
text_box.insert("2.0", "\nAge: 20 tuổi ")
text_box.insert("3.0", "\naddress: tru son-doluong-nghe an ")
text_box.insert("4.0", "\ngiới tính: nam ")

window.mainloop()
