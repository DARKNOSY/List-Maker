import tkinter as tk
from tkinter import filedialog, messagebox
import json

banner = """

░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓███████▓▒░ ░▒▓████████▓▒░                        @
░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░                                D
░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░                                    A
░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓██████▓▒░     ░▒▓█▓▒░                                        R
░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░    ░▒▓█▓▒░                                            K
░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░    ░▒▓█▓▒░                                                N
░▒▓████████▓▒░ ░▒▓█▓▒░ ░▒▓███████▓▒░     ░▒▓█▓▒░                                                    O
                                                                                                        S
                                                                                                            Y
░▒▓██████████████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓███████▓▒░  ░▒▓██████▓▒░   ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                    
"""

class ConfigEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("List Maker")
        self.configure(bg="#1e1e1e")
        
        self.options = {
            "delete_lines": False, # Delete empty lines
            "delete_duplicates": False, # Delete duplicate elements in output list
            "separate_files": False, # Put files' content in the output list file and a space between each files' content
            "reset_config": False, # Reset config after use
            "delimiter_before": r"\n",  # Delimiter in input files
            "delimiter_after": r"\n",   # Delimiter in output file
            "input_files": [], # Input files
            "output_name": "output"
        }
        
        self.option_vars = {}
        self.load_config()
        self.create_widgets(self.option_vars)
    
    def create_widgets(self, option_vars):
        for i, (option, value) in enumerate(self.options.items()):
            fg_color = "#ffffff"
            
            if isinstance(value, bool):
                var = tk.BooleanVar(value=value)
                option_vars[option] = var
                checkbox = tk.Checkbutton(self, text=option.replace('_', ' ').capitalize(), variable=var, bg="#1e1e1e", fg=fg_color, selectcolor="#1e1e1e")  # Adjust text presentation
                checkbox.grid(row=i, column=0, sticky="w")
            elif isinstance(value, list):
                label = tk.Label(self, text=option.replace('_', ' ').capitalize(), bg="#1e1e1e", fg=fg_color)
                label.grid(row=i, column=0, sticky="w")
                add_button = tk.Button(self, text="Add Files", command=lambda option=option: self.add_files(option), bg="#3c3c3c", fg=fg_color)
                add_button.grid(row=i, column=1, sticky="w")
                file_label = tk.Label(self, text=", ".join(value), bg="#1e1e1e", fg=fg_color)
                file_label.grid(row=i, column=2, sticky="w")
            elif isinstance(value, str):
                label = tk.Label(self, text=option.replace('_', ' ').capitalize(), bg="#1e1e1e", fg=fg_color)
                label.grid(row=i, column=0, sticky="w")
                entry = tk.Entry(self, bg="#3c3c3c", fg=fg_color)
                entry.grid(row=i, column=1, sticky="w")
                entry.insert(0, value)
                option_vars[option] = entry
        
        save_button = tk.Button(self, text="Save", command=self.save_config, bg="#4CAF50", fg="#ffffff")
        save_button.grid(row=i+3, column=0, pady=10)
    
    def load_config(self):
        try:
            with open("src/config.json", "r") as f:
                loaded_config = json.load(f)
                for key, value in loaded_config.items():
                    if value == "\n":
                        loaded_config[key] = self.options[key]
                self.options = loaded_config
        except FileNotFoundError:
            messagebox.showinfo("Info", "Config file not found.")
    
    def save_config(self):
        for option, var in self.option_vars.items():
            if isinstance(var, tk.BooleanVar):
                self.options[option] = var.get()
            elif isinstance(var, tk.Entry):
                self.options[option] = var.get()
        
        with open("src/config.json", "w") as f:
            json.dump(self.options, f, indent=4)

        messagebox.showinfo("Success", "Config saved successfully.")
        exit()
    
    def add_files(self, option):
        files = filedialog.askopenfilenames()
        if files:
            self.options[option] = list(files)
            for widget in self.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("text") == option:
                    widget.grid_forget()
            file_label = tk.Label(self, text=", ".join(files), bg="#1e1e1e", fg="#ffffff")
            file_label.grid(row=list(self.options.keys()).index(option), column=2, sticky="w")
    
    def toggle_checkbox(self, option):
        state = "Checked" if self.option_vars[option].get() else "Unchecked"
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text") == option.replace('_', ' ').capitalize():
                widget.config(text=state)

if __name__ == "__main__":
    print(banner)
    app = ConfigEditor()
    app.mainloop()