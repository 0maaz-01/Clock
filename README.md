
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


### Resizing the App
- The app automatically adjusts its font size and layout to maintain usability at different screen sizes. This ensures that no matter how large or small you resize the window, the buttons, clocks, and input fields will remain readable and easy to interact with.

<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Resizable1.png" width="600" height="400">
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Resizable2.png" width="600" height="400">
<img src="https://github.com/0maaz-01/Clock/blob/main/Images/Resizable3.png" width="600" height="400">


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



### Running the Application

To run the application, execute the following script:

```bash
python timer_app.py
```

This will launch the GUI, and you can interact with the timer, stopwatch, and clock features. You can resize the window and the UI components will adjust automatically.







### Contributing

Feel free to modify and extend this project as you wish! Enjoy exploring time zones and building useful applications!

### License

This project is open-source and available under the MIT License - see the [LICENSE](LICENSE) file for details.


