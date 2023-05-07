import tkinter as tk

class ControlPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Can Crusher Control Panel")

        self.attributes('-fullscreen', True)

        # Set background color
        self.configure(bg="#F0F0F0")

        # Create start/stop button
        self.start_stop_button = self.create_button("Start", self.start_stop_toggle, "green", ("Arial", 20, "bold"), 20, 20)

        # Create debug button
        self.debug_button = self.create_button("Debug", self.debug, "#0052cc", ("Arial", 16))

        # Create wiring button
        self.wiring_button = self.create_button("Wiring", self.edit_wiring, "#d39e00", ("Arial", 16))

        # Create info button
        self.info_button = self.create_button("Info", self.edit_info, "#5cb85c", ("Arial", 16))

        # Create wiring and info text boxes
        self.wiring_text = self.create_text_box()
        self.info_text = self.create_text_box()

        # Create and configure status frame
        status_frame = tk.Frame(self, bg="white", bd=1, relief="solid")
        status_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Create status labels
        self.create_status_label(status_frame, "Operational status:", 0)
        self.create_status_label(status_frame, "Arm connection:", 1)
        self.create_status_label(status_frame, "Controller connection:", 2)

        # Create status circles
        self.operational_circle = self.create_status_circle(status_frame, 0)
        self.arm_circle = self.create_status_circle(status_frame, 1)
        self.controller_circle = self.create_status_circle(status_frame, 2)

        # Set initial status
        self.operational_status = False
        self.arm_status = False
        self.controller_status = False

    def create_button(self, text, command, bg, font, padx=10, pady=10):
        button = tk.Button(self, text=text, command=command, padx=padx, pady=pady, bg=bg, fg="white", font=font)
        button.pack(padx=10, pady=10, fill="both", expand=True)
        return button

    def create_text_box(self):
        text_box = tk.Text(self, width=50, height=5, bg="white", font=("Arial", 12), wrap="word")
        text_box.pack(padx=10, pady=10)
        return text_box

    def create_status_label(self, status_frame, text, row):
        label = tk.Label(status_frame, text=text, font=("Arial", 12), bg="white")
        label.grid(row=row, column=0, padx=10, pady=10, sticky="w")

    def create_status_circle(self, status_frame, row):
        circle = tk.Canvas(status_frame, width=20, height=20, bg="white", highlightthickness=0)
        circle.grid(row=row, column=1, padx=10, pady=10, sticky="e")
        circle.create_oval(2, 2, 18, 18, fill="red")
        return circle

    def start_stop_toggle(self):
        # Toggle start/stop button and update text and color
        if self.start_stop_button.cget("text") == "Start":
            self.start_stop_button.configure(text="Stop", bg="red")
            self.operational_circle.create_oval(2, 2, 18, 18, fill="green")
            self.operational_status = True
        else:
            self.start_stop_button.configure(text="Start", bg="green")
            self.operational_circle.create_oval(2, 2, 18, 18, fill="red")
            self.operational_status = False
    def debug(self):
        # Print debug message
        print("Debug button clicked")

    def edit_wiring(self):
        # Edit wiring text
        self.wiring_text.delete("1.0", "end")
        self.wiring_text.insert("end", "Wiring:\n")

    def edit_info(self):
        # Edit info text
        self.info_text.delete("1.0", "end")
        self.info_text.insert("end", "Info:\n")

if __name__ == '__main__':
    app = ControlPanel()
    app.mainloop()
