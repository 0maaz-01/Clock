
# Clock App

#### This application is a multifunctional clock that provides several features such as a timer, stopwatch, world clock, and a digital clock with city-specific time zones. The app is built using **Tkinter** and **CustomTkinter** for its graphical interface and functionality. It allows users to track time in multiple ways and provides a sleek, modern look.



## Graphic User Interface

#### The front page consists of a digital clock that displays the local time and an analog clock.
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Front_Page.png" width="600" height="400">

#### World Clock that allows user to search for the city and add it to the screen.
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/A.png" width="600" height="400">


#### and it also suggests the name of the cities available while typing.
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/B.png" width="600" height="400">

#### The stopwatch consists of a digital clock displaying time in the format HH:MM:SS, which represents the duration elapsed since the stopwatch started.

<img src="https://github.com/0maaz-01/Clock/blob/main/Images/StopWatch.png" width="600" height="400">

#### The timer consists of a digital clock displaying time in the format HH:MM:SS, which represents the remaining time.
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Timer.png" width="600" height="400">


## Features
- **Digital Clock**: Displays the current time in real-time with a modern design.
- **Analog Clock**: Visualizes the time using a traditional clock face with moving hands.
- **Stopwatch**: Includes a stopwatch feature for time tracking.
- **Timer**: Allows you to set countdown timers.
- **World Clock**: Display the time for different cities around the world.
- **Responsive Layout**: Automatically adjusts the layout and font size based on the window size.
- **City-specific Time**: Displays the time for a city based on its geographical coordinates (latitude and longitude).
- **Time Zone Detection**: Automatically detects the time zone for the given latitude and longitude using the `timezonefinder` library.
  


## Technologies Used
- **Python**: Programming language used for the app.
- **CustomTkinter**: A modern interface library based on Tkinter to create the user interface.
- **pytz**: A Python library for time zone support.
- **timezonefinder**: A library that allows you to find the timezone for a given latitude and longitude.
- **datetime**: A Python module for handling date and time.
- **Time**: The Python `time` module is used for managing time and updates.
- **Math**: For calculating angles to draw the clock hands.


### Resizable User Interface
This app supports resizing. The interface adjusts its layout, font sizes, and clock displays based on the size of the window. This ensures a responsive design that looks great on any screen size.

<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Resizable1.png" width="600" height="400">
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Resizable2.png" width="600" height="400">
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Resizable3.png" width="600" height="400">


### Installation Requirements

1. **Python** (Version 3.x recommended)
   
2. Clone this repository to your local machine:

3. Install the necessary dependencies using `pip`:

a) **customtkinter**:
   ```bash
   pip install customtkinter
   ```
b) **Tkinter**: Tkinter is typically included with Python, but if needed, install it using:
   ```bash
   pip install tk
   ```
c) **pytz**
   ```
   pip install pytz 
   ```
d) **timezonefinder**
   ```
   pip install pytz timezonefinder
   ```
4. Run the Python script to launch the app.


### How to Use
1. Run the application by executing `main.py` or the corresponding script for the clock functionality you want to use.
2. Use the **Timer**, **Stopwatch**, **World Clock**, and **Digital Clock** features by clicking on the buttons in the interface.
3. In **World Clock**, search for and add cities to monitor their time. The interface will automatically adjust to accommodate the new clocks.



### Contributing

Feel free to modify and extend this project as you wish! Enjoy exploring time zones and building useful applications!

### License

This project is open-source and available under the MIT License - https://github.com/0maaz-01/Clock/edit/main/LICENSE


