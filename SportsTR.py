# Brenden Overstreet | DLM: 5-10-2024 | v1.0.0
# This program allows a user to enter the players stats and it relays the percentages back to them
# Code used from ButtonClicker1.py made by Ryan Russell

import tkinter as tk
import math

class MainWindow:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Sports Tracker")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Basketball")
        self.label.pack(pady=10)

        self.button = tk.Button(self.root, text="Open", command=self.open_basketball_window)
        self.button.pack(pady=10)

        self.label = tk.Label(self.root, text="Football")
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Open", command=self.open_football_window)
        self.button.pack(pady=20)

        self.label = tk.Label(self.root, text="Baseball")
        self.label.pack(pady=30)

        self.button = tk.Button(self.root, text="Open", command=self.open_baseball_window)
        self.button.pack(pady=30)
                                
    def open_basketball_window(self):
        self.basketball_window = BasketballWindow(self.root, self)

    def open_football_window(self):
        self.football_window = FootballWindow(self.root, self)

    def open_baseball_window(self):
        self.baseball_window = BaseballWindow(self.root, self)

    def run(self):
        self.root.mainloop()

class BasketballWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        
        self.top = tk.Toplevel(self.master)
        self.top.title("Basketball")
        self.top.geometry("400x400")

class FootballWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        
        self.top = tk.Toplevel(self.master)
        self.top.title("Football")
        self.top.geometry("400x400")

class BaseballWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        
        self.top = tk.Toplevel(self.master)
        self.top.title("Baseball")
        self.top.geometry("400x400")

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.run()
