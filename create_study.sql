DROP TABLE IF EXISTS arch_study;
create table arch_study (
	study_id		varchar(25) not null,
	patient_id		varchar(25) not null,
	media_label		varchar(25),
	studyCompleted_date	timestamp,
	mtg_size		integer, 

	foreign key (patient_id) references arch_patient(patient_id), 
	primary key (study_id, patient_id)
);