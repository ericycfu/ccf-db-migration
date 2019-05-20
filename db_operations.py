
def exec_operation(conn, query, tup):
	cursor = conn.cursor(buffered = True)
	cursor.execute(query, tup)
	conn.commit()
	cursor.close()



def insert_patient(conn, patientid, first_name, last_name, middle_init = None):
	tup = (patientid, first_name, last_name, middle_init)
	query = "INSERT INTO arch_patient VALUES (%s, %s, %s, %s)"
	exec_operation(conn, query, tup)

def insert_study(conn, study_id, patient_id, media_label = None, completed_date= None, mtg_size= None):
	if (not (mtg_size is None)):
		mtg_size = int(mtg_size)
	#maybe also conver timestamp of completed date
	tup = (study_id, patient_id, media_label, completed_date, mtg_size)
	query = "INSERT INTO arch_study VALUES (%s, %s, %s, %s, %s)"
	exec_operation(conn, query, tup)

def insert_eeg_record(conn, study_id, patient_id, rec_name, media_label, k_cksum = None,
	b_cksum = None, l_cksum = None, m_cksum = None, s_cksum = None, o_cksum = None,
	size_in_sec = None, size_in_byte = None, rec_label = None, comment = None):
	size_in_sec = int(size_in_sec)
	size_in_byte = int(size_in_byte)
	tup = (study_id, patient_id, rec_name, media_label, k_cksum, b_cksum, l_cksum, m_cksum, s_cksum,
	o_cksum, size_in_sec, size_in_byte, rec_label, comment)
	query = "INSERT INTO arch_eeg_record VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	exec_operation(conn, query, tup)

def insert_media(conn, media_label, media_index, archived_date = None, media_type = None, media_name = None,
	media_capacity = None, used_size = None, number_copies = None):
	media_capacity = int(media_capacity)
	media_index = int(media_index)
	used_size = float(used_size)
	#timestamp archived date
	#number_copies tinyint
	if (not(number_copies is None)):
		number_copies = int(number_copies)
	tup = (media_label, media_index, archived_date, media_type, media_name, media_capacity, used_size, number_copies)
	query = "INSERT INTO arch_media VALUES (%s, %s,%s, %s, %s, %s, %s, %s)"
	exec_operation(conn, query, tup)

def insert_media_detail(conn, media_label, volume_no, desc= None, study_id= None):
	tup = (media_label, volume_no, desc, study_id)
	#volume_no smallint ???
	volume_no = int(volume_no)
	query = "INSERT INTO arch_media_detail VALUES (%s, %s, %s, %s)"
	exec_operation(conn, query, tup)

def insert_video_record(conn, study_id, patient_id, vid_name, media_label, video_size = None, start_time = None,
	end_time = None, v_cksum = None):
	video_size = int(video_size)
	#timestamp start_time and end_time
	tup = (study_id, patient_id, vid_name, media_label, video_size , start_time,
	end_time, v_cksum)
	query = "INSERT INTO arch_video_record VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	exec_operation(conn, query, tup)
