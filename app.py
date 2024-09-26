from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'abd646a9e4683730832449064117e39a'  # Replace with your API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    city = request.args.get('city')
    weather_data = None
    if city:
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        print(response.status_code)  # Print status code for debugging
        print(response.json())       # Print response content for debugging
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': response.json().get('message', 'City not found')}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

