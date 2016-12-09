CREATE TABLE offices (
	name VARCHAR(50) NOT NULL PRIMARY KEY,	
	city VARCHAR(30) NOT NULL,
	sq_footage UNSIGNED SMALL INT NOT NULL
);

CREATE TABLE agencies (
	agency_id  INTEGER NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	address VARCHAR(50) NOT NULL,
	city VARCHAR(30) NOT NULL,
	phone_number VARCHAR(16) NOT NULL
);

CREATE TABLE rental_agreements (
	rental_id INTEGER PRIMARY KEY NOT NULL,
	office_name VARCHAR(50) NOT NULL,
	rental_amount UNSIGNED BIG INT NOT NULL,
	end_date DATE NOT NULL,
	FOREIGN KEY(office_name) REFERENCES offices(name)
);

CREATE TABLE agencies_and_rentals (
	rental_id INTEGER NOT NULL,
	agency_id INTEGER NOT NULL,
	FOREIGN KEY (rental_id) REFERENCES rental_agreements(rental_id),
	FOREIGN KEY (agency_id) REFERENCES agencies(agency_id)
);
