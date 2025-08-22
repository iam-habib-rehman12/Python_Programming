import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QHBoxLayout, QTextEdit
)
from PyQt5.QtCore import Qt
import mysql.connector
from datetime import datetime

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = "82b92291cf566eb914ace3e1b4c4ad19"
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setMinimumSize(500, 600)

        self.city_label = QLabel("Current City: ")
        self.city_input = QLabel("Detecting...")
        self.enter_city_label = QLabel("Enter City:")
        self.city_textbox = QLineEdit()
        self.city_weather_button = QPushButton("Get Weather by City")
        self.get_weather_button = QPushButton("Get Weather by Current Location")
        self.forecast_button = QPushButton("Get 2-Day Forecast")

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)

        hbox = QHBoxLayout()
        hbox.addWidget(self.enter_city_label)
        hbox.addWidget(self.city_textbox)
        layout.addLayout(hbox)

        layout.addWidget(self.city_weather_button)
        layout.addWidget(self.forecast_button)
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        self.get_weather_button.clicked.connect(self.get_weather_by_location)
        self.city_weather_button.clicked.connect(self.get_weather_by_city)
        self.forecast_button.clicked.connect(self.get_forecast_by_city)

        self.setStyleSheet("""
            QLabel, QPushButton, QLineEdit, QTextEdit {
                font-family: Cambria;
                font-size: 16px;
            }
            QPushButton {
                font-weight: bold;
            }
        """)

    def get_location_by_ip(self):
        try:
            response = requests.get("http://ip-api.com/json/")
            response.raise_for_status()
            data = response.json()
            if data["status"] == "success":
                return data["lat"], data["lon"], data["city"]
        except:
            pass
        return None, None, "Unknown"

    def get_weather_by_location(self):
        lat, lon, city = self.get_location_by_ip()
        self.city_input.setText(city)
        if lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
            self.fetch_weather(url)
        else:
            self.display_message("Could not detect location.")

    def get_weather_by_city(self):
        city = self.city_textbox.text().strip()
        if city:
            self.city_input.setText(city)
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
            self.fetch_weather(url)
        else:
            self.display_message("Please enter a city name.")

    def get_forecast_by_city(self):
        city = self.city_textbox.text().strip()
        if city:
            self.city_input.setText(city)
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}"
            self.fetch_forecast(url)
        else:
            self.display_message("Please enter a city name.")

    def fetch_weather(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            temp_k = data['main']['temp']
            temp_c = temp_k - 273.15
            desc = data['weather'][0]['description']
            weather_id = data['weather'][0]['id']
            emoji = self.get_weather_emoji(weather_id)

            message = f"Temperature: {temp_c:.0f}°C\nWeather: {desc} {emoji}"
            self.display_message(message)

        except requests.RequestException as e:
            self.display_message(f"Error fetching weather:\n{str(e)}")

            # city = self.city_input.text()
            # self.save_weather_to_db(city, temp_c)

    def fetch_forecast(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            forecast_list = data['list'][:16]  # 3-hour interval * 16 = approx. 2 days
            message = "2-Day Forecast:\n"
            for entry in forecast_list:
                dt = entry['dt_txt']
                temp_k = entry['main']['temp']
                temp_c = temp_k - 273.15
                desc = entry['weather'][0]['description']
                message += f"{dt} - {temp_c:.0f}°C, {desc}\n"

            self.display_message(message)

        except requests.RequestException as e:
            self.display_message(f"Error fetching forecast:\n{str(e)}")

    def display_message(self, message):
        self.result_area.setText(message)


    def save_weather_to_db(self, city, temp):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="root",  
                database="python_db"
            )
            cursor = conn.cursor()

            query = "INSERT INTO weather (city_name, temp, recorded_at) VALUES (%s, %s, %s)"
            values = (city, temp, datetime.now())
            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            self.display_error(f"Database Error:\n{err}")


    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
