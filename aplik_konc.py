import tkinter as tk
from tkinter import ttk
import runpy
import tkinter.font as TkFont
import time



window = tk.Tk()
TkFont.families()
window.title("Aplikacja do wykrywania emocji")
window.geometry("1000x650")
text = tk.Label(window, text="Aplikacja do wykrywania emocji", width=100, height=1, foreground="black")
text.config(font=("Calibri", 20))
text.pack()
f = TkFont.Font(text, text.cget("font"))
f.configure(underline=True)
text.configure(font=f)


def close_window():
    window.destroy()


btn1 = tk.Button(window, text="Wykrywanie emocji na zdjęciach za pomocą biblioteki FER ", width=65, height=1, command=lambda:runpy.run_module('emo', run_name='__main__'), activeforeground="green", relief="raised", bd=8, bg="#59bdff", cursor="hand2")
btn2 = tk.Button(window, text="Wykrywanie emocji na zdjęciach za pomocą biblioteki facial_emotion_recognition", width=65, height=1, command=lambda:runpy.run_module('FacialEmo', run_name='__main__'), activeforeground="green", relief="raised", bd=8, bg="#59bdff", cursor="hand2")
btn3 = tk.Button(window, text="Wykrywanie emocji na kamerze za pomocą biblioteki FER", width=65, height=1, command=lambda:runpy.run_module('kamera_emo', run_name='__main__'), activeforeground="green", relief="raised", bd=8, bg="#59bdff", cursor="hand2")
btn4 = tk.Button(window, text="Wykrywanie emocji na kamerze za pomocą biblioteki facial_emotion_recognition", width=65, height=1, command=lambda:runpy.run_module('FacialEmoCam', run_name='__main__'), activeforeground="green", relief="raised", bd=8, bg="#59bdff", cursor="hand2")
btn5 = tk.Button(window, text="Wyjście", width=65, height=1, command=lambda:close_window(), activeforeground="green", relief="raised", bd=8, bg="#59bdff", cursor="hand2")
btn1.place(relx=0.5, rely=0.13, anchor=tk.CENTER)
btn2.place(relx=0.5, rely=0.30, anchor=tk.CENTER)
btn3.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
btn4.place(relx=0.5, rely=0.64, anchor=tk.CENTER)
btn5.place(relx=0.5, rely=0.81, anchor=tk.CENTER)
btn1.config(font=("Calibri", 20))
btn2.config(font=("Calibri", 20))
btn3.config(font=("Calibri", 20))
btn4.config(font=("Calibri", 20))
btn5.config(font=("Calibri", 20))
btn1.bind("<Button-1>")
btn2.bind("<Button-1>")
btn3.bind("<Button-1>")
btn4.bind("<Button-1>")
btn5.bind("<Button-1>")
window.mainloop()