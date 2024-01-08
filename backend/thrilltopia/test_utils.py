import unittest
from utils import *


class TestGetActivityById(unittest.TestCase):
    def test_activityById_valid_10(self):
        expected_result = [{
            "Activity Description": "Embark on an exhilarating mountain biking adventure, available for outdoor enthusiasts. Choose your terrain and difficulty level, from beginner trails to \nadvanced routes. Suitable for riders aged 12 and above (accompanied by an adult), offering a thrilling experience. Bikes and safety gear provided for a safe and enjoyable ride. Difficulty Level: Beginner \nto Advanced. Minimum Age: 12 years old (accompanied by an adult)",
            "Activity Name": "Outdoor Mountain Biking",
            "Activity id": 10,
            "Duration": "2 hour 0 mins",
            "Equipment id": 10,
            "Indoor / Outdoor": 1,
            "Photo URL": "https://images.unsplash.com/photo-1544191696-102dbdaeeaa0?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "Price": 30.0
        }]
        self.assertEqual(expected_result, get_activity_by_activity_id(10))

    def test_activityById_invalid20(self):
        self.assertEqual([], get_activity_by_activity_id(20))


class TestGetReservationByActivityName(unittest.TestCase):
    def test_reservationByActivityName_valid_OutdoorMountainBiking(self):
        expected_result = [{
            "Activity Name": "Outdoor Mountain Biking",
            "Activity id": 10,
            "Equipment id": 10,
            "First Name": "Robert",
            "Last Name": "Baker",
            "Number of people": 2,
            "Phone Number": "07537883647",
            "Reservation Date": "30/11/2023",
            "Reservation Time": "19:0",
            "Reservation id": 12
        }]
        self.assertEqual(expected_result, get_reservation_by_activity_name('Outdoor Mountain Biking'))

    def test_reservationByActivityName_invalid_IncorrectName(self):
        self.assertEqual([], get_reservation_by_activity_name("Outdoor Climbing"))


class TestGetReservationByDate(unittest.TestCase):
    def test_reservationByDate_valid_date(self):
        expected_result = [
            {"Activity Name": "Outdoor Climbing Wall", "Activity id": 6, "Equipment id": 6, "First Name": "Daniel",
             "Last Name": "Miller", "Number of people": 2, "Phone Number": "03456789012",
             "Reservation Date": "08/01/2024", "Reservation Time": "13:30", "Reservation id": 10}]
        self.assertEqual(expected_result, search_reservations_by_date('2024/01/08'))

    def test_reservationByDate_invalid_datetype(self):
        with self.assertRaises(ValueError):
            search_reservations_by_date('2024-01-08')


class TestCancelReservationById(unittest.TestCase):
    def test_cancelreservation_valid_reservation_id_10(self):
        self.assertEqual(1, cancel_reservation_by_id(12))  # 1 is the expected result as 1 row should be affected

    def test_cancelreservation_invalid_id_0(self):
        self.assertEqual(0, cancel_reservation_by_id(0))  # 0 rows expected to be returned


class TestGetReservationById(unittest.TestCase):
    def test_getreservationbyid_valid_id(self):
        expected_result = [
            {'Reservation id': 3, 'First Name': 'Sarah', 'Last Name': 'Campbell', 'Phone Number': '07265647890',
             'Reservation Date': '22/11/2023', 'Reservation Time': '9:45', 'Number of people': 1, 'Activity id': 7,
             'Equipment id': 7}]
        self.assertEqual(expected_result, get_reservation_by_id(3))

    def test_getreservationbyid_invalid_id(self):
        self.assertEqual(None, get_reservation_by_id('ABC'))

    def test_getreservationbyid_boundary_id(self):
        self.assertEqual(None, get_reservation_by_id(0000))


class TestDbUpdateReservationDate(unittest.TestCase):
    def test_reservationByDate_valid_date_and_valid_reservation_id(self):
        expected_result = [
            {'Reservation id': 1, 'First Name': 'Vicki', 'Last Name': 'Brown', 'Phone Number': '07846873376',
             'Reservation Date': '21/11/2023', 'Reservation Time': '14:30', 'Number of people': 1, 'Activity id': 1,
             'Equipment id': 1}]
        self.assertEqual(expected_result, db_update_reservation_date("2023-11-21", 1))

    def test_reservationByDate_valid_date_but_invalid_id(self):
        with self.assertRaises(mysql.connector.DataError):
            db_update_reservation_date("2023-11-21", 'XYZ')

    def test_reservationByDate_invalid_date_but_valid_id(self):
        with self.assertRaises(mysql.connector.DataError):
            db_update_reservation_date("year", 1)

    def test_reservationByDate_boundary_date_and_boundary_id(self):
        self.assertEqual(None, get_reservation_by_id(0000))


class TestGetAllIndoorActivities(unittest.TestCase):
    def test_getallindooractivities_valid_bit(self):
        indoor_activity_names = []
        activities = get_all_indoor_activities()
        for activity in activities:
            indoor_activity_names.append(activity['Activity Name'])
        expected_result = ['Indoor Tennis',
                           'Indoor Climbing Wall',
                           'Indoor Paintball',
                           'Indoor Virtual Mountain Biking',
                           'Indoor Mini Golf']
        self.assertEqual(expected_result, indoor_activity_names)


class TestGetAllOutdoorActivities(unittest.TestCase):
    def test_getalloutdooractivities_valid_bit(self):
        outdoor_activity_names = []
        activities = get_all_outdoor_activities()
        for activity in activities:
            outdoor_activity_names.append(activity['Activity Name'])
        expected_result = ['Kayaking',
                           'Paddle Boarding',
                           'Outdoor Tennis',
                           'Outdoor Climbing Wall',
                           'Outdoor Paintball',
                           'Outdoor Mountain Biking',
                           'Outdoor Mini Golf']
        self.assertEqual(expected_result, outdoor_activity_names)


if __name__ == '__main__':
    unittest.main()
