from db_utils import connect_to_db, DbConnectionError
import mysql.connector


def get_all_activities():
    """Retrieve and display all activities in the Thrilltopia Database"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        select_activities = "SELECT * FROM activities"
        cursor.execute(select_activities)
        # Getting all activities
        activities = cursor.fetchall()
        # closing the curser
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the time duration
    mapped = []
    for item in activities:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_activity_by_activity_id(activity_id):
    """Retrieve activity details from Thrilltopia using activity_id"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        get_activity = f"SELECT * FROM activities WHERE activity_id = {activity_id}"
        cursor.execute(get_activity)
        activity = cursor.fetchall()
        # closing the cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the time duration
    mapped = []
    for item in activity:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_all_indoor_activities():
    """Retrieve and display all activities in the Thrilltopia Database that are indoor"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        select_activities = "SELECT * FROM activities WHERE indoor_outdoor = 0 "
        cursor.execute(select_activities)
        activities = cursor.fetchall()
        # closing cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in activities:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_all_outdoor_activities():
    """Retrieve and display all activities in the Thrilltopia Database that are outdoor"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        select_activities = "SELECT * FROM activities WHERE indoor_outdoor = 1 "
        cursor.execute(select_activities)
        # Getting all activities
        activities = cursor.fetchall()
        # closing cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in activities:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_all_reservations():
    """Retrieve and display all reservations in the Thrilltopia Database"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        all_reservations = "SELECT * FROM reservations"
        cursor.execute(all_reservations)
        reservations = cursor.fetchall()
        # closing cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in reservations:
        seconds = item[5].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Reservation id': item[0],
            'First Name': item[1],
            'Last Name': item[2],
            'Phone Number': item[3],
            'Reservation Date': item[4].strftime("%d/%m/%Y") if item[4] else None,
            'Reservation Time': '{}:{}'.format(hours, minutes),
            'Number of people': item[6],
            'Activity id': item[7],
            'Equipment id': item[8]

        })
    print(mapped)
    return mapped


def get_reservation_by_activity_name(activity_name):
    """Retrieve and display all reservations for a specific activity in the Thrilltopia Database"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        reservations_for_activity_name = f"SELECT * FROM vw_reservations_by_activity WHERE activity_name = %s"
        cursor.execute(reservations_for_activity_name, (activity_name,))
        reservations = cursor.fetchall()
        # closing cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_reservations function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in reservations:
        seconds = item[5].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Reservation id': item[0],
            'First Name': item[1],
            'Last Name': item[2],
            'Phone Number': item[3],
            'Reservation Date': item[4].strftime("%d/%m/%Y") if item[4] else None,
            'Reservation Time': '{}:{}'.format(hours, minutes),
            'Number of people': item[6],
            'Activity id': item[7],
            'Equipment id': item[8],
            'Activity Name': item[9]

        })
    print(mapped)
    return mapped


def search_reservations_by_date(selected_date):
    """Retrieve and display reservations by querying Reservations table"""
    try:
        # connecting to the database
        db_name = 'Thrilltopia'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')
        # sql query for the function
        query = """
        SELECT Reservations.*, Activities.activity_name FROM Reservations 
        INNER JOIN Activities on Reservations.activity_id = Activities.activity_id
        WHERE reservation_date = %s
        """
        cur.execute(query, (selected_date,))
        result = cur.fetchall()
        # closing cursor
        cur.close()
    # exception if data can not be found or date format incorrect
    except ValueError:
        raise ValueError("Incorrect date. Please insert in format YYYY-MM-DD")
    except Exception:
        raise DbConnectionError("Failed to read data")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in result:
        seconds = item[5].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Reservation id': item[0],
            'First Name': item[1],
            'Last Name': item[2],
            'Phone Number': item[3],
            'Reservation Date': item[4].strftime("%d/%m/%Y") if item[4] else None,
            'Reservation Time': '{}:{}'.format(hours, minutes),
            'Number of people': item[6],
            'Activity id': item[7],
            'Equipment id': item[8],
            'Activity Name': item[9]
        })

    print(mapped)
    return mapped


def cancel_reservation_by_id(reservation_id):
    """Cancel a reservation from DB Thrilltopia with a specific reservation ID"""
    # connecting to the database
    db_name = 'thrilltopia'
    db_connection = connect_to_db(db_name)
    cursor = db_connection.cursor()
    try:
        print(f"You are connected to the DB: {db_name}")
        # sql query for the function
        query = f"""
                DELETE FROM Reservations
                WHERE reservation_id = {reservation_id}
                """
        cursor.execute(query)
        rows_affected = cursor.rowcount
        db_connection.commit()
        print("Reservation cancelled")
        # closing cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during cancel reservation function")
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    return rows_affected


def add_reservation(first_name: str, last_name: str, phone_number: str, reservation_date: str,
                    reservation_time: str, num_of_people: int, activity_id: int, equipment_id: int):
    """adding a reservation to the database"""
    # connecting to the database
    db_name = 'thrilltopia'
    db_connection = connect_to_db(db_name)
    cursor = db_connection.cursor()
    try:
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        add_reservation = """INSERT INTO Reservations (first_name, last_name, phone_number, 
                             reservation_date, reservation_time, num_of_people, activity_id, equipment_id) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(add_reservation, (first_name, last_name, phone_number, reservation_date,
                                         reservation_time, num_of_people, activity_id, equipment_id))

        db_connection.commit()
        print("Reservation added successfully")
    # exception if data can not be found
    except mysql.connector.Error as error:
        print("Error reading data from the DB", error)
    # closing the connection
    finally:
        rows_affected = cursor.rowcount
        cursor.close()
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
        return rows_affected


def get_reservation_by_customer_last_name(last_name):
    """Retrieve and display all reservations for an individual using their last name in the Thrilltopia Database"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        reservations_by_customer_name = f"SELECT * FROM vw_reservations_by_activity WHERE last_name = %s"
        cursor.execute(reservations_by_customer_name, (last_name,))
        customer_reservations = cursor.fetchall()
        # closing the cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_reservation_by_customer_last_name function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []

    for item in customer_reservations:
        seconds = item[5].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Reservation id': item[0],
            'First Name': item[1],
            'Last Name': item[2],
            'Phone Number': item[3],
            'Reservation Date': item[4].strftime("%d/%m/%Y") if item[4] else None,
            'Reservation Time': '{}:{}'.format(hours, minutes),
            'Number of people': item[6],
            'Activity id': item[7],
            'Equipment id': item[8],
            'Activity Name': item[9]

        })
    print(mapped)
    return mapped


def get_all_activities_ascending_price():
    """Retrieve and display all activities in the Thrilltopia Database in ascending price"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        activities = " SELECT * FROM activities ORDER BY price asc "
        cursor.execute(activities)
        activities = cursor.fetchall()
        # closing the connection
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities_ascending_price function")
# closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in activities:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_all_activities_descending_price():
    """Retrieve and display all activities in the Thrilltopia Database in descending price"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        activities = " SELECT * FROM activities ORDER BY price desc "
        cursor.execute(activities)
        activities = cursor.fetchall()
        # closing the connection
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities_descending_price function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in activities:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_equipment_for_activities(activity_name):
    """Retrieve and display all activities in the Thrilltopia Database"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        equipment_for_activity = """SELECT activity_name, Whats_included 
                                    FROM vw_equipment_for_activity 
                                    WHERE activity_name = %s"""
        cursor.execute(equipment_for_activity, (activity_name,))
        # Getting all activities
        equipment = cursor.fetchall()
        # closing the cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities_by_activity_name function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in equipment:
        mapped.append({
            'Activity Name': item[0],
            'Equipment': item[1]

        })
    print(mapped)
    return mapped


def get_reservation_by_id(reservation_id):
    """Search the reservation from DB Thrilltopia with a specific reservation ID"""
    # connecting to the database
    db_name = 'thrilltopia'
    db_connection = connect_to_db(db_name)
    cur = db_connection.cursor()
    print(f'Connected to DB: {db_name}')
    try:
        # sql query for the function
        query = f"""SELECT * FROM Reservations WHERE reservation_id = %s"""
        cur.execute(query, (reservation_id,))
        result = cur.fetchall()
        # closing the cursor
        cur.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_reservation_by_id function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in result:
        seconds = item[5].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Reservation id': item[0],
            'First Name': item[1],
            'Last Name': item[2],
            'Phone Number': item[3],
            'Reservation Date': item[4].strftime("%d/%m/%Y") if item[4] else None,
            'Reservation Time': '{}:{}'.format(hours, minutes),
            'Number of people': item[6],
            'Activity id': item[7],
            'Equipment id': item[8]
        })
        print(mapped)
        return mapped


def db_update_reservation_date(reservation_date, reservation_id):
    """Update reservation date by querying the Reservations table"""
    # connecting to the database
    db_name = 'thrilltopia'
    db_connection = connect_to_db(db_name)
    cur = db_connection.cursor()
    print(f'Connected to DB: {db_name}')
    try:
        # sql query for the function
        query = f"""
        UPDATE Reservations 
        SET reservation_date = %s
        WHERE reservation_id = %s
        """
        cur.execute(query, (reservation_date, reservation_id))
        db_connection.commit()
        updated = get_reservation_by_id(reservation_id)
        cur.close()
        if updated:
            return updated
    # exception if data can not be found
    except mysql.connector.errors.DataError as err:
        print(f"Something went wrong. Please correct your input accordingly {err}.")
        raise

    except Exception:
        raise DbConnectionError("Failed to read data during get_reservation_by_id function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')


def get_activity_by_activity_name(activity_name):
    """Retrieve activity details from Thrilltopia using activity_name"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        get_activity = """SELECT * FROM activities WHERE activity_name = %s"""
        cursor.execute(get_activity, (activity_name,))
        activity = cursor.fetchall()
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities_by_activity_name function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in activity:
        seconds = item[4].total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        mapped.append({
            'Activity id': item[0],
            'Activity Name': item[1],
            'Indoor / Outdoor': item[2],
            'Activity Description': item[3],
            'Duration': '{} hour {} mins'.format(hours, minutes),
            'Price': item[5],
            'Equipment id': item[6],
            'Photo URL': item[7]

        })
    print(mapped)
    return mapped


def get_equipment_provided_for_activities():
    """Retrieve and display all equipment for activities at Thrilltopia"""
    try:
        # connecting to the database
        db_name = 'thrilltopia'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'You are connected to the DB: {db_name}')
        # sql query for the function
        equipment_for_activity = """SELECT activity_name, Whats_included 
                                    FROM vw_equipment_for_activity """
        cursor.execute(equipment_for_activity)
        # Getting all activities
        equipment = cursor.fetchall()
        # closing the cursor
        cursor.close()
    # exception if data can not be found
    except Exception:
        raise DbConnectionError("Failed to read data during get_all_activities_by_activity_name function")
    # closing the connection
    finally:
        if db_connection:
            db_connection.close()
            print("The DB connection is now closed")
    # mapping the data into a dictionary and handling formatting the data
    mapped = []
    for item in equipment:
        mapped.append({
            'Activity Name': item[0],
            'Equipment': item[1]

        })
    print(mapped)
    return mapped
