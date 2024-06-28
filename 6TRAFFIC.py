import tkinter as tk
import random

class TrafficControlSystem:
    def __init__(self, master):
        self.master = master
        master.title("Traffic Control System")

        self.directions = ['North', 'South', 'East', 'West']
        self.colors = {'Red': '#FF0000', 'Green': '#00FF00', 'Yellow': '#FFFF00'}
        self.signal_states = {direction: random.choice(list(self.colors.keys())) for direction in self.directions}
        
        self.direction_labels = {direction: tk.Label(master, text=f"{direction} Direction", font=("Helvetica", 16)) for direction in self.directions}
        self.color_labels = {direction: tk.Label(master, text=f"Signal: {self.signal_states[direction]}", font=("Helvetica", 16), fg=self.colors[self.signal_states[direction]]) for direction in self.directions}
        self.time_elapsed = {direction: 0 for direction in self.directions}
        self.time_labels = {direction: tk.Label(master, text=f"Time({direction}): 0s", font=("Helvetica", 16)) for direction in self.directions}
        
        self.manual_buttons = {direction: tk.Button(master, text=f"Change {direction} Signal", command=lambda d=direction: self.change_signal_manual(d)) for direction in self.directions}
        self.start_button = tk.Button(master, text="Start Automatic", command=self.start_automatic)
        self.stop_button = tk.Button(master, text="Stop Automatic", command=self.stop_automatic)

        for direction in self.directions:
            self.direction_labels[direction].pack()
            self.color_labels[direction].pack()
            self.time_labels[direction].pack()
            self.manual_buttons[direction].pack()
        
        self.start_button.pack()
        self.stop_button.pack()

        self.automatic_running = False
        self.update_time()

    def update_time(self):
        if self.automatic_running:
            for direction in self.directions:
                self.time_elapsed[direction] += 1
                self.time_labels[direction].config(text=f"Time({direction}): {self.time_elapsed[direction]}s")
            self.master.after(1000, self.update_time)

    def change_signal_manual(self, direction):
        new_color = random.choice(list(self.colors.keys()))
        self.signal_states[direction] = new_color
        self.color_labels[direction].config(text=f"Signal: {new_color}", fg=self.colors[new_color])
        self.time_elapsed[direction] = 0  # Reset time elapsed to 0 seconds

    def start_automatic(self):
        self.automatic_running = True
        self.update_time()

    def stop_automatic(self):
        self.automatic_running = False

def main():
    root = tk.Tk()
    root.geometry("400x500")
    app = TrafficControlSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
