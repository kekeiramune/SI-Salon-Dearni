from app.config.Database import mysql

def get_all_reservasi():
    cursor = mysql.connection.cursor()
    query = """
        SELECT 
        r.id_reservasi, r.id_customer, c.nama_customer, 
        r.tanggal_reservasi, r.jam_reservasi, l.nama_layanan,
        s.nama_staff, r.status
        FROM reservasi r
        JOIN customer c ON r.id_customer = c.id_customer
        JOIN staff s ON r.id_staff = s.id_staff
        JOIN layanan l ON r.id_layanan = l.id_layanan
    """
    cursor.execute(query)
    reservasi = cursor.fetchall()
    cursor.close()
    return reservasi


def get_reservasi_by_id(id_reservasi):
    cursor = mysql.connection.cursor()
    query = """
        SELECT 
            r.id_reservasi, r.id_customer, c.nama_customer, 
            r.tanggal_reservasi, r.jam_reservasi, r.id_layanan, r.id_staff, r.status
        FROM reservasi r
        JOIN customer c ON r.id_customer = c.id_customer
        WHERE r.id_reservasi = %s
    """
    cursor.execute(query, (id_reservasi,))
    reservasi = cursor.fetchone()
    cursor.close()
    return reservasi


def insert_reservasi(id_customer, tanggal_reservasi, jam_reservasi, id_layanan, id_staff, status):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO reservasi (id_customer, tanggal_reservasi, jam_reservasi, id_layanan, id_staff, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (id_customer, tanggal_reservasi, jam_reservasi, id_layanan, id_staff, status))
    mysql.connection.commit()
    id_reservasi = cursor.lastrowid
    cursor.close()
    return id_reservasi

def update_reservasi(id_customer, tanggal_reservasi, jam_reservasi, id_layanan, id_staff, status, id_reservasi):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE reservasi
        SET id_customer=%s, tanggal_reservasi=%s, jam_reservasi=%s, id_layanan=%s, id_staff=%s, status=%s
        WHERE id_reservasi=%s
    """, (id_customer, tanggal_reservasi, jam_reservasi, id_layanan, id_staff, status, id_reservasi))
    mysql.connection.commit()
    cursor.close()
    return True



def delete_reservasi(id_reservasi):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM reservasi WHERE id_reservasi=%s", (id_reservasi,))
    mysql.connection.commit()
    cursor.close()
    return True
