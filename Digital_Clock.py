from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from customtkinter import *


class DigitalClock:
    def __init__(self, root, latitude, longitude, row, city_name):
        self.root = root
        self.city_name = city_name

        self.timezone_finder = TimezoneFinder()
        self.timezone_name = self.timezone_finder.timezone_at(lat = latitude, lng = longitude)
        
        if not self.timezone_name:
            self.timezone_name = "UTC"
        
        self.timezone = timezone(self.timezone_name)

        self.label = CTkLabel(root, font = ("Arial", 16), fg_color="black")
        self.label.grid(row = row, column = 0, sticky = "w")

        self.update_clock()



    def resize(self, font_size):
        self.label.configure(font=("Arial", font_size))

    def update_clock(self):
        now = datetime.now(self.timezone)
        current_time = now.strftime("%H:%M:%S")  
        self.label.configure(text = f"{self.city_name}: {current_time}")  
        self.label.after(1000, self.update_clock)  

