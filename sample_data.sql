delete from Office;
delete from CustomerAgencies;
delete from AgencyLocation;
delete from RentalAgreement;
delete from Manage;
insert into Office values ('Alpha', 'Gaithersburg', '1000');
insert into Office values ('Bravo', 'Baltimore', '1500');
insert into Office values ('Charlie', 'Rockville', '2000');
insert into Office values ('Delta', 'Baltimore', '2500');
insert into Office values ('Echo', 'Hagerstown', '3000');

insert into AgencyLocation values ('Annapolis', '12345 Wyatt Drive, Annapolis MD 21586');
insert into AgencyLocation values ('Baltimore', '23456 Wyatt Lane, Baltimore MD 25498');
insert into AgencyLocation values ('Fredrick', '34567 Blue Circle, Fredrick MD 27895');
insert into AgencyLocation values ('Silver Spring', '45678 Red Drive, Silver Spring MD 45876');
insert into AgencyLocation values ('Ocean City', '56789 Cheese Lane, Ocean City MD 75868');

insert into CustomerAgencies values ('11111', 'Foxtrot', 'Annapolis', '1111111111');
insert into CustomerAgencies values ('22222', 'Golf', 'Baltimore', '2222222222');
insert into CustomerAgencies values ('33333', 'Hotel', 'Fredrick', '3333333333');
insert into CustomerAgencies values ('44444', 'India', 'Silver Spring', '4444444444');
insert into CustomerAgencies values ('55555', 'Julie', 'Ocean City', '5555555555');

insert into RentalAgreement values ('66666', '500', '1282017');
insert into RentalAgreement values ('77777', '600', '1172017');
insert into RentalAgreement values ('88888', '700', '1062017');
insert into RentalAgreement values ('99999', '800', '9142017');
insert into RentalAgreement values ('00001', '900', '7152017');
insert into Manage values ('00100', 'Alpha', '11111', '66666');
insert into Manage values ('00200', 'Bravo', '22222', '77777');
insert into Manage values ('00300', 'Charlie', '33333', '88888');
insert into Manage values ('00400', 'Delta', '44444', '99999');
insert into Manage values ('00500', 'Echo', '55555', '00001');


