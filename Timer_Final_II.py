# from tkinter import *
from customtkinter import *
from time import *
from tkinter import *
import time
import math



class Timer:
    def __init__(self, window):
        self.window = window
        self.window.title("Clock")
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"700x400+{(self.screen_width//3)}+{self.screen_height//4}")

        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 1)
        self.window.rowconfigure(0, weight = 1)
        self.running = False
        self.time_left = 0  # Total time left in seconds


        self.time_frame = CTkFrame(self.window) # , fg_color=  "black")
        self.time_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.time_frame.columnconfigure(0, weight = 1)
        self.time_frame.rowconfigure(3, weight = 1)


        self.time_label = CTkLabel(self.time_frame, text="00:00:00", font=("Arial", 50), bg_color = "White", text_color="black")
        self.time_label.grid(row=0, column=0, sticky="nsew")

        self.entry_frame = CTkFrame(master = self.time_frame, fg_color="#2D2D2D")
        self.entry_frame.grid(row = 2, column = 0, sticky = "nsew", pady = 20)

        # Define placeholder logic
        def on_focus_in(entry, placeholder):
            if entry.get() == placeholder:
                entry.delete(0, "end")  # Clear the placeholder
                entry.configure(fg_color="black")  # Set text color to black

        def on_focus_out(entry, placeholder):
            if entry.get() == "":  # If entry is empty, restore the placeholder
                entry.insert(0, placeholder)
                entry.configure(fg_color="gray")  # Set text color to gray

        # Configure the frame grid for balanced alignment
        self.entry_frame.grid_rowconfigure(0, weight=1)  # Space above entries
        self.entry_frame.grid_rowconfigure(2, weight=1)  # Space below entries
        self.entry_frame.grid_columnconfigure(0, weight=1)  # Space to the left of entries
        self.entry_frame.grid_columnconfigure(1, weight=0)  # First entry column
        self.entry_frame.grid_columnconfigure(2, weight=0)  # Spacer between first and second
        self.entry_frame.grid_columnconfigure(3, weight=0)  # Second entry column
        self.entry_frame.grid_columnconfigure(4, weight=0)  # Spacer between second and third
        self.entry_frame.grid_columnconfigure(5, weight=0)  # Third entry column
        self.entry_frame.grid_columnconfigure(6, weight=1)  # Space to the right of entries

        # Hour entry
        self.hour_entry = CTkEntry(master=self.entry_frame, bg_color="White", text_color="white", placeholder_text = "HH", placeholder_text_color = "white")
        self.hour_entry.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        # Minute entry
        self.minute_entry = CTkEntry(master=self.entry_frame, bg_color="White", text_color="white", placeholder_text_color="white", placeholder_text="MM")
        self.minute_entry.grid(row=1, column=3, padx=20, pady=10, sticky="nsew")

        # Second entry
        self.second_entry = CTkEntry(master=self.entry_frame, bg_color="White", text_color="white", placeholder_text_color="white", placeholder_text="SS")
        self.second_entry.grid(row=1, column=5, padx=20, pady=10, sticky="nsew")


        self.window.bind("<Configure>", self.adjust_layout_debounce)

        self.button_frame = CTkFrame(master = self.window, border_width=5, corner_radius=0, fg_color = "#242124" ) # fg_color = "black",
        self.button_frame.grid(row = 0, column = 1, sticky="nsew")

        self.button_frame.columnconfigure(0, weight = 1)

        self.clock = CTkButton(master = self.button_frame, text = "Clock",font=("Arial", 24), fg_color ="#242124", # fg_color = "#FFA500", text_color = "black",
                               height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(), # hover_color = "#cd5700", border_color="White",
                               corner_radius=0, anchor = "w", border_width=0, hover_color = "#cd5700", command = self.open_clock)
        self.clock.grid(row = 0, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.stopwatch = CTkButton(master = self.button_frame, text = "Stopwatch",font=("Arial", 24), fg_color = "#242124",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, anchor = "w", command= self.open_stopwatch,border_width = 0)
        self.stopwatch.grid(row = 2, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.timer = CTkButton(master = self.button_frame, text = "Timer",font=("Arial", 24), fg_color = "#cd5700", anchor = "w",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, border_width=0, command = self.open_timer)
        self.timer.grid(row = 1, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.world_clock = CTkButton(master = self.button_frame, text = "World Clock",font=("Arial", 24), anchor = "w",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, fg_color = "#242124" , border_width=0, command = self.open_world_clock)
        self.world_clock.grid(row = 3, column = 0, sticky="nsew", padx = 20, pady = 10)

        # Start, Stop, Reset Button Frame
        self.button_frame2 = CTkFrame(master = self.time_frame, fg_color = "#2D2D2D")
        self.button_frame2.grid(row = 3, column = 0)

        self.start_button = CTkButton(master = self.button_frame2, text = "Start", fg_color = "#cd5700", command = self.start_timer)
        self.start_button.grid(row = 0, column = 0, padx = 20)

        self.stop_button = CTkButton(master = self.button_frame2, text = "Stop", fg_color = "#cd5700", command = self.stop_timer)
        self.stop_button.grid(row = 0, column = 1, padx = 20)

        self.reset_button = CTkButton(master = self.button_frame2, text = "Reset", fg_color = "#cd5700", command = self.reset_timer)
        self.reset_button.grid(row = 0, column = 2, padx = 20)


    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            formatted_time = self.format_time(self.time_left)

            # Only update the label if the text has changed
            if self.time_label.cget("text") != formatted_time:
                self.time_label.configure(text=formatted_time)

            # Schedule next update
            self.window.after(1000, self.update_timer)

        elif self.time_left == 0 and self.running:
            self.running = False
            self.time_label.configure(text="Time's up!")
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            self.reset_button.configure(state="normal")


    def start_timer(self):
        if not self.running:
            try:
                # Fetch time input from entries on first start
                if self.time_left == 0:
                    hours = int(self.hour_entry.get()) if self.hour_entry.get().isdigit() else 0
                    minutes = int(self.minute_entry.get()) if self.minute_entry.get().isdigit() else 0
                    seconds = int(self.second_entry.get()) if self.second_entry.get().isdigit() else 0
                    self.time_left = hours * 3600 + minutes * 60 + seconds

                if self.time_left <= 0:
                    raise ValueError("Invalid time input!")

                self.running = True
                self.time_label.configure(text=self.format_time(self.time_left))
                self.start_button.configure(state="disabled")
                self.stop_button.configure(state="normal")
                self.reset_button.configure(state="disabled")
                self.update_timer()

            except ValueError:
                self.time_label.configure(text="Invalid input!")

    def stop_timer(self):
        if self.running:
            self.running = False
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            self.reset_button.configure(state="normal")


    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.time_label.configure(text="0:00:00")
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.reset_button.configure(state="disabled")


    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"



    def adjust_layout(self, event = None):
        # Adjust font size based on window size
        current_width = self.window.winfo_width()
        current_height = self.window.winfo_height()
        font_size = max(12, (current_width + current_height) // 30)
        self.time_label.configure(font=("Arial", font_size * 2))
        self.time_label.grid(pady = 10)
        self.hour_entry.configure(font=("Arial", font_size))
        self.minute_entry.configure(font=("Arial", font_size))
        self.second_entry.configure(font=("Arial", font_size))
        self.hour_entry.configure(width = font_size * 2)
        self.minute_entry.configure(width = font_size * 2)
        self.second_entry.configure(width = font_size * 2)
        self.hour_entry.grid(padx = font_size//2, pady = font_size//2)
        self.minute_entry.grid(padx = font_size//2, pady = font_size//2)
        self.second_entry.grid(padx = font_size//2, pady = font_size//2)

        # Buttons in Button_Frame2
        self.start_button.configure(font =  ("Arial", font_size))
        self.stop_button.grid(padx = font_size//2)
        self.stop_button.grid(padx = font_size//2)
        self.stop_button.grid(padx = font_size//2)
        self.stop_button.configure(font =  ("Arial", font_size))
        self.reset_button.configure(font = ("Arial", font_size))

        # Button in Button_Frame1
        self.clock.configure(font = ("Arial", font_size//2))
        self.button_frame.configure(border_width = font_size//10)
        self.stopwatch.configure(font = ("Arial", font_size//2))
        self.timer.configure(font = ("Arial", font_size//2))
        self.world_clock.configure(font=("Arial", font_size // 2))


    def adjust_layout_debounce(self, event=None):
        if hasattr(self, "_layout_adjust_scheduled") and self._layout_adjust_scheduled:
            self.window.after_cancel(self._layout_adjust_scheduled)

        self._layout_adjust_scheduled = self.window.after(200, self.adjust_layout)


    def open_clock(self):
        from Front_Final import First_page
        First_page(self.window)


    def open_timer(self):
        Timer(self.window)

    def open_stopwatch(self):
        from Stopwatch_Final import Timer
        Timer(self.window)

    def open_world_clock(self):
        from World_Clock import World_Clock
        World_Clock(self.window)



if __name__ == "__main__":
    window = CTk()
    first_page = Timer(window)
    window.mainloop()
