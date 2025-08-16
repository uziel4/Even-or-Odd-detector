"""
Author: Uziel E. Santos 
Description: A simple weather application using PyQt5 and OpenWeatherMap API.
Date: 2025/08/16
"""

# Import the sys module for system-specific parameters and functions
import sys

# Import the requests library to make HTTP requests to the weather API
import requests

# Import necessary PyQt5 widgets for building the GUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

# Import Qt core functionalities (e.g., alignment, event handling)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    """
    Main widget for the Weather Application.
    Handles UI setup, user input, API requests, and display of weather data.
    """
    def __init__(self):
        """
        Initializes the WeatherApp widget, sets up UI elements and layout.
        """
        super().__init__()
        # Label prompting user to enter city name
        self.city_label = QLabel("Enter City:",self)
        # Input field for city name
        self.city_input = QLineEdit(self)
        # Button to trigger weather fetch
        self.get_weather_button = QPushButton("Get Weather", self)
        # Label to display temperature
        self.temperature_label = QLabel( self)
        # Label to display weather emoji
        self.emoji_label = QLabel( self)
        # Label to display weather description
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        """
        Configures the UI layout, widget properties, and styles.
        """
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        # Add widgets to the vertical layout
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Center align all labels and input
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)    

        # Set object names for styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")         
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Apply custom stylesheet for fonts and sizes
        self.setStyleSheet("""
            QLabel, QPushButton {
            font-family: Times New Roman;
            }
            QLabel#city_label {
            font-size: 40px; 
            font-style: italic;
            }
            QLineEdit#city_input {
            font-size: 40px; 
            }
            QPushButton#get_weather_button {
            font-size: 30px; 
            font-weight: bold;
            }
            QLabel#temperature_label {
            font-size: 75px;
            }
            QLabel#emoji_label {
            font-size: 100px;
            font-family: segoe ui emoji;
            }
            QLabel#description_label {
            font-size: 50px;
            }
        """)

        # Connect button click to weather fetch method
        self.get_weather_button.clicked.connect(self.get_weather) 

    def get_weather(self):
        """
        Fetches weather data from OpenWeatherMap API for the entered city.
        Handles errors and displays results or error messages.
        """
        api_key = "8bfff886bdbda359a365394e1b92bea4"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_err:
            # Handle specific HTTP errors with custom messages
            match response.status_code:
                case 400:
                    self.display_errors("Bad Request:\n Please check the city name.")
                case 401:
                    self.display_errors("Unauthorized:\n Please check your API key.")
                case 403:
                    self.display_errors("Forbidden:\n Access denied to the requested resource.")
                case 404:
                    self.display_errors("City not found:\n Please check the city name.")
                case 500: 
                    self.display_errors("Internal Server Error:\n Please try again later.")
                case 502:
                    self.display_errors("Bad Gateway:\n The server is down or not responding.")
                case 503:
                    self.display_errors("Service Unavailable:\n The server is currently unavailable.")  
                case 504:
                    self.display_errors("Gateway Timeout:\n The server took too long to respond.")
                case _:
                    self.display_errors(f"An error occurred:\n {http_err}")

        except requests.exceptions.ConnectionError:
            self.display_errors("Connection Error:\n Please check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_errors("Timeout Error:\n The request took too long to complete.")

        except requests.exceptions.TooManyRedirects:
            self.display_errors("Too Many Redirects:\n The URL may be incorrect or the server is misconfigured.")

        except requests.exceptions.RequestException as req_err:
            self.display_errors(f"An error occurred:\n {req_err}")
        
    def display_errors(self, error_message):
        """
        Displays error messages in the temperature label and clears other labels.
        Args:
            error_message (str): The error message to display.
        """
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(error_message)
        self.emoji_label.clear()
        self.description_label.clear()
        
    
    def display_weather(self, weather_data):
        """
        Displays weather information (temperature, emoji, description) in the UI.
        Args:
            weather_data (dict): Weather data from the API response.
        """
        self.temperature_label.setStyleSheet("font-size: 75px;")
        # Convert temperature from Kelvin to Fahrenheit
        temperature = (weather_data["main"]["temp"] - 273.15) * 9/5 + 32  # Convert from Kelvin to Fahrenheit
        weather_ID = weather_data["weather"][0]["id"]
        weather_description = weather_data["weather"][0]["description"]


        self.temperature_label.setText(f"{temperature:.0f} °F")
        self.emoji_label.setText(self.get_weather_emoji(weather_ID))
        self.description_label.setText(weather_description.capitalize())

    @staticmethod
    def get_weather_emoji(weather_ID):
        """
        Returns an emoji representing the weather condition based on weather ID.
        Args:
            weather_ID (int): Weather condition code from API.
        Returns:
            str: Emoji character.
        """
        if 200 <= weather_ID < 232:
            return "🌩️"
        elif 300 <= weather_ID < 321:
            return "🌦️"
        elif 500 <= weather_ID < 531:
            return "🌧️"
        elif 600 <= weather_ID < 622:
            return "❄️"
        elif 701 <= weather_ID < 741:
            return "🌫️"
        elif weather_ID== 762:
            return "🌋"
        elif weather_ID == 771:
            return "💨"
        elif weather_ID == 781:
            return "🌪️"
        elif weather_ID == 800:
            return "☀️" 
        elif 801 <= weather_ID <= 804:
            return "☁️" 
        else:
            return ""

# Entry point for the application. This block ensures the code runs only if the script is executed directly.
if __name__ == "__main__":
    """
    Main entry point for the Weather App.
    Initializes QApplication, creates and shows the WeatherApp widget, and starts the event loop.
    """
    # Create the main QApplication instance required for all PyQt5 applications.
    app = QApplication(sys.argv)
    # Instantiate the WeatherApp widget.
    weather_app = WeatherApp()
    # Display the WeatherApp window.
    weather_app.show()
    # Start the Qt event loop and exit the program when the window is closed.
    sys.exit(app.exec_())
