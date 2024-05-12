# Brenden Overstreet | DLM: 5-12-2024 | v1.2.1
# This program allows a user to enter the players stats and it relays the percentages back to them

# Imports tkinter as tk in to the python file
import tkinter as tk
from sportsTR_math import SportsStatsCalculator

# This creates the main window class that opens the program
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")
        self.create_widgets()
    # This creates the sub windows
    def create_widgets(self):
        sports = ["Football", "Baseball", "Basketball"]
        for sport in sports:
            tk.Button(self.master, text=f"Open {sport} Calculator", command=lambda sport=sport: self.open_calculator(sport)).pack(pady=5)
        # This creates a button that closes the windows
        close_button = tk.Button(self.master, text="Close Main Window", command=self.master.destroy)
        close_button.pack(pady=10)
    # This defines the calculator that is in the window you choose to open
    def open_calculator(self, sport):
        calculator_window = tk.Toplevel(self.master)
        app = SportsStatsCalculator(calculator_window, sport)
# Define the main function to run the gui
def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
# Runs the gui
if __name__ == "__main__":
    main()





