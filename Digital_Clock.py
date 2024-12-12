from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from customtkinter import *


class DigitalClock:
    def __init__(self, root, latitude, longitude, row, city_name):
        self.root = root
        self.city_name = city_name
        # Find the timezone based on coordinates
        self.timezone_finder = TimezoneFinder()
        self.timezone_name = self.timezone_finder.timezone_at(lat = latitude, lng = longitude)
        
        if not self.timezone_name:
            # Default to UTC if no timezone is found
            self.timezone_name = "UTC"
        
        self.timezone = timezone(self.timezone_name)

        # Create a label to display the time
        self.label = CTkLabel(root, font = ("Arial", 16), fg_color="black")
        self.label.grid(row = row, column = 0, sticky = "w")

        # Update the clock
        self.update_clock()
    #    self.root.bind("<Configure>", self.adjust)

    #def adjust(self, event = None):
    #    self.font_size = self.root.winfo_width() // 30
    #    self.label.configure(font = ("Arial", self.font_size))




    def resize(self, font_size):
        """Resize the label's font size."""
        self.label.configure(font=("Arial", font_size))

    def update_clock(self):
        # Get the current time in the specified timezone
        now = datetime.now(self.timezone)
        current_time = now.strftime("%H:%M:%S")  # Format time as HH:MM:SS
        self.label.configure(text = f"{self.city_name}: {current_time}")  # Update label text
        self.label.after(1000, self.update_clock)  # Refresh every second


'''if __name__ == "__main__":
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Digital Clock by Coordinates")
    root.geometry("600x400")  # Window size
    root.configure(bg="black")

    # Add digital clocks for specific coordinates
    # Format: latitude, longitude, x-coordinate, y-coordinate
    clock1 = DigitalClock(root, 40.7128, -74.0060, 50, 50)  # New York
    clock2 = DigitalClock(root, 51.5074, 0.1278, 50, 100)  # London
    clock3 = DigitalClock(root, 28.6139, 77.2090, 50, 150)  # Delhi

    # Start the Tkinter event loop
    root.mainloop()

'''