import json
from collections import OrderedDict
import requests
from datetime import datetime
from WeatherAPI.get_weather import get_weather

# setting variable to run the script whilst is app running is true
is_app_running = True
# creating an ordered dictionary with all the activities available at Thrilltopia in it
activities = OrderedDict()
activities[1] = 'Kayaking'
activities[2] = 'Paddle Boarding'
activities[3] = 'Indoor Tennis'
activities[4] = 'Outdoor Tennis'
activities[5] = 'Indoor Climbing Wall'
activities[6] = 'Outdoor Climbing Wall'
activities[7] = 'Indoor Paintball'
activities[8] = 'Outdoor Paintball'
activities[9] = 'Indoor Virtual Mountain Biking'
activities[10] = 'Outdoor Mountain Biking'
activities[11] = 'Indoor Mini Golf'
activities[12] = 'Outdoor Mini Golf'

# getting the api key from the config file and adding the variable api_key
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['forecast_api']['api_key']


def welcome_message():
    """Display welcome message"""
    print("Welcome to Thrilltopia, CFG's biggest indoor and outdoor activity centre!")
    print("Discover exhilarating indoor and outdoor activities that can be done alone or with friends and family!\n")


def exit_app():
    """Exit the application"""
    confirmation = input("Are you sure you want to exit? (Y/N) ").strip().lower()
    if confirmation == "y":
        print("Thank you for visiting Thrilltopia")
        print("Please come back soon!")
        # change global variable is_app_running to false, stopping the loop
        global is_app_running
        is_app_running = False


def all_activities():
    """ Display all activities """
    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def activities_by_name():
    """ Get all activities by activity name"""
    while True:
        try:
            for k, v in activities.items():
                print(k, ": ", v)
            activity_name = input("\nPlease enter the name of activity are interested in: ").title()
            if activity_name in activities.values():
                break
            else:
                print("Invalid input. Please select a valid activity name. ")
        except TypeError:
            print(f"Invalid input. No activity with activity name {activity_name} found. ")

    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/name/{}'.format(activity_name),
                          headers={'content-type': 'application/json'})
    if result.status_code == 200:
        print(f"Below is the information for the activity {activity_name}.")
        print(result.text)
        return result.json()
    elif result.status_code == 404:
        print("No activity with this name available.")
    return result.text


def activities_by_activity_id():
    """ Get all activities by activity id"""
    while True:
        try:
            for k, v in activities.items():
                print(k, ": ", v)
            activity_id = int(input("\nPlease select the ID for the activity you require from the list above: "))
            if activity_id in activities.keys():
                break
            else:
                print("Invalid input. Please select a valid activity id. ")
        except TypeError:
            print("Invalid input. Please select a valid number for activity id. ")

    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/{}'.format(activity_id),
                          headers={'content-type': 'application/json'})
    if result.status_code == 200:
        print(f"Below is the information for the activity {activity_id}.")
        print(result.text)
        return result.json()
    elif result.status_code == 404:
        print("No activity with this id available.")
    return result.text


def all_reservations():
    """ Get all reservations"""
    result = requests.get('http://127.0.0.1:5005/thrilltopia/reservations',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def reservation_by_last_name():
    """ Get all reservations by last name"""
    while True:
        try:
            last_name = input("What is the last name on the reservation you are looking for? ").title()
        except ValueError:
            print(f"Invalid input. No reservation with last name {last_name}.")

        result = requests.get('http://127.0.0.1:5005/thrilltopia/reservations/name/{}'.format(last_name),
                              headers={'content-type': 'application/json'})
        if result.status_code == 200:
            print(f"Below is the information for the reservation with last name {last_name}.")
            print(result.text)
            return result.json()
        elif result.status_code == 404:
            print("No activity with this name available.")
        return result.text


def reservation_by_activity_name():
    """ Get all reservations for a particular activity using the activity name"""
    while True:
        try:
            for k, v in activities.items():
                print(k, ": ", v)
            activity_name = input("\nWhat is the name of the activity you would like to see reservations for? ").title()
        except ValueError:
            print("There are no reservations for the activity")

        result = requests.get('http://127.0.0.1:5005/thrilltopia/reservations/{}'.format(activity_name),
                              headers={'content-type': 'application/json'})
        if result.status_code == 200:
            print(f"Below is the information for the activity with last name {activity_name}.")
            print(result.text)
            return result.json()
        elif result.status_code == 404:
            print("No reservation with this name available.")
        return result.text


def reservation_by_date():
    """ Get all reservations by a particular date"""
    while True:
        try:
            print("please use the following format: yyyy-mm-dd")
            date = input("What is the date you would like to see reservations for? ")
        except ValueError:
            print("There are no reservations for that date")
        reservation_date = datetime.strptime(date, "%Y-%m-%d").date()

        result = requests.get('http://127.0.0.1:5005/thrilltopia/reservations/date/{}'.format(reservation_date),
                              headers={'content-type': 'application/json'})
        if result.status_code == 200:
            print(f"Below is the information for the reservation with date {reservation_date}.")
            print(result.text)
            return result.json()
        elif result.status_code == 404:
            print("No reservation with this date available.")
        return result.text


def all_equipment():
    """ Get all equipment"""
    result = requests.get('http://127.0.0.1:5005/thrilltopia/equipment',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def equipment_for_activity():
    """ Get all equipment for a particular activity using the activity name"""
    while True:
        try:
            for k, v in activities.items():
                print(k, ": ", v)
            activity_name = input("\nWhat is the name of the activity you would like to see the equipment "
                                  "provided for? ").title()
        except ValueError:
            print("There are no activities with this name")

        result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/equipment/{}'.format(activity_name),
                              headers={'content-type': 'application/json'})

        if result.status_code == 200:
            print(f"Below is the information for the activity with last name {activity_name}.")
            print(result.text)
            return result.json()
        elif result.status_code == 404:
            print("No reservation with this name available.")
        return result.text


def activities_price_ascending():
    """ Get all activities in ascending order"""
    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/price/asc',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def activities_price_descending():
    """ Get all activities in descending order"""
    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/price/desc',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def indoor_activities():
    """ Get all activities that are indoor"""
    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/indoor',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def outdoor_activities():
    """ Get all activities that are outdoor"""
    result = requests.get('http://127.0.0.1:5005/thrilltopia/activities/outdoor',
                          headers={'content-type': 'application/json'})
    print(result.text)
    return result.json()


def cancel_reservation():
    """Search and delete a reservation in the database by customer last name"""
    while True:
        try:
            reservation_id = int(input("Please enter the reservation id of the reservation to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid id for the reservation.")

    result = requests.delete('http://127.0.0.1:5005/thrilltopia/reservation/cancel/{}'.format(reservation_id),
                             headers={'content-type': 'application/json'})
    if result.status_code == 200:
        print('`reservation deleted successfully.')
    elif result.status_code == 404:
        print('No reservation with given id found in the database.')
    return result.text


def update_reservation_date_by_id():
    """
    Update and existing reservation by searching it by its id then updating the date
    """
    while True:
        try:
            print("please use the following format: yyyy-mm-dd")
            date = input("What is the date you would like to change the reservations to? ")
            reservation_date = datetime.strptime(date, "%Y-%m-%d").date()
            reservation_id = int(input("Please enter your reservation id: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid reservation id .")

    result = requests.patch('http://127.0.0.1:5005/thrilltopia/reservations/update/{}/{}'.format(reservation_date, reservation_id),
                           headers={'content-type': 'application/json'})
    if result.status_code == 200:
        print("Reservation with with id {} has had their reservation updated to {}".format(reservation_id, reservation_date))
        print(result.json())
        return result.json()
    elif result.status_code == 404:
        print("Reservation with these details not found in the database.")


def add_reservation():
    """ function to add a new reservation"""
    first_name = input("Please enter your first name: ").title()
    last_name = input("Please enter your last name: ").title()
    phone_number = input("Please enter your phone number: ")
    print("Only dates from today for the next 14 days will be valid")
    reservation_date = input("Please enter your reservation date in the following format: yyyy-mm-dd: ")
    reservation_time = input("Please enter your reservation time in the following format: hh:mm: ")
    num_of_people = int(input("Please enter the number of people: "))
    for k, v in activities.items():
        print(k, ": ", v)
    activity_id = int(input("Please enter the activity id: "))
    equipment_id = activity_id
    result = get_weather(api_key, reservation_date, reservation_time, activity_id)
    print(result)
    while result == "Invalid date or outside the forecast range.":
        reservation_date = input("Please enter your reservation date in the following format: yyyy-mm-dd: ")
        reservation_time = input("Please enter your reservation time in the following format: hh:mm: ")
        result = get_weather(api_key, reservation_date, reservation_time, activity_id)
        print(result)
    proceed = input("Would you like to continue with this reservation? Y/N ").upper()
    if proceed == "N":
        exit_app()
    else:
        reservation = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "reservation_date": reservation_date,
            "reservation_time": reservation_time,
            "num_of_people": num_of_people,
            "activity_id": activity_id,
            "equipment_id": equipment_id
        }
        print(reservation)

        result = requests.post('http://127.0.0.1:5005/thrilltopia/reservations',
                               headers={'content-type': 'application/json'},
                               data=json.dumps(reservation))

        print(f"Reservation with first name {first_name} and last name {last_name} has been added.")
        return result


def run():
    """ function to run the application in the console"""
    # display the welcome message to the user
    welcome_message()

    # choices ordered dictionary to display the menu options available for the user in the run function
    menu_choices = OrderedDict()
    menu_choices[1] = 'Display Activities'
    menu_choices[2] = 'Display Reservations'
    menu_choices[3] = 'Make / Alter / cancel a Reservation'
    menu_choices[4] = 'Display Equipment'
    menu_choices[5] = 'Exit'

    # ordered dictionary to call all the function options available relating to activities
    activity_options = OrderedDict()
    activity_options[1] = all_activities
    activity_options[2] = activities_by_name
    activity_options[3] = activities_by_activity_id
    activity_options[4] = indoor_activities
    activity_options[5] = outdoor_activities
    activity_options[6] = activities_price_ascending
    activity_options[7] = activities_price_descending
    activity_options[8] = exit_app

    # ordered dictionary to call all the function options available relating to viewing reservation
    view_reservation_options = OrderedDict()
    view_reservation_options[1] = all_reservations
    view_reservation_options[2] = reservation_by_last_name
    view_reservation_options[3] = reservation_by_activity_name
    view_reservation_options[4] = reservation_by_date
    view_reservation_options[5] = exit_app

    # ordered dictionary to call all the function options available relating to altering reservations
    alter_reservation_options = OrderedDict()
    alter_reservation_options[1] = update_reservation_date_by_id
    alter_reservation_options[2] = add_reservation
    alter_reservation_options[3] = cancel_reservation
    alter_reservation_options[4] = exit_app

    # ordered dictionary to call all the function options available relating to equipment
    view_equipment_options = OrderedDict()
    view_equipment_options[1] = all_equipment
    view_equipment_options[2] = equipment_for_activity
    view_equipment_options[3] = exit_app

    # while loop to keep the app running whilst is app running is true
    while is_app_running:
        # adding a try in order to catch any input errors
        try:
            # printing the choices in the console for the user from the menu choices ordered dictionary
            for k, v in menu_choices.items():
                print(k, "to view options for ", v)
            # asking the user to choose a number for the option they want to select
            menu_choice = int(input("Please enter the number for the menu options you would like to view: \n"))
            # validating the user choice and displaying further options
            if menu_choice in menu_choices:
                # if the user chooses option 1 showing the options for the activities functions
                if menu_choice == 1:
                    print("\n1. To display all activities available at Thrilltopia")
                    print("2. To search for details of a specific activity by it's name")
                    print("3. To search for details of a specific activity by it's ID number")
                    print("4. To display all Indoor activities")
                    print("5. To display all Outdoor activities")
                    print("6. To display all activities in ascending price order")
                    print("7. To display all activities in descending price order")
                    print("8. To exit\n")
                    # getting an integer input from the user for their menu choice
                    activity_choice = int(input("Please enter the number for the activities "
                                                "menu options you would like to view: \n"))
                    # checking if the user choice is in the activity options dictionary keys and if it is calling that
                    # function
                    if activity_choice in activity_options:
                        activity_options[activity_choice]()
                    # handling incorrect input
                    else:
                        print("Invalid choice. Please select a valid option.\n")
                    # giving the user the option to continue with other options or to quit the app
                    carry_on = input("please enter 0 to exit or any other key to continue \n")
                    if carry_on == 0 or carry_on == "0":
                        exit_app()

                # if the user chooses option 2 showing the options for viewing reservations functions
                elif menu_choice == 2:
                    print("\n1. To show all reservations at Thrilltopia")
                    print("2. To search for a reservation by a Surname")
                    print("3. To show all reservations for an activity using the activity name")
                    print("4. To show all reservations on a specific date")
                    print("5. To exit\n")
                    # getting an integer input from the user for their menu choice
                    view_reservation_choice = int(input("Please enter the number for the view reservation "
                                                        "menu options you would like to view: \n"))
                    # checking if the user choice is in the view reservations  dictionary keys and if it is calling
                    # that function
                    if view_reservation_choice in view_reservation_options:
                        view_reservation_options[view_reservation_choice]()
                    # handling incorrect input
                    else:
                        print("Invalid choice. Please select a valid option.\n")
                    # giving the user the option to continue with other options or to quit the app
                    carry_on = input("please enter 0 to exit or any other key to continue \n")
                    if carry_on == 0 or carry_on == "0":
                        exit_app()

                # if the user chooses option 3 showing the options for adding, altering and deleting reservations
                # functions
                elif menu_choice == 3:
                    print("\n1. To update a reservation date with the reservation ID")
                    print("2. To make a reservation")
                    print("3. To cancel a reservation")
                    print("4. To exit\n")
                    # getting an integer input from the user for their menu choice
                    alter_reservation_choice = int(input("Please enter the number for the alter reservation "
                                                         "menu options you would like to view: \n"))
                    # checking if the user choice is in the alter reservations  dictionary keys and if it is calling
                    # that function
                    if alter_reservation_choice in alter_reservation_options:
                        alter_reservation_options[alter_reservation_choice]()
                    # handling incorrect input
                    else:
                        print("Invalid choice. Please select a valid option.\n")
                    # giving the user the option to continue with other options or to quit the app
                    carry_on = input("please enter 0 to exit or any other key to continue \n")
                    if carry_on == 0 or carry_on == "0":
                        exit_app()

                # if the user chooses option 4 showing the options for viewing equipment functions
                elif menu_choice == 4:
                    print("\n1. To show all activities and the equipment provided by Thrilltopia")
                    print("2. To search a specific activity to see the equipment provided")
                    print("3. To exit\n")
                    # getting an integer input from the user for their menu choice
                    view_equipment_choice = int(input("Please enter the number for the view equipment "
                                                      "menu options you would like to view: \n"))
                    # checking if the user choice is in the view equipment  dictionary keys and if it is calling
                    # that function
                    if view_equipment_choice in view_equipment_options:
                        view_equipment_options[view_equipment_choice]()
                    else:
                        print("Invalid choice. Please select a valid option.\n")
                    # giving the user the option to continue with other options or to quit the app
                    carry_on = input("please enter 0 to exit or any other key to continue \n")
                    if carry_on == 0 or carry_on == "0":
                        exit_app()

                # if the user chooses option 5 exit the app
                elif menu_choice == 5:
                    exit_app()
                # handling incorrect input
                else:
                    print("Invalid option! Please enter a valid choice!")
            # handling incorrect input
            else:
                print("Invalid choice, Please select a valid option.\n")
        # catching input option errors
        except ValueError:
            print("Invalid choice, Please select a valid option.\n")


if __name__ == "__main__":
    run()
