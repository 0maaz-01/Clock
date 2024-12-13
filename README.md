
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
- **Timer**: Set a custom countdown timer.
- **Stopwatch**: Start, stop, and reset the stopwatch.
- **World Clock**: Add cities and view their current time across various time zones.
- **Digital Clock**: Shows the current time in a digital format for any selected city.

### Requirements
- Python 3.x
- `customtkinter` library
- `tkinter` library (comes pre-installed with Python)

### Features in Detail

#### 1. Timer:
The timer allows users to input hours, minutes, and seconds, and then countdown until the time is up. It also includes **Start**, **Stop**, and **Reset** buttons. 
- **Resizable UI**: The layout and font sizes adjust based on the size of the window, making the timer display easy to read at any screen size.

#### 2. Stopwatch:
Start, pause, and reset a stopwatch. The app's interface is simple and straightforward, with buttons to control the stopwatch's operation.

#### 3. World Clock:
View current times in multiple cities around the world. 
- **Add cities**: Search for cities by name, and add them to your list of monitored cities.
- **Resizable UI**: The world clock interface adjusts based on the window size, and each city's clock will resize to ensure readability.

#### 4. Digital Clock:
Displays the current time in a digital format for each added city. The app shows the local time in various global locations.

### Resizable User Interface
This app supports resizing. The interface adjusts its layout, font sizes, and clock displays based on the size of the window. This ensures a responsive design that looks great on any screen size.

---

### How to Use
1. Run the application by executing `main.py` or the corresponding script for the clock functionality you want to use.
2. Use the **Timer**, **Stopwatch**, **World Clock**, and **Digital Clock** features by clicking on the buttons in the interface.
3. In **World Clock**, search for and add cities to monitor their time. The interface will automatically adjust to accommodate the new clocks.

---

### Resizing the App
- The app automatically adjusts its font size and layout to maintain usability at different screen sizes. This ensures that no matter how large or small you resize the window, the buttons, clocks, and input fields will remain readable and easy to interact with.


Here's the information for the README file based on the provided code.

---

### Timer Application with Tkinter and CustomTkinter

This project is a simple timer application built using Python's Tkinter library and the `customtkinter` package. The application features a Timer, Stopwatch, and Clock along with a World Clock functionality. The user interface (UI) is designed with a modern and minimalistic approach, where the user can interact with the timer using input fields for hours, minutes, and seconds.

### Features

- **Timer**: Users can input hours, minutes, and seconds to start a countdown timer. The timer counts down and displays the remaining time in a `hh:mm:ss` format. The user can start, stop, or reset the timer.
  
- **Stopwatch**: The stopwatch allows users to start, stop, and reset a stopwatch that tracks elapsed time in a `mm:ss:ms` format.

- **Clock**: The clock displays the current time in a `hh:mm:ss` format and remains visible on top of other windows.

- **World Clock**: Displays time for different time zones worldwide.

### Installation Requirements

1. **Python** (Version 3.x recommended)
2. **customtkinter**: Install using pip:
   ```bash
   pip install customtkinter
   ```
3. **Tkinter**: Tkinter is typically included with Python, but if needed, install it using:
   ```bash
   pip install tk
   ```

### Running the Application

To run the application, execute the following script:

```bash
python timer_app.py
```

This will launch the GUI, and you can interact with the timer, stopwatch, and clock features. You can resize the window and the UI components will adjust automatically.

### Application Breakdown

1. **Window Layout**:
   - The main window is a `CTk` object (CustomTkinter's main window).
   - A large frame (`time_frame`) contains the display for the timer and inputs for setting the timer.
   - A secondary frame (`button_frame`) includes buttons for navigating between features like Timer, Stopwatch, World Clock, and Clock.

2. **Timer Functionality**:
   - The user can enter the desired time in hours, minutes, and seconds.
   - Clicking "Start" begins the countdown, and the "Stop" button pauses it.
   - When the timer reaches zero, it stops automatically and displays "Time's up!".
   - The "Reset" button restores the timer to its initial state.

3. **Stopwatch Functionality**:
   - The stopwatch allows users to start, stop, and reset the elapsed time.
   - The stopwatch displays the elapsed time in a `mm:ss:ms` format.

4. **Clock**:
   - The clock is displayed continuously with the current time, updating in real-time.

5. **World Clock**:
   - A feature that shows the time for different locations around the world (needs to be defined in the relevant module `World_Clock`).

### Customization

- **Font Size Adjustment**: The font sizes of labels, buttons, and entries automatically adjust based on the window size to ensure readability.
  
- **Layout Adjustment**: The layout is responsive, with elements adjusting according to the window size. This is implemented through the `adjust_layout()` method that dynamically adjusts the fonts and positions of the widgets.

### Code Overview

The application uses a class structure, with the `Timer` class managing the timer, stopwatch, and clock functionalities. Each component is responsible for specific interactions, such as starting and stopping the timer, and updating the display.

- **Main Components**:
  - **CTkLabel**: Used for displaying time and status messages.
  - **CTkButton**: Buttons for interacting with the timer, stopwatch, clock, and world clock.
  - **CTkEntry**: Entry fields for inputting the hours, minutes, and seconds for the timer.
  - **CTkFrame**: Frames to organize the layout.

- **Methods**:
  - `start_timer`: Starts the countdown based on user input.
  - `stop_timer`: Stops the countdown.
  - `reset_timer`: Resets the timer to the initial state.
  - `update_timer`: Updates the timer display every second.
  - `format_time`: Formats the time in `hh:mm:ss` format.

### File Structure

- `timer_app.py`: The main application script with the timer, stopwatch, and clock functionalities.
- `Stopwatch_Final.py`: Contains the Stopwatch functionality.
- `World_Clock.py`: Contains the World Clock functionality.
- `Front_Final.py`: Contains the main page layout and initialization code.

### Contributing

Feel free to fork this repository, submit issues, and open pull requests. Any improvements or new feature suggestions are welcome!

### License

This project is open-source and available under the MIT License.

---

Let me know if you need further adjustments!



Here's the README file for the code you've provided:

---

# Digital Clock App

## Overview
This project is a **Digital Clock App** with multiple functionalities such as a stopwatch, timer, world clock, and analog clock display. The app is designed using Python with the `CustomTkinter` library to create a sleek and modern user interface, offering a customizable and interactive experience.

## Features
- **Digital Clock**: Displays the current time in real-time with a modern design.
- **Analog Clock**: Visualizes the time using a traditional clock face with moving hands.
- **Stopwatch**: Includes a stopwatch feature for time tracking.
- **Timer**: Allows you to set countdown timers.
- **World Clock**: Display the time for different cities around the world.
- **Responsive Layout**: Automatically adjusts the layout and font size based on the window size.

## Technologies Used
- **Python**: The programming language used for the app.
- **CustomTkinter**: A modern version of Tkinter that allows for custom widgets and an improved interface.
- **Time**: The Python `time` module is used for managing time and updates.
- **Math**: For calculating angles to draw the clock hands.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Install the necessary dependencies using `pip`:

   ```bash
   pip install customtkinter
   ```

3. Run the Python script to launch the app:

   ```bash
   python your_script_name.py
   ```

## Usage

- The main screen displays the **Digital Clock** along with buttons for different features like **Stopwatch**, **Timer**, **World Clock**, and **Analog Clock**.
- Each button opens its respective feature in a new window.
- The **Analog Clock** is updated in real-time with moving hour, minute, and second hands.
- The **Timer** and **Stopwatch** features allow you to set countdowns or measure time respectively.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy exploring this app! Feel free to modify and expand the functionality as needed.

---

This README is now complete with the description, instructions, and code structure for your project!





# Digital Clock App

## Overview
This project is a **Digital Clock App** that displays the current time for a specific city based on its geographical coordinates (latitude and longitude). The app allows you to easily see the time in different locations around the world with support for automatic time zone detection.

## Features
- **City-specific Time**: Displays the time for a city based on its geographical coordinates (latitude and longitude).
- **Time Zone Detection**: Automatically detects the time zone for the given latitude and longitude using the `timezonefinder` library.
- **Customizable Display**: The font size of the clock can be resized based on your preference.
- **Live Updates**: The clock updates every second to show the real-time clock.

## Technologies Used
- **Python**: Programming language used for the app.
- **CustomTkinter**: A modern interface library based on Tkinter to create the user interface.
- **pytz**: A Python library for time zone support.
- **timezonefinder**: A library that allows you to find the timezone for a given latitude and longitude.
- **datetime**: A Python module for handling date and time.

## How It Works
- The app takes the latitude and longitude of a city and finds its timezone using the `TimezoneFinder` library.
- The app then fetches the current time in that timezone using the `pytz` library and updates the clock every second.
- The clock is displayed in a simple, easy-to-read format, showing both the city name and the current time.

## Installation

1. Clone this repository to your local machine:

   ```
   git clone <repository_url>
   ```

2. Install the necessary dependencies using `pip`:

   ```
   pip install customtkinter pytz timezonefinder
   ```

3. Run the Python script to launch the app.

## Usage

- Initialize the `DigitalClock` class with the root window of your Tkinter app, the latitude and longitude of the desired city, the row in the grid where the clock should be placed, and the name of the city.
  
  Example:
  ```python
  root = CTk()  # Create the main Tkinter window
  clock = DigitalClock(root, latitude=40.7128, longitude=-74.0060, row=0, city_name="New York")
  root.mainloop()
  ```

- You can resize the clock by calling the `resize()` method with a new font size:
  ```python
  clock.resize(20)  # Resize the clock to a font size of 20
  ```

## Code Structure

- `DigitalClock` Class: This is the main class that handles the clock functionality. It initializes the clock with the city’s timezone and updates the clock every second.
  
  ### Methods:
  - **`__init__`**: Initializes the clock with the given parameters (root window, latitude, longitude, city name).
  - **`resize`**: Resizes the font of the clock.
  - **`update_clock`**: Updates the clock every second to reflect the current time in the specified city.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify and extend this project as you wish! Enjoy exploring time zones and building useful applications!








## Resizablity of pages. 
![image at](https://github.com/0maaz-01/Clock/blob/main/Images/Resizable1.png)
![image at](https://github.com/0maaz-01/Clock/blob/main/Images/Resizable2.png)
![image at](https://github.com/0maaz-01/Clock/blob/main/Images/Resizable3.png)
