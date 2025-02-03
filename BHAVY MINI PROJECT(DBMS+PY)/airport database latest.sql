create database airport;
USE airport;
 
CREATE TABLE employee(
e_id INT PRIMARY KEY,
e_name VARCHAR(60),
e_sal INT,
e_exp INT
);

INSERT INTO employee values (01,'bhavy',50000,5),(02,'jenish',60000,6);

CREATE TABLE flight(
f_no INT PRIMARY KEY,
f_company VARCHAR(60)
);
insert into flight values (106,'AirIndia'),(110,'AirDubai'),(103,'Emirates');

CREATE TABLE ticket(
t_no INT PRIMARY KEY,
t_source VARCHAR(60),
t_des VARCHAR(60),
t_date DATE	
);
ALTER TABLE ticket ADD c_id INT;
ALTER TABLE ticket ADD FOREIGN KEY (c_id) REFERENCES customer(c_id);
ALTER TABLE ticket ADD f_no INT;
ALTER TABLE ticket ADD FOREIGN KEY (f_no) REFERENCES flight(f_no);


CREATE TABLE customer(
c_id INT PRIMARY KEY,
c_name VARCHAR(50),
c_dob INT,
e_id INT,
FOREIGN KEY (e_id) REFERENCES employee(e_id)
);
insert into customer values (10,'om',2000,01);

CREATE TABLE emplogin(
e_id INT,
FOREIGN KEY (e_id) REFERENCES employee(e_id),
e_pass varchar(20)
);
insert into emplogin values (01,'bhavy20');

CREATE TABLE custlogin(
c_id INT,
FOREIGN KEY (c_id) REFERENCES customer(c_id),
c_pass varchar(20)
);
insert into custlogin values (10,'om10');

select * from flight;
select * from customer;
select * from custlogin;
select * from emplogin;
select * from ticket;
desc Employee;
desc Customer;

