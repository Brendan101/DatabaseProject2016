create table office
       (office_name		varchar(25),
       	office_city		varchar(25),
	office_sqft		numeric(10,0) check (office_sqft > 0),
	primary key (office_name),
	foreign key (office_name) references Manages
		on delete cascade
	);

create table CustomerAgencies
       (agency_id		varchar(8),
       	agency_name		varchar(25),
	agency_city		varchar(25),
	phonenumber		varchar(10),
	primary key (agency_id),
	foreign key (agency_id) references Manages
		on delete cascade
	);

create table AgencyLocation
       (agency_city		varchar(25),
       	agency_address		varchar(100),
	primary key (agency_city),
	foreign key (agency_city) references CustomerAgencies (agency_city)
		on delete set null
	);

create table RentalAgreement
       (rental_id		varchar(8),
        rentamount		numeric(10,0) check (rentamount > 0),
	enddate			varchar(8),
	primary key (rental_id),
	foreign key (rental_id) references Manage
		on delete cascade
	);

create table Manage
       (manage_id		varchar(8),
        office_name		varchar(25),
	agency_id		varchar(8),
	rental_id		varchar(8),
	primary key (manage_id)
	);