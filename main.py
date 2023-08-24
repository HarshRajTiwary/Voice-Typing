import tkinter as tk
import pyautogui
import time
import speech_recognition as sr
from tkinter import messagebox

class Voice_Typing():
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Typing")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        about = tk.Menu(menubar, tearoff=0)
        about.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="About", menu=about)

        e = tk.Menu(menubar, tearoff=0)
        e.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="Exit", menu=e)

        self.l = tk.Button(self.root, text="Start", command=self.listen)
        self.sl = tk.Button(self.root, text="Stop", command=self.stop_listen)

        self.l.pack(side=tk.LEFT, padx=5, pady=5)
        self.sl.pack(side=tk.LEFT, padx=5, pady=5)

        self.status_text = tk.StringVar()
        self.status_text.set("Not listening")
        self.status_label = tk.Label(self.root, textvariable=self.status_text)
        self.status_label.pack(side=tk.BOTTOM, padx=5, pady=5)

    def listen(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.status_text.set("Listening...")
            self.root.update()
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio)
            pyautogui.typewrite(text)
        except sr.UnknownValueError:
            self.status_text.set("Sorry, could not recognize what you said")
        except sr.RequestError:
            self.status_text.set("Sorry, could not connect to the speech recognition service")
        self.root.update()

    def stop_listen(self):
        self.status_text.set("Listening stopped")

    def exit_app(self):
        self.root.destroy()

    def show_about(self):
        about_text = "Voice Typing\nVersion 1.0\n\nThis app is developed by Er. Harsh Raj, this app allows you to use your voice as input and types what you said."
        messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x50")
    app = Voice_Typing(root)
    root.mainloop()
