DROP TABLE IF EXISTS arch_media_detail;
create table arch_media_detail (
	media_label		varchar(25) not null,
	volume_no		smallint not null,
	description			varchar(25),
	study_id		varchar(25),

  	foreign key (media_label) references arch_media(media_label),
	primary key (media_label, volume_no)
);