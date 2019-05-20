DROP TABLE IF EXISTS arch_video_record;
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
