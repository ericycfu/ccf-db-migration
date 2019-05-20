DROP TABLE IF EXISTS arch_patient;
DROP TABLE IF EXISTS arch_study;
DROP TABLE IF EXISTS arch_eeg_record;
DROP TABLE IF EXISTS arch_media;
DROP TABLE IF EXISTS arch_media_detail;
DROP TABLE IF EXISTS arch_video_record;

create table arch_patient (
  	patient_id		varchar(25) not null,
	first_name		varchar(25) not null,
	last_name		varchar(25) not null,
	middle_init		varchar(3),

	primary key	(patient_id)
);

create table arch_study (
	study_id		varchar(25) not null,
	patient_id		varchar(25) not null,
	media_label		varchar(25),
	studyCompleted_date	timestamp,
	mtg_size		integer, 

	foreign key (patient_id) references arch_patient(patient_id), 
	primary key (study_id, patient_id)
);

create table arch_eeg_record (
	study_id		varchar(25) not null,
	patient_id		varchar(25) not null,
	rec_name		varchar(25) not null,
	media_label		varchar(25) not null,
	k_cksum		varchar(64),
	b_cksum		varchar(64),
	l_cksum		varchar(64),
	m_cksum		varchar(64),
	s_cksum		varchar(64),
	o_cksum		varchar(64),
	size_in_sec		integer,
	size_in_byte		integer,
	rec_label		varchar(64),
	comment			varchar(64),

    	foreign key (study_id, patient_id) references 
			arch_study(study_id, patient_id),
	foreign key (media_label) references arch_media(media_label),
	primary key (study_id, rec_name, media_label)
);

create table arch_media (
	media_label		varchar(25) not null unique,
	media_index		integer not null,
	archived_date		timestamp,
	media_type		varchar(25),
	media_name		varchar(25),
	media_capacity		integer,
	used_size		float,
	number_copies		tinyint,

	primary key (media_label)
);

create table arch_media_detail (
	media_label		varchar(25) not null,
	volume_no		smallint not null,
	description			varchar(25),
	study_id		varchar(25),

  	foreign key (media_label) references arch_media(media_label),
	primary key (media_label, volume_no)
);

create table arch_video_record (
	study_id		varchar(25) not null,
	patient_id		varchar(25) not null,
	vid_name		varchar(25) not null,
	media_label		varchar(25) not null,
	video_size		integer,
	start_time		timestamp,
	end_time		timestamp,
	v_cksum		varchar(64),

    	foreign key (study_id, patient_id) references 
			arch_study(study_id, patient_id),
	foreign key (media_label) references arch_media(media_label),
	primary key (study_id, vid_name, media_label)
);
