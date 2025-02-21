import os
import tkinter as tk
from tkinter import messagebox

class ShutdownSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shutdown Scheduler")
        self.root.geometry("480x320")
        
        self.create_widgets()

    def create_widgets(self):
        # Create and place the label and entry
        self.label = tk.Label(self.root, text="Enter minutes to shutdown:")
        self.label.place(relx=0.5, rely=0.2, anchor='center')

        self.entry = tk.Entry(self.root)
        self.entry.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.5)

        # Create and place the buttons
        self.schedule_button = tk.Button(self.root, text="Schedule Shutdown", command=self.schedule_shutdown)
        self.schedule_button.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.3, relheight=0.1)

        self.cancel_button = tk.Button(self.root, text="Cancel Shutdown", command=self.cancel_shutdown)
        self.cancel_button.place(relx=0.5, rely=0.7, anchor='center', relwidth=0.3, relheight=0.1)

    def schedule_shutdown(self):
        try:
            minutes = int(self.entry.get())
            seconds = minutes * 60
            messagebox.showinfo("Shutdown Scheduled", f"System will shutdown in {minutes} minutes.")
            os.system(f"shutdown /s /f /t {seconds}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

    def cancel_shutdown(self):
        os.system("shutdown /a")
        messagebox.showinfo("Shutdown Canceled", "Scheduled shutdown has been canceled.")

if __name__ == "__main__":
    tKroot = tk.Tk()
    app = ShutdownSchedulerApp(tKroot)
    tKroot.mainloop()