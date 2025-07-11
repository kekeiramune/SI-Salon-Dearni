from app.config.Database import mysql

def get_all_transaksi():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT t.*, c.nama_customer
        FROM transaksi_layanan t
        JOIN reservasi r ON t.id_reservasi = r.id_reservasi
        JOIN customer c ON r.id_customer = c.id_customer
    """)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_reservasi_selesai():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT * 
        FROM reservasi 
        WHERE status = 'Selesai'
        AND id_reservasi NOT IN (
            SELECT id_reservasi FROM transaksi_layanan
        )
    """)
    result = cursor.fetchall()
    cursor.close()
    return result


def insert_transaksi(id_reservasi, tanggal_transaksi, total_bayar, metode_pembayaran, status_pembayaran):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO transaksi_layanan 
        (id_reservasi, tanggal_transaksi, total_bayar, metode_pembayaran, status_pembayaran)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_reservasi, tanggal_transaksi, total_bayar, metode_pembayaran, status_pembayaran))
    mysql.connection.commit()
    cursor.close()
    return True

def update_status_pembayaran(id_transaksi, status_baru):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE transaksi_layanan 
        SET status_pembayaran = %s 
        WHERE id_transaksi = %s
    """, (status_baru, id_transaksi))
    mysql.connection.commit()
    cursor.close()
    return True

def get_total_bayar(id_reservasi):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT l.harga_layanan 
        FROM reservasi r 
        JOIN layanan l ON r.id_layanan = l.id_layanan 
        WHERE r.id_reservasi=%s
    """, (id_reservasi,))
    result = cursor.fetchone()
    cursor.close()
    return result['harga_layanan'] if result else 0

from app.config.Database import mysql

def get_status_transaksi(id_transaksi):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT status_pembayaran 
        FROM transaksi_layanan 
        WHERE id_transaksi = %s
    """, (id_transaksi,))
    result = cursor.fetchone()
    cursor.close()
    return result['status_pembayaran'] if result else None
