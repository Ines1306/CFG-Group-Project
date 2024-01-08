# PARENT CLASS
class WeatherChecker:
    def __init__(self, weather_summary):
        self.weather_summary = weather_summary

    def severe_risk_checker(self):
        severe_risk = self.weather_summary.get('severe_risk')

        if severe_risk is None or severe_risk == '':
            return "ERROR"

        # Covert severe_risk to number
        severe_risk = float(severe_risk)

        if severe_risk < 30:
            risk = "Low"
        elif 30 <= severe_risk < 70:
            risk = "Moderate"
        else:
            risk = "High"
        return risk

    def precipitation_checker(self):
        precipitation_prob = self.weather_summary.get('precipitation_probability')

        if precipitation_prob is None or precipitation_prob == '':
            return "ERROR"

        # Covert precipitation_prob to number
        precipitation_prob = float(precipitation_prob)

        if precipitation_prob == 0:
            precipit = "No"
        elif 0 < precipitation_prob < 30:
            precipit = "Low"
        elif 30 <= precipitation_prob < 60:
            precipit = "Moderate"
        else:
            precipit = "High"
        return precipit

    def wind_speed_checker(self):
        wind_speed = self.weather_summary.get('wind_speed')

        if wind_speed is None or wind_speed == '':
            return "ERROR"

        # Covert wind_speed to number
        wind_speed = float(wind_speed)

        if wind_speed < 5:
            speed = "Calm"
        elif 5 <= wind_speed < 12:
            speed = "Light"
        elif 12 <= wind_speed < 20:
            speed = "Moderate"
        elif 20 <= wind_speed < 30:
            speed = "High"
        else:
            speed = "Very high"
        return speed

    def temperature_checker(self):
        # Add logic to check temperature
        temp_max = self.weather_summary.get('temperature_max')
        temp_min = self.weather_summary.get('temperature_min')
        temp_at_hour = self.weather_summary.get('temperature_at_hour')

        if temp_max is None and temp_min is None and temp_at_hour is None:
            return "ERROR"
        if temp_max == '' and temp_min == '' and temp_at_hour == '':
            return "ERROR"
        # Covert temp_max, temp_min and temp_at_hour to number
        temp_max = float(temp_max)
        temp_min = float(temp_min)
        temp_at_hour = float(temp_at_hour)
        return temp_max, temp_min, temp_at_hour


# CHILD CLASS of WeatherChecker
class Activity(WeatherChecker):
    def __init__(self, weather_summary):
        super().__init__(weather_summary)

    def check_severe_risk(self):
        risk = self.severe_risk_checker()
        if risk == "ERROR":
            return "ERROR checking the weather", False
        elif risk == "Low":
            message = "Low risk of severe weather."
            advisable = True
        elif risk == "Moderate":
            message = "Moderate risk of severe weather. Please stay cautious and consider booking an alternative date."
            advisable = False
        elif risk == "High":
            message = "High risk of severe weather. We don't advise you to book."
            advisable = False
        else:
            message = "Severe risk data not available."
            advisable = False
        return message, advisable

    def check_temperature(self):
        temp_max, temp_min, temp_at_hour = self.temperature_checker()
        if temp_max is None and temp_min is None and temp_at_hour is None:
            return "ERROR checking the weather", False
        elif temp_at_hour < 5:
            message = f"It's going to be very cold({temp_at_hour}ºC) at the time you selected. Consider booking an alternative date."
            advisable = False
        elif temp_at_hour < 10 and temp_min < 5:
            message = f"It's going to be cold({temp_at_hour}ºC) at the time you selected. Consider booking an alternative date."
            advisable = False
        elif temp_at_hour >= 30 and temp_max >= 30:
            message = f"It's going to be very hot({temp_at_hour}ºC) at the time you selected. Consider booking an alternative date."
            advisable = False
        elif 25 <= temp_at_hour < 28 and temp_max >= 30:
            message = f"It's going to be hot({temp_at_hour}ºC) at the time you selected. Be cautious and drink lots of water!"
            advisable = False
        else:
            message = f"The temperature will be {temp_at_hour}ºC at the time you selected."
            advisable = True
        return message, advisable


# CHILD CLASS of Activity
class WaterActivity(Activity):
    def __init__(self, weather_summary):
        super().__init__(weather_summary)

    def check_wind(self):
        wind_speed = self.wind_speed_checker()
        if wind_speed == "ERROR":
            return "ERROR checking the weather", False
        elif wind_speed == "Calm":
            message = "There is no wind at the time you selected."
            advisable = True
        elif wind_speed == "Light":
            message = "There is light wind at the time you selected. Still, wind can stir up waves and you should be careful."
            advisable = True
        elif wind_speed == "Moderate":
            message = "There is moderate wind speed at the time you selected. Consider booking an alternative date because the sea might be too rough."
            advisable = False
        elif wind_speed == "High":
            message = "There is high wind speed at the time you selected. We advise you not to proceed. Consider booking an alternative date."
            advisable = False
        elif wind_speed == "Very high":
            message = "There is very high wind speed at the time you selected. We advise you not to proceed. Consider booking an alternative date."
            advisable = False
        return message, advisable

    def check_precipitation(self):
        precipitation_probability = self.precipitation_checker()

        if precipitation_probability == "ERROR":
            return "ERROR checking the weather", False
        elif precipitation_probability == "No":
            message = "There is no chance of precipitation at the time you selected."
            advisable = True
        elif precipitation_probability == "Low":
            message = "There is a low chance of precipitation at the time you selected."
            advisable = True
        elif precipitation_probability == "Moderate":
            message = "There is a moderate chance of precipitation at the time you selected. Consider booking an alternative date."
            advisable = False
        elif precipitation_probability == "High":
            message = "There is a high chance of precipitation at the time you selected. Consider booking an alternative date."
            advisable = False
        return message, advisable

    def check_weather_water_activity(self):

        if self.check_severe_risk()[1] == False:
            return (self.check_severe_risk()[0])
        if self.check_wind()[1] == False:
            return (self.check_wind()[0])
        if self.check_precipitation()[1] == False:
            return (self.check_precipitation()[0])
        if self.check_temperature()[1] == False:
            return (self.check_temperature()[0])
        else:
            return ("Weather looks good! You can proceed with your booking.")


# CHILD CLASS of Activity
class NonWaterActivity(Activity):
    def __init__(self, weather_summary):
        super().__init__(weather_summary)

    def check_wind(self):
        wind_speed = self.wind_speed_checker()
        if wind_speed == "ERROR":
            return "ERROR checking the weather", False
        elif wind_speed == "Calm":
            message = "There is no wind at the time you selected."
            advisable = True
        elif wind_speed == "Light":
            message = "There is light wind at the time you selected."
            advisable = True
        elif wind_speed == "Moderate":
            message = "There is moderate wind speed at the time you selected."
            advisable = True
        elif wind_speed == "High":
            message = "There is high wind speed at the time you selected. Consider booking an alternative date."
            advisable = False
        elif wind_speed == "Very high":
            message = "There is very high wind speed at the time you selected. We advise you not to proceed. Consider booking an alternative date."
            advisable = False
        return message, advisable

    def check_precipitation(self):
        precipitation_probability = self.precipitation_checker()

        if precipitation_probability == "ERROR":
            return "ERROR checking the weather", False
        elif precipitation_probability == "No":
            message = "There is no chance of precipitation at the time you selected."
            advisable = True
        elif precipitation_probability == "Low":
            message = "There is a low chance of precipitation at the time you selected."
            advisable = True
        elif precipitation_probability == "Moderate":
            message = "There is a moderate chance of precipitation at the time you selected. Consider booking an alternative date."
            advisable = False
        elif precipitation_probability == "High":
            message = "There is a high chance of precipitation at the time you selected. Consider booking an alternative date."
            advisable = False
        return message, advisable

    def check_weather_non_water_activity(self):

        if self.check_severe_risk()[1] == False:
            return (self.check_severe_risk()[0])
        if self.check_precipitation()[1] == False:
            return (self.check_precipitation()[0])
        if self.check_wind()[1] == False:
            return (self.check_wind()[0])
        if self.check_temperature()[1] == False:
            return (self.check_temperature()[0])
        else:
            return ("Weather looks good! You can proceed with your booking.")
