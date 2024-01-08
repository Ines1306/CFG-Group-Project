CREATE DATABASE Thrilltopia;
USE Thrilltopia;

CREATE TABLE Equipment(
equipment_id INT NOT NULL PRIMARY KEY,
equipment_name VARCHAR(50) NOT NULL,
whats_included VARCHAR(1000) NOT NULL,
equipment_stock INT NOT NULL
);

CREATE TABLE Activities(
activity_id INT NOT NULL PRIMARY KEY,
activity_name VARCHAR(100) NOT NULL,
indoor_outdoor BIT NOT NULL,
activity_description VARCHAR(4000) NOT NULL,
duration TIME NOT NULL,
price FLOAT NOT NULL,
equipment_id INT,
photo_url VARCHAR(1000) NOT NULL,
FOREIGN KEY(equipment_id) REFERENCES Equipment(equipment_id)
);


CREATE TABLE Reservations(
reservation_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
phone_number VARCHAR(20) NOT NULL,
reservation_date DATE NOT NULL,
reservation_time TIME NOT NULL,
num_of_people INT NOT NULL,
activity_id INT NOT NULL,
equipment_id INT NOT NULL,
FOREIGN KEY(activity_id) REFERENCES Activities(activity_id),
FOREIGN KEY(equipment_id) REFERENCES Equipment(equipment_id)
);


INSERT INTO Equipment
(equipment_id, equipment_name, whats_included, equipment_stock)
VALUES
(1, 'Kayaking', 'Kayak, Paddle, Wetsuit, Life Jacket', 50),
(2, 'Paddle Boarding', 'Paddle Board, Paddle, Wetsuit, Life Jacket', 50),
(3, 'Indoor Tennis', 'Tennis Racket, 2 Tennis Balls', 20),
(4, 'Outdoor Tennis', 'Tennis Racket, 2 Tennis Balls', 20),
(5, 'Indoor Climbing Wall', 'Climbing Harness, Helmet, Knee Pads, Elbow Pads, Goggles', 5),
(6, 'Outdoor Climbing Wall', 'Climbing Harness, Helmet, Knee Pads, Elbow Pads, Goggles', 5),
(7, 'Indoor Paintball', 'Paintball Gun, 500 Paint Balls, Helmet, Knee Pads, Elbow Pads, Goggles', 25),
(8, 'Outdoor Paintball', 'Paintball Gun, 500 Paint Balls, Helmet, Knee Pads, Elbow Pads, Goggles', 25),
(9, 'Indoor Virtual Mountain Biking', 'Virtual Headset, Indoor Static Bike, Helmet, Knee Pads, Elbow Pads',4),
(10, 'Outdoor Mountain Biking', 'Mountain Bike, Helmet, Knee Pads, Elbow Pads', 50),
(11, 'Indoor Mini Golf', 'Golf Club, 1 Golf Ball, Score Card, Pencil', 50),
(12, 'Outdoor Mini Golf', 'Golf Club, 1 Golf Ball, Score Card, Pencil', 50);


INSERT INTO Activities
(activity_id, activity_name, indoor_outdoor, activity_description, duration, price, equipment_id, photo_url)
VALUES

(1, 'Kayaking', 1, 'Experience the thrill of kayaking on serene waters. Suitable for all skill levels, this outdoor adventure
is perfect for families, with children over 8 years old accompanied by an adult. Choose between a solo kayak or a kayak for two, and
enjoy the scenic beauty from a unique perspective. Difficulty Level: Beginner to Intermediate. Minimum Age: 8 years old (accompanied by an adult)', '020000', 30.00, 1,
'https://images.unsplash.com/photo-1588472235276-7638965471e2?q=80&w=3869&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(2, 'Paddle Boarding', 1, 'Try paddle boarding for a fantastic way to enjoy the water and improve balance. Great for families, with
children over 10 welcome accompanied by an adult. You can choose between solo paddle boards or tandem boards for two. Glide along calm
waters and soak in the tranquil surroundings. Difficulty Level: Beginner. Minimum Age: 10 years old (accompanied by an adult).', '013000', 25.00, 2,
'https://images.unsplash.com/photo-1618857320903-6e7eea312a8e?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(3, 'Indoor Tennis', 0, 'Improve your tennis skills or enjoy a casual game in our indoor tennis courts. Suitable for all
ages and skill levels, perfect for individuals or groups. Rackets and balls provided, making it convenient for everyone to join in the fun. Difficulty Level: Beginner to Advanced.
Minimum Age: No age restrictions', '010000', 15.00, 3,
'https://images.unsplash.com/photo-1602012846858-0727988e215b?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(4, 'Outdoor Tennis ', 1, 'Improve your tennis skills or enjoy a casual game on our outdoor tennis courts. Suitable for all
ages and skill levels, perfect for individuals or groups. Rackets and balls provided, making it convenient for everyone to join in the fun. Difficulty Level: Beginner to Advanced.
Minimum Age: No age restrictions', '010000', 15.00, 4,
'https://images.unsplash.com/flagged/photo-1576972405668-2d020a01cbfa?q=80&w=3874&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(5, 'Indoor Climbing Wall', 0, 'Challenge yourself on our indoor climbing wall. Suitable for various skill levels, from beginners looking to try something new
to experienced climbers seeking a thrill. Safety equipment and guidance provided for an exhilarating experience. Participants aged 6 and above are welcome, with children required to
be accompanied by an adult.', '013000', 20.00, 5,
 'https://images.unsplash.com/photo-1564769662533-4f00a87b4056?q=80&w=3944&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(6, 'Outdoor Climbing Wall', 1, 'Challenge yourself on our outdoor climbing wall. Suitable for various skill levels, from beginners looking to try something new
to experienced climbers seeking a thrill. Safety equipment and guidance provided for an exhilarating experience. Participants aged 6 and above are welcome, with children required to
be accompanied by an adult.', '013000', 20.00, 6,
'https://images.unsplash.com/photo-1578763399089-42091eda1cda?q=80&w=3876&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(7, 'Indoor Paintball', 0, 'Experience the excitement of paintball in our thrilling indoor arena. Suitable for players with various skill levels, from those seeking a fun challenge
to seasoned paintball enthusiasts. Safety gear and markers provided for an adrenaline-pumping adventure. Participants aged 12 and above are welcome, with minors required to be accompanied
by an adult. Difficulty Level: Moderate to Advanced. Minimum Age: 12 years old (accompanied by an adult).', '020000', 30.00, 7,
'https://images.unsplash.com/photo-1588432892804-a10512c79146?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(8, 'Outdoor Paintball', 1, 'Experience the excitement of paintball in our thrilling outdoor arena. Suitable for players with various skill levels, from those seeking a fun challenge
to seasoned paintball enthusiasts. Safety gear and markers provided for an adrenaline-pumping adventure. Participants aged 12 and above are welcome, with minors required to be accompanied
by an adult. Difficulty Level: Moderate to Advanced. Minimum Age: 12 years old (accompanied by an adult).', '020000', 30.00, 8,
'https://images.unsplash.com/photo-1627389522449-fa0f191a1dbd?q=80&w=3871&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(9, 'Indoor Virtual Mountain Biking', 0, 'Embark on an exhilarating virtual mountain biking adventure. Choose your terrain and difficulty level, from beginner trails to advanced routes.
Suitable for riders aged 12 and above (accompanied by an adult), offering a thrilling experience. Bikes and safety gear provided for a safe and enjoyable ride. Difficulty Level: Beginner
to Advanced. Minimum Age: 12 years old (accompanied by an adult).', '020000', 30.00, 9,
'https://images.unsplash.com/photo-1592477725143-2e57dc728f0a?q=80&w=3806&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(10, 'Outdoor Mountain Biking', 1, 'Embark on an exhilarating mountain biking adventure, available for outdoor enthusiasts. Choose your terrain and difficulty level, from beginner trails to
advanced routes. Suitable for riders aged 12 and above (accompanied by an adult), offering a thrilling experience. Bikes and safety gear provided for a safe and enjoyable ride. Difficulty Level: Beginner
to Advanced. Minimum Age: 12 years old (accompanied by an adult)', '020000', 30.00, 10,
'https://images.unsplash.com/photo-1544191696-102dbdaeeaa0?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(11, 'Indoor Mini Golf', 0, 'Enjoy a round of mini golf, available in our indoor setting. Perfect for families, friends, or individuals of all ages and skill levels. Experience the thrill of
navigating through our creatively designed courses. No age restrictions make it an ideal activity for everyone. Difficulty Level: Fun for All Skill Levels. Minimum Age: No age restrictions',
 '010000', 10.00, 11, 'https://images.unsplash.com/photo-1665791567320-8cee5dc908d2?q=80&w=3774&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),

(12, 'Outdoor Mini Golf', 1, 'Enjoy a round of mini golf, available in our outdoor setting. Perfect for families, friends, or individuals of all ages and skill levels. Experience the thrill of
navigating through our creatively designed courses. No age restrictions make it an ideal activity for everyone. Difficulty Level: Fun for All Skill Levels. Minimum Age: No age restrictions',
 '010000', 10.00, 12, 'https://images.unsplash.com/photo-1552028651-43167575559b?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');


INSERT INTO Reservations
(first_name, last_name, phone_number, reservation_date, reservation_time, num_of_people, activity_id, equipment_id)
VALUES
('Vicki', 'Brown', '07846873376', '2023-11-21', '143000', 1, 1, 1),
('Marnie', 'Hutcheson', '01254443889', '2023-11-22', '093000', 2, 2, 2),
('Sarah', 'Campbell', '07265647890', '2023-11-22', '094500', 1, 7, 7),
('Charlie', 'Brooke', '07425795632', '2023-11-23', '131500', 1, 4, 4),
('Mary', 'Grant', '01254443889', '2023-12-04', '150000', 4, 3, 3),
('Patricia', 'Wilson', '07265647890', '2023-12-20', '100000', 3, 11, 11),
('William', 'Bryant', '07425795632', '2023-11-30', '143000', 1, 12, 12),
('John', 'Smith', '09876543210', '2023-11-15', '120000', 1, 5, 5),
('Emily', 'Johnson', '07654321098', '2023-12-19', '180000', 2, 9, 9),
('Daniel', 'Miller', '03456789012', '2024-01-08', '133000', 2, 6, 6),
('Phillip', 'Owen', '07648395833', '2024-01-03', '150000', 3, 8, 8),
('Robert', 'Baker', '07537883647', '2023-11-30', '190000', 2, 10, 10),
('Andrew', 'Ross', '07539760032', '2023-11-29', '113000', 4, 1, 1),
('Rachel', 'Livingston', '07539097861', '2023-12-05', '153000', 2, 2, 2),
('Emma', 'Harris', '07022893756', '2023-11-28', '140000', 4, 5, 5);


CREATE VIEW vw_reservations_by_activity AS
SELECT r.reservation_id,
	   r.first_name,
       r.last_name,
       r.phone_number,
       r.reservation_date,
       r.reservation_time,
       r.num_of_people,
       r.activity_id,
       r.equipment_id,
       a.activity_name
FROM
	   Reservations r
       JOIN Activities a ON r.activity_id = a.activity_id;

CREATE VIEW vw_equipment_for_activity AS
SELECT a.activity_name,
	   e.equipment_name,
	   e.Whats_included
FROM
	   Activities a
       JOIN Equipment e ON a.equipment_id = e.equipment_id;

UPDATE Activities
SET activity_name = 'Outdoor Tennis'
WHERE activity_id = 4;