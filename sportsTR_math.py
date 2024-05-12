# Imports tkinter into the file
import tkinter as tk
from tkinter import messagebox

# This creates the class that runs the calculator in the window
class SportsStatsCalculator:
    def __init__(self, master, sport):
        self.master = master
        self.sport = sport
        self.master.title(f"{self.sport} Stats Calculator")

        self.create_widgets()
    # This creates your labels and input boxes
    def create_widgets(self):
        tk.Label(self.master, text=f"Enter {self.sport} stats:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

        tk.Label(self.master, text="Goals/Runs/Points Scored:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.score_entry = tk.Entry(self.master)
        self.score_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Total Shots/At-bats/Field Goals Attempted:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.shots_entry = tk.Entry(self.master)
        self.shots_entry.grid(row=2, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_stats)
        self.calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.close_button = tk.Button(self.master, text="Close Window", command=self.master.destroy)
        self.close_button.grid(row=4, columnspan=2, padx=10, pady=10)

    # This gets the results, checks them, and displays the results
    def calculate_stats(self):
        score = self.score_entry.get()
        shots = self.shots_entry.get()

        try:
            score = float(score)
            shots = float(shots)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for score and shots.")
            return

        if shots == 0:
            messagebox.showerror("Error", "Total shots/At-bats/Field Goals Attempted cannot be zero.")
            return

        if self.sport == "Football":
            percentage = (score / shots) * 100
            messagebox.showinfo("Result", f"Scoring Percentage: {percentage:.2f}%")
        elif self.sport == "Baseball":
            batting_avg = score / shots
            messagebox.showinfo("Result", f"Batting Average: {batting_avg:.3f}")
        elif self.sport == "Basketball":
            shooting_percentage = (score / shots) * 100
            messagebox.showinfo("Result", f"Shooting Percentage: {shooting_percentage:.2f}%")
