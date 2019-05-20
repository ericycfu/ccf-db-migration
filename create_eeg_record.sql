DROP TABLE IF EXISTS arch_eeg_record;
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