DROP TABLE IF EXISTS arch_media;
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