# from tkinter import *
from customtkinter import *
from time import *
from tkinter import *
import time
import math


class First_page:
    def __init__(self, window):
        self.window = window
        self.window.title("Clock")
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"700x400+{(self.screen_width//3)}+{self.screen_height//4}")

        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 1)
        self.window.rowconfigure(0, weight = 1)


        self.time_frame = CTkFrame(self.window) # , fg_color=  "black")
        self.time_frame.grid(row = 0, column = 0, sticky = "nsew")
        # self.time_frame.rowconfigure(0, weight = 1)
        # self.time_frame.rowconfigure(1, weight=1)
        # self.time_frame.rowconfigure(2, weight=1)
        self.time_frame.columnconfigure(0, weight = 1)
        # self.time_frame.rowconfigure(1, weight = 1)
        # self.time_frame.rowconfigure(2, weight = 1)
        self.time_frame.rowconfigure(3, weight = 1)



        self.time_label = CTkLabel(self.time_frame, text="", font=("Arial", 24))
        self.time_label.grid(row=0, column=0, sticky="nsew")

        # self.day_label = CTkLabel(self.time_frame, text="", font=("Arial", 24))
        # self.day_label.grid(row=1, column=0, sticky="nsew")

        self.date_string = CTkLabel(self.time_frame, text="", font=("Arial", 24))
        self.date_string.grid(row=2, column=0, sticky="nsew")

#        self.button = CTkButton(self.dynamic_frame, text="Dynamic Button", command=self.button_action)
#        self.button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.update()
        self.window.bind("<Configure>", self.adjust_layout)

        self.button_frame = CTkFrame(master = self.window, border_width=5, corner_radius=0, fg_color = "#242124" ) # fg_color = "black",
        self.button_frame.grid(row = 0, column = 1, sticky="nsew")

        self.button_frame.columnconfigure(0, weight = 1)

        self.clock = CTkButton(master = self.button_frame, text = "Clock",font=("Arial", 24), fg_color = "#cd5700", # fg_color = "#FFA500", text_color = "black",
                               height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(), # hover_color = "#cd5700", border_color="White",
                               corner_radius=0, anchor = "w", border_width=0, hover_color = "#cd5700", command = self.open_clock)
        self.clock.grid(row = 0, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.stopwatch = CTkButton(master = self.button_frame, text = "Stopwatch",font=("Arial", 24), fg_color = "#242124",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, anchor = "w", border_width = 0, command = self.open_stopwatch)
        self.stopwatch.grid(row = 2, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.timer = CTkButton(master = self.button_frame, text = "Timer",font=("Arial", 24), fg_color = "#242124", anchor = "w", command = self.open_timer,
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, border_width=0)
        self.timer.grid(row = 1, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.world_clock = CTkButton(master = self.button_frame, text = "World Clock",font=("Arial", 24), anchor = "w",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, fg_color = "#242124" , border_width=0, command = self.open_world_clock)
        self.world_clock.grid(row = 3, column = 0, sticky="nsew", padx = 20, pady = 10)

        # Create a canvas to draw the clock
        self.canvas = Canvas(self.time_frame, background="#2D2D2D", bd=0, height = 370, relief=RIDGE)
        self.canvas.grid(row = 3, column = 0, sticky = "nsew")


        # Update the clock when the window is resized
        self.time_frame.bind("<Configure>", self.update_clock)

        # Start updating the clock
        self.update_clock()

    def update(self):
        time_string =  strftime("%I: %M: %S %p")
        self.time_label.configure(text = time_string)

        # day_string = strftime("%A")
        # self.day_label.configure(text=day_string)

        date_string = strftime("%d %B %Y")
        self.date_string.configure(text=date_string)

        self.window.after(1000, self.update)


    def adjust_layout(self, event = None):
        # Adjust font size based on window size
        current_width = self.window.winfo_width()
        current_height = self.window.winfo_height()
        font_size = max(12, (current_width + current_height) // 30)
        self.time_label.configure(font=("Arial", font_size))
        # self.day_label.configure(font=("Arial", font_size))
        self.date_string.configure(font=("Arial", font_size//2))
        self.clock.configure(font = ("Arial", font_size//2))
        self.button_frame.configure(border_width = font_size//10)
        self.stopwatch.configure(font = ("Arial", font_size//2))
        self.timer.configure(font = ("Arial", font_size//2))
        self.world_clock.configure(font=("Arial", font_size // 2))



    def draw_circle(self, center_x, center_y, radius):
        """Draw the clock face."""
        self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="#cd5700", width=10)

        # Draw hour markers
        for i in range(12):
            angle = math.radians(i * 30)  # Each hour is 30 degrees
            x1 = center_x + radius * 0.9 * math.cos(angle)
            y1 = center_y - radius * 0.9 * math.sin(angle)
            x2 = center_x + radius * 0.8 * math.cos(angle)
            y2 = center_y - radius * 0.8 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="white", width=8)


    def draw_hand(self, center_x, center_y, length, width, angle, color):
        """Draw a clock hand."""
        angle = math.radians(angle)
        x = center_x + length * math.cos(angle)
        y = center_y - length * math.sin(angle)  # Use + for y to reverse direction
        self.canvas.create_line(center_x, center_y, x, y, fill=color, width=width+2)


    def update_clock(self, event=None):
        """Update the clock hands based on the current time."""
        # Get the center and radius based on canvas size
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x, center_y = width / 2, height / 2
        radius = min(width, height) / 2.5  # Radius is 2.5 times smaller than the smaller dimension of the window

        self.canvas.delete("all")  # Clear the canvas
        self.draw_circle(center_x, center_y, radius)  # Redraw the clock face

        # Get the current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate the angles for the clock hands
        hour_angle = (hours + minutes / 60) * 30 - 90
        minute_angle = (minutes + seconds / 60) * 6 - 90
        second_angle = seconds * 6 - 90

        # Reverse direction of the angles
        hour_angle = -hour_angle
        minute_angle = -minute_angle
        second_angle = -second_angle


        # Draw the clock hands
        self.draw_hand(center_x, center_y, radius * 0.5,6, hour_angle, "white")  # Hour hand
        self.draw_hand(center_x, center_y, radius * 0.7, 4, minute_angle,"#FFDB58")  # Minute hand
        self.draw_hand(center_x, center_y, radius * 0.8, 2, second_angle, "red")  # Second hand

        # Schedule the next update
        self.window.after(1000, self.update_clock)


    def open_timer(self):
        from Timer_Final_II import Timer
        Timer(self.window)

    def open_stopwatch(self):
        from Stopwatch_Final import Timer
        Timer(self.window)

    def open_world_clock(self):
        from World_Clock import World_Clock
        World_Clock(self.window)

    def open_clock(self):
        First_page(self.window)


if __name__ == "__main__":
    window = CTk()
    first_page = First_page(window)
    window.mainloop()
