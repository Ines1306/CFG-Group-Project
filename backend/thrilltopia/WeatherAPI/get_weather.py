import requests
from datetime import datetime, timedelta
from .creating_classes import WaterActivity, NonWaterActivity


def is_valid_date(input_date):
    # Get today's date
    today = datetime.now().date()

    # Calculate the date for 15 days from today
    forecast_end_date = today + timedelta(days=14)

    try:
        # Convert input date string to datetime object
        given_date = datetime.strptime(input_date, "%Y-%m-%d").date()
        # Check if the given date is not older than today
        if given_date < today:
            return -1
        # Check if the given date is within the valid range
        if today <= given_date <= forecast_end_date:
            # Calculate the index of the given date in the forecast range
            day_index = (given_date - today).days
            return day_index
        else:
            return -1
    # In case input is not in a valid format
    except ValueError:
        return -1


def is_valid_hour(input_hour):
    try:
        hour_parts = input_hour.split(':')

        # Check if the input has two parts (hours, minutes)
        if len(hour_parts) == 2:
            hours = int(hour_parts[0])
            minutes = int(hour_parts[1])

            # Check if the input represents a valid time
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours
            else:
                return -1
        else:
            return -1
    except ValueError:
        return -1


def get_weather_for_date(appid, date, startTime):
    if is_valid_date(date) < 0:
        print("Invalid date or outside the forecast range.")
        return False, "Invalid date or outside the forecast range."
    if is_valid_hour(startTime) < 0:
        print("Invalid hour.")
        return False, "Invalid hour."

    endpoint = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/lisbon'
    payload = {
        'unitGroup': 'metric',
        'key': appid,
        'contentType': 'json',
        'startDate': date,
        'endDate': date,  # to get the weather for just one day
        'startTime': startTime
    }
    response = requests.get(url=endpoint, params=payload)

    if response.status_code == 200:
        try:
            data = response.json()
            # pp(data) --> to see the whole json response (used for debugging)
            if 'days' in data and len(data['days']) > 0:
                day_weather = data['days'][is_valid_date(date)]
                hour_day_weather = day_weather['hours'][is_valid_hour(startTime)]

                # Extract relevant weather parameters for the day and hour
                weather_summary = {
                    'hour': hour_day_weather.get('datetime'),
                    'datetime': day_weather.get('datetime'),
                    'temperature_max': day_weather.get('feelslikemax'),
                    'temperature_min': day_weather.get('feelslikemin'),
                    'temperature_at_hour': hour_day_weather.get('temp'),
                    'precipitation_probability': day_weather.get('precipprob'),
                    'wind_speed': day_weather.get('windspeed'),
                    'severe_risk': day_weather.get('severerisk')
                }
            return True, weather_summary
        except ValueError:
            print("Invalid JSON format in the response")
            return False, ({"error": "Invalid JSON format in the response"}), 500
    else:
        print("Request was unsuccessful. Status code:", response.status_code)
        return False, ({"error": "Request was unsuccessful"}), response.status_code


def get_weather(appid, date, startTime, activityID):
    # Retrieve weather information using the provided parameters
    weather_summary = get_weather_for_date(appid, date, startTime)
    if weather_summary[0] == False:
        return weather_summary[1]

    # IDs for the outdoor activities
    outdoor_activities = [1, 2, 4, 6, 8, 10, 12]
    # IDs for the outdoor water activities
    water_activities = [1, 2]

    # Convert str of activityID to int
    activityID = int(activityID)

    # Check if the activityID corresponds to an outdoor activity
    if activityID in outdoor_activities:
        # Check if the outdoor activity is also a water activity
        if activityID in water_activities:
            message = WaterActivity(weather_summary[1]).check_weather_water_activity()
        # Non water activity
        else:
            message = NonWaterActivity(weather_summary[1]).check_weather_non_water_activity()
        return message
