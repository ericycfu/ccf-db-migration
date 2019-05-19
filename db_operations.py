
def exec_operation(conn, query, tup):
	cursor = conn.cursor()
	cursor.execute(query, tup)
	conn.commit()
	cursor.close()



def insert_patient(conn, patientid, first_name, last_name, middle_init = None):
	tup = (patientid, first_name, last_name, middle_init)
	query = "INSERT INTO arch_patient VALUES (?, ?, ?, ?)"
	exec_operation(conn, query, tup)

def insert_study(conn, study_id, patient_id, media_label = None, completed_date= None, mtg_size= None):
	tup = (study_id, patient_id, media_label, completed_date, mtg_size)
	query = "INSERT INTO arch_study VALUES (?, ?, ?, ?, ?)"
	exec_operation(conn, query, tup)

def insert_eeg_record(conn, study_id, patient_id, rec_name, media_label, k_cksum = None,
	b_cksum = None, l_cksum = None, m_cksum = None, s_cksum = None, o_cksum = None,
	size_in_sec = None, size_in_byte = None, rec_label = None, comment = None):
	tup = (study_id, patient_id, rec_name, media_label, k_cksum, b_cksum, l_cksum, m_cksum, s_cksum,
	o_cksum, size_in_sec, size_in_byte, rec_label, comment)
	query = "INSERT INTO arch_eeg_record VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
	exec_operation(conn, query, tup)

def insert_media(conn, media_label, media_index, archived_date = None, media_type = None, media_name = None,
	media_capacity = None, used_size = None, number_copies = None):
	tup = (media_label, media_index, archived_date, media_type, media_name, media_capacity, used_size, number_copies)
	exec_operation(conn, query, tup)

def insert_media_detail(conn, media_label, volume_no, desc= None, study_id= None):
	tup = (media_label, volume_no, desc, study_id)
	exec_operation(conn, query, tup)

def insert_video_record(conn, study_id, patient_id, vid_name, media_label, video_size = None, start_time = None,
	end_time = None, v_cksum = None)
