create table Office
       (office_name		varchar(25),
       	office_city		varchar(25),
	office_sqft		numeric(10,0) check (office_sqft > 0),
	primary key (office_name)
	);

create table AgencyLocation
       (agency_city             varchar(25),
        agency_address          varchar(100),
        primary key (agency_city)
        );


create table CustomerAgencies
       (agency_id		varchar(8),
       	agency_name		varchar(25),
	agency_city		varchar(25),
	phonenumber		varchar(10),
	primary key (agency_id),
	foreign key (agency_city) references AgencyLocation
		on delete cascade
	);

create table RentalAgreement
       (rental_id		varchar(8),
        rentamount		numeric(10,0) check (rentamount > 0),
	enddate			varchar(8),
	primary key (rental_id)
	);

create table Manage
       (manage_id		varchar(8),
        office_name		varchar(25),
	agency_id		varchar(8),
	rental_id		varchar(8),
	primary key (manage_id),
	foreign key (office_name) references Office(office_name),
	foreign key (agency_id) references CustomerAgencies(agency_id),
	foreign key (rental_id) references RentalAgreement(rental_id)
	);