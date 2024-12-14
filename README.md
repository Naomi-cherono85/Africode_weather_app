# Africode_weather_app
**Weather App**
This is a simple weather application built using Flask that allows users to request weather data for a specific city and country. The weather data is fetched using a weather API (via the get_requested_weather function).

**Features**
Input city and country to retrieve weather data.
Displays temperature, humidity, and other weather details.
Built using Flask, a lightweight Python web framework.

**Requirements**
Make sure you have the following installed:
*Python 3.7+
Flask*

Any dependencies required by the get_requested_weather function (such as a weather API client).
Installation
**Clone the repository to your local machine**: *git clone https://github.com/yourusername/weather-app.git*

Navigate into the project directory: cd weather-app

**Set up a virtual environment**: *python -m venv env*

Activate the virtual environment:

**On Windows**: *env\Scripts\activate*
**On Mac/Linux**: *source env/bin/activate*
**Install the required dependencies**: *pip install -r requirements.txt*

Usage
To run the application, use the following command:
*python app.py*

Once the server is running, you can access the app by navigating to http://127.0.0.1:8000/ in your browser.

The index() route:
Handles both GET and POST requests.
When POST is submitted, it calls the get_requested_weather(city, country) function to fetch the weather data for the provided city and country.
If the data is retrieved successfully, it is displayed in the index.html template.
If no data is found, it returns None.

 **File Structure**
weather-app/
│
├── app.py           # Main Flask application
├── weather.py       # Contains the `get_requested_weather` function
├── templates/
│   └── index.html   # HTML template for the weather form and data display
└── requirements.txt # Project dependencies
Template: index.html

**The index.html template includes:**
A form for users to input the city and country.
Displays the weather data, such as temperature, humidity, etc., once available.

**License**
This project is licensed under the MIT License.
