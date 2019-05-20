DROP TABLE IF EXISTS arch_patient;
create table arch_patient (
  	patient_id		varchar(25) not null,
	first_name		varchar(25) not null,
	last_name		varchar(25) not null,
	middle_init		varchar(3),

	primary key	(patient_id)
);
