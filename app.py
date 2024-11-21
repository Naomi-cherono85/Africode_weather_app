from flask import Flask, render_template, request
from weather import get_requested_weather


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')
      
        weather_data = get_requested_weather(city,country)

        if weather_data:
            return render_template('index.html', weather=weather_data)
        else:
            return None
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
 