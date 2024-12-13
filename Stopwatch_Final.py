# from tkinter import *
from customtkinter import *
from time import *
import time



class Timer:
    def __init__(self, window):
        self.window = window
        self.window.title("Clock")
        self.window.attributes("-topmost", True)
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"700x400+{(self.screen_width//3)}+{self.screen_height//4}")

        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 1)
        self.window.rowconfigure(0, weight = 1)
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0


        self.time_frame = CTkFrame(self.window) # , fg_color=  "black")
        self.time_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.time_frame.columnconfigure(0, weight = 1)
        self.time_frame.rowconfigure(3, weight = 1)


        self.time_label = CTkLabel(self.time_frame, text="00:00:00", font=("Arial", 50), bg_color = "White", text_color="black")
        self.time_label.grid(row=0, column=0, sticky="nsew")

        # Define placeholder logic
        def on_focus_in(entry, placeholder):
            if entry.get() == placeholder:
                entry.delete(0, "end")  # Clear the placeholder
                entry.configure(fg_color="black")  # Set text color to black

        def on_focus_out(entry, placeholder):
            if entry.get() == "":  # If entry is empty, restore the placeholder
                entry.insert(0, placeholder)
                entry.configure(fg_color="gray")  # Set text color to gray


        # self.update()
        # self.window.bind("<Configure>", self.adjust_layout)
        self.window.bind("<Configure>", self.adjust_layout_debounce)

        self.button_frame = CTkFrame(master = self.window, border_width=5, corner_radius=0, fg_color = "#242124" ) # fg_color = "black",
        self.button_frame.grid(row = 0, column = 1, sticky="nsew")

        self.button_frame.columnconfigure(0, weight = 1)

        self.clock = CTkButton(master = self.button_frame, text = "Clock",font=("Arial", 24), fg_color ="#242124", # fg_color = "#FFA500", text_color = "black",
                               height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(), # hover_color = "#cd5700", border_color="White",
                               corner_radius=0, anchor = "w", border_width=0, hover_color = "#cd5700", command = self.open_clock)
        self.clock.grid(row = 0, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.stopwatch = CTkButton(master = self.button_frame, text = "Stopwatch",font=("Arial", 24), fg_color = "#cd5700",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, anchor = "w", border_width = 0, command = self.open_stopwatch)
        self.stopwatch.grid(row = 2, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.timer = CTkButton(master = self.button_frame, text = "Timer",font=("Arial", 24), fg_color = "#242124" , anchor = "w",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, border_width=0, command = self.open_timer)
        self.timer.grid(row = 1, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.world_clock = CTkButton(master = self.button_frame, text = "World Clock",font=("Arial", 24), anchor = "w", command = self.open_world_clock,
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, fg_color = "#242124" , border_width=0)
        self.world_clock.grid(row = 3, column = 0, sticky="nsew", padx = 20, pady = 10)

        # Start, Stop, Reset Button Frame
        self.button_frame2 = CTkFrame(master = self.time_frame, fg_color = "#2D2D2D")
        self.button_frame2.grid(row = 3, column = 0)

        self.start_button = CTkButton(master = self.button_frame2, text = "Start", fg_color = "#cd5700", command = self.start) # , command = self.start_timer)
        self.start_button.grid(row = 0, column = 0, padx = 20)

        self.stop_button = CTkButton(master = self.button_frame2, text = "Stop", fg_color = "#cd5700", command = self.stop) #, command = self.stop_timer)
        self.stop_button.grid(row = 0, column = 1, padx = 20)

        self.reset_button = CTkButton(master = self.button_frame2, text = "Reset", fg_color = "#cd5700", command = self.reset) #, command = self.reset_timer)
        self.reset_button.grid(row = 0, column = 2, padx = 20)





    def adjust_layout(self, event = None):
        # Adjust font size based on window size
        current_width = self.window.winfo_width()
        current_height = self.window.winfo_height()
        font_size = max(12, (current_width + current_height) // 30)
        self.time_label.configure(font=("Arial", font_size * 2))
        self.time_label.grid(pady = 10)


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



    def update_time(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.time_label.configure(text=formatted_time)
            self.window.after(100, self.update_time)

    def format_time(self, elapsed_time):
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 100)
        return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.time_label.configure(text="00:00:00")

    def open_clock(self):
        from Front_Final import First_page
        First_page(self.window)

    def open_timer(self):
        from Timer_Final_II import Timer
        Timer(self.window)

    def open_stopwatch(self):
        Timer(self.window)

    def open_world_clock(self):
        from World_Clock import World_Clock
        World_Clock(self.window)


if __name__ == "__main__":
    window = CTk()
    first_page = Timer(window)
    window.mainloop()
