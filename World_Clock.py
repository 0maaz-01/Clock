# from tkinter import *
from customtkinter import *
from City_III import cities_list, coordinate_map
import tkinter as tk
from Digital_Clock import DigitalClock

class World_Clock:
    def __init__(self, window):
        self.window = window
        self.window.title("Clock")
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"700x400+{(self.screen_width // 3)}+{self.screen_height // 4}")

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.time_frame = CTkFrame(self.window)  # , fg_color=  "black")
        self.time_frame.grid(row=0, column=0, sticky="nsew")
        self.clocks = []

        self.window.bind("<Configure>", self.adjust_layout)


        # Button Frame
        self.button_frame = CTkFrame(master = self.window, border_width=5, corner_radius=0, fg_color = "#242124" ) # fg_color = "black",
        self.button_frame.grid(row = 0, column = 1, sticky="nsew")

        self.clock = CTkButton(master = self.button_frame, text = "Clock",font=("Arial", 24), fg_color = "#242124", # fg_color = "#FFA500", text_color = "black",
                               height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(), # hover_color = "#cd5700", border_color="White",
                               corner_radius=0, anchor = "w", border_width=0, hover_color = "#cd5700", command = self.open_clock)
        self.clock.grid(row = 0, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.stopwatch = CTkButton(master = self.button_frame, text = "Stopwatch",font=("Arial", 24), fg_color = "#242124",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, anchor = "w", border_width = 0, command = self.open_stopwatch)
        self.stopwatch.grid(row = 2, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.timer = CTkButton(master = self.button_frame, text = "Timer",font=("Arial", 24), fg_color = "#242124", anchor = "w",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, border_width=0, command = self.open_timer)
        self.timer.grid(row = 1, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.world_clock = CTkButton(master = self.button_frame, text = "World Clock",font=("Arial", 24), anchor = "w", fg_color="#cd5700",
                               text_color = "white", height = self.button_frame.winfo_height()//2,width = self.button_frame.winfo_width(),
                               hover_color = "#cd5700", corner_radius=0, border_width=0, command = self.open_world_clock)
        self.world_clock.grid(row = 3, column = 0, sticky="nsew", padx = 20, pady = 10)

        self.city_frame = CTkScrollableFrame(master = self.time_frame, fg_color="black")
        self.city_frame.grid(row = 1, column = 0, padx = 40, sticky = "nsew")



        # World Clock
        self.search_frame = CTkFrame(master=self.time_frame, fg_color = "#2D2D2D")
        self.search_frame.grid(row=0, column=0, sticky="nsew")


        self.add_button = CTkButton(master=self.search_frame, text="add", corner_radius=10, fg_color="#cd5700", command = self.add)
        self.add_button.grid(row=0, column=1)


        # The list that will be displayed on the screen.
        self.cities = set()

        self.words = []

        self.search_entry = CTkEntry(master=self.search_frame, text_color="white",  #########
                                     placeholder_text="Enter city name or country...", corner_radius=10)  #########
        self.search_entry.grid(row=0, column=0, sticky="w", padx=20)

        self.suggestions_list = tk.Listbox(master=self.window, height = self.time_frame.winfo_height() // 2)  #########
        self.search_entry.bind("<KeyRelease>", self.update_suggestions)
        self.suggestions_list.bind("<<ListboxSelect>>", self.select_suggestion)

        self.city_frame.bind("<Configure>", self.on_resize)


    def update_suggestions(self, event):  ####
        query = self.search_entry.get().lower()

        matching_suggestions = [word for word in cities_list if word.startswith(query)]

        if query and matching_suggestions:
            self.suggestions_list.delete(0, tk.END)

            for suggestion in matching_suggestions:
                self.suggestions_list.insert(tk.END, suggestion)

            self.suggestions_list.place(x=self.search_entry.winfo_x(),
                                        y=self.search_entry.winfo_y() + self.search_entry.winfo_height(),
                                        width=self.search_entry.winfo_width())

        else:
            self.suggestions_list.place_forget()



    def select_suggestion(self, event):
        selected = self.suggestions_list.get(self.suggestions_list.curselection())
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, selected)
        self.suggestions_list.place_forget()



    def add(self):
        city_name = self.search_entry.get()

        if city_name in coordinate_map:
            if city_name not in self.cities:
                self.cities.add(city_name)

                latitude, longitude = coordinate_map[city_name]

                row = len(self.cities)

                clock = DigitalClock(self.city_frame, latitude, longitude, row, city_name)
                self.clocks.append(clock)


    def on_resize(self, event):
        """Handle window resizing events."""
        new_font_size = max(12, self.city_frame.winfo_width() // 30)
        self.resize_all_clocks(new_font_size)


    def resize_all_clocks(self, font_size):
        """Resize all clock labels to the specified font size."""
        for clock in self.clocks:
            clock.resize(font_size)


    def adjust_layout(self, event = None):
        # Adjust font size based on window size
        current_width = self.window.winfo_width()
        current_height = self.window.winfo_height()
        font_size = max(12, (current_width + current_height) // 30)
        self.clock.configure(font = ("Arial", font_size//2))
        self.button_frame.configure(border_width = font_size//10)
        self.stopwatch.configure(font = ("Arial", font_size//2))
        self.timer.configure(font = ("Arial", font_size//2))
        self.world_clock.configure(font=("Arial", font_size // 2))
        self.search_entry.configure(width = font_size * 7, height = font_size, font = ("Aerial",font_size//2))   ####
        self.search_entry.grid(padx = (font_size - (font_size//2)), pady = (font_size - (font_size//2)))  #####
        self.add_button.configure(font = ("Arial", font_size//2))
#        self.cities_frame.configure(height = font_size * 6, width = font_size * 10)
        self.suggestions_list.configure(font = ("Aerial", font_size//2), height = font_size * 6)
        self.city_frame.configure(height = font_size * 6, width = font_size * 10)


    def open_timer(self):
        from Timer_Final_II import Timer
        Timer(self.window)

    def open_stopwatch(self):
        from Stopwatch_Final import Timer
        Timer(self.window)

    def open_world_clock(self):
        World_Clock(self.window)

    def open_clock(self):
        from Front_Final import First_page
        First_page(self.window)



if __name__ == "__main__":
    window = CTk()
    first_page = World_Clock(window)
    window.mainloop()
