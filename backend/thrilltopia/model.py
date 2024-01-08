from flask import Flask, jsonify, request, json
from flask_cors import CORS
from utils import *
from WeatherAPI.get_weather import get_weather
from datetime import datetime

app = Flask(__name__)
CORS(app)

with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['forecast_api']['api_key']


@app.route('/thrilltopia')
def welcome():
    """
    Route to home page with a welcome message
    """
    return "Welcome to Thrilltopia!"


@app.route('/thrilltopia/activities')
def show_all_activities():
    """
    Route to show all activities available at Thrilltopia
    """
    result = get_all_activities()
    return jsonify(result), 200


@app.route('/thrilltopia/activities/<int:activity_id>', methods=['GET'])
def show_activity_by_id(activity_id):
    """
    Defining a route for getting a specific activity by ID
    """
    result = get_activity_by_activity_id(activity_id)
    if len(result) < 1:
        print('No Activity found')
    else:
        return jsonify(result), 200


@app.route('/thrilltopia/activities/indoor', methods=['GET'])
def get_indoor_activities():
    """
    Defining a route for getting all indoor activities
    """
    result = get_all_indoor_activities()
    if len(result) < 1:
        print('No Activity found')
    else:
        return jsonify(result), 200


@app.route('/thrilltopia/activities/outdoor', methods=['GET'])
def get_outdoor_activities():
    """
        Defining a route for getting all outdoor activities
        """
    result = get_all_outdoor_activities()
    if len(result) < 1:
        print('No Activity found')
    else:
        return jsonify(result), 200


@app.route('/thrilltopia/reservations', methods=['GET'])
def show_all_reservations():
    """
       Route to show all reservations at Thrilltopia
       """
    result = get_all_reservations()
    return jsonify(result), 200


@app.route('/thrilltopia/reservations/<activity_name>', methods=['GET'])
def show_reservations_by_activity_name(activity_name):
    """
    Route to show all reservations for a specific activity by name
    """
    result = get_reservation_by_activity_name(activity_name)
    return jsonify(result), 200


@app.route('/thrilltopia/reservations/date/<selected_date>', methods=['GET'])
def get_reservation_by_date(selected_date):
    """
    Route to show all reservations for a specific date
    """
    selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    result = search_reservations_by_date(selected_date)
    if result:
        j_result = json.dumps(result, default=str)
        return j_result, 200
    else:
        return 'No reservation made on this date.', 404


@app.route('/thrilltopia/weather/<activity_id>/<date>/<startTime>', methods=['GET'])
def show_weather(activity_id, date, startTime):
    """
    Route to show the weather for the next 15 days
    """
    if not (activity_id and date and startTime):
        return jsonify({"error": "Invalid parameters"}), 500
    # Please use your own key to connect to the API
    appid = api_key
    result = get_weather(appid, date, startTime, activity_id)

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Failed to fetch weather data"}), 500


@app.route('/thrilltopia/reservation/cancel/<int:reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    """Route to cancel a reservation from the Thrilltopia Database by its ID"""
    rows = cancel_reservation_by_id(reservation_id)
    if rows > 0:
        print('Reservation cancelled successfully.')
        return 'OK', 200
    else:
        print('No reservation with given ID in the database.')
        return 'Not found', 404


@app.route('/thrilltopia/reservations', methods=['POST'])
def add_a_reservation():
    """Route to add a new reservation to the Thrilltopia database"""
    new_reservation = request.get_json()
    formatted_time = new_reservation['reservation_time'].replace(':', '') + '00'
    rows = add_reservation(
        first_name=new_reservation['first_name'],
        last_name=new_reservation['last_name'],
        phone_number=new_reservation['phone_number'],
        reservation_date=new_reservation['reservation_date'],
        reservation_time=formatted_time,
        num_of_people=new_reservation['num_of_people'],
        activity_id=new_reservation['activity_id'],
        equipment_id=new_reservation['equipment_id']
    )
    if rows > 0:
        print('Reservation added successfully.')
        return 'OK', 200
    else:
        print('Cannot make a reservation.')
        return 'Bad request', 400


@app.route('/thrilltopia/reservations/update/<reservation_date>/<int:reservation_id>', methods=['PATCH'])
def update_reservation_date(reservation_date, reservation_id):
    """Route to edit the reservation date on the Thrilltopia database"""
    reservations = get_reservation_by_id(reservation_id)
    if not reservations:
        return jsonify({'error': 'Reservation not found'}), 404
    updated = db_update_reservation_date(reservation_date, reservation_id)
    return jsonify(updated), 200


@app.route('/thrilltopia/reservations/name/<last_name>', methods=['GET'])
def show_customer_reservation_using_last_name(last_name):
    """
    Route to show all reservations for a customer using their last name
    """
    result = get_reservation_by_customer_last_name(last_name)
    return jsonify(result), 200


@app.route('/thrilltopia/activities/price/asc')
def show_all_activities_ascending_price():
    """
    Route to show all activities available at Thrilltopia in ascending price order
    """
    result = get_all_activities_ascending_price()
    return jsonify(result), 200


@app.route('/thrilltopia/activities/price/desc')
def show_all_activities_descending_price():
    """
    Route to show all activities available at Thrilltopia n descending price order
    """
    result = get_all_activities_descending_price()
    return jsonify(result), 200


@app.route('/thrilltopia/activities/equipment/<activity_name>', methods=['GET'])
def show_equipment_for_activity_by_activity_name(activity_name):
    """
    Route to show the equipment needed for a specific activity
    """
    equipment = get_equipment_for_activities(activity_name)
    return jsonify(equipment), 200


@app.route('/thrilltopia/activities/name/<activity_name>', methods=['GET'])
def show_all_activities_by_activity_name(activity_name):
    """
    Route to show all activities using a specific name
    """
    activity = get_activity_by_activity_name(activity_name)
    return jsonify(activity), 200


@app.route('/thrilltopia/equipment', methods=['GET'])
def show_all_equipment():
    """Show all equipment provided for each activity at thrilltopia"""
    equipment = get_equipment_provided_for_activities()
    return jsonify(equipment), 200


if __name__ == '__main__':
    app.run(debug=True, port=5005)
