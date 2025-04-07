
import tkinter as tk
from tkinter import messagebox
from src.ai_recon import recon
from src.stealth_mode import stealth
from src.role_access import access

def show_recon():
    recon.generate_report()
    messagebox.showinfo("AI Recon", "Report generated successfully.")

def launch_gui():
    role = access.authenticate_user()
    if not role:
        return

    window = tk.Tk()
    window.title("Tactical Simulation GUI")
    window.geometry("500x300")

    tk.Label(window, text="Welcome to the Secure Simulation System", font=("Helvetica", 14)).pack(pady=20)

    tk.Button(window, text="🧠 Generate AI Recon Report", command=show_recon).pack(pady=10)
    tk.Button(window, text="🕵️ Stealth Mode", command=stealth.launch_stealth_dashboard).pack(pady=10)
    tk.Button(window, text="❌ Exit", command=window.destroy).pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    launch_gui()
