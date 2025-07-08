from app.config.Database import mysql
from datetime import date

# --- READ All Absensi ---
def get_all_absensi(id_staff=None, is_owner=False):
    try:
        cursor = mysql.connection.cursor()
        if is_owner:
            query = """
                SELECT a.id_absensi, a.id_staff, s.nama_staff, a.tanggal, 
                       a.jam_masuk, a.jam_keluar, a.status, a.keterangan
                FROM absensi a
                JOIN staff s ON a.id_staff = s.id_staff
            """
            cursor.execute(query)
        else:
            query = """
                SELECT a.id_absensi, a.id_staff, s.nama_staff, a.tanggal, 
                       a.jam_masuk, a.jam_keluar, a.status, a.keterangan
                FROM absensi a
                JOIN staff s ON a.id_staff = s.id_staff
                WHERE a.id_staff = %s
            """
            cursor.execute(query, (id_staff,))
        absens = cursor.fetchall()
        cursor.close()
        return absens
    except Exception as e:
        print("Error fetching absensi:", str(e))
        return None





# --- READ absensi by ID ---
def get_absensi_by_id(id_absensi: int):
    try:
        cursor = mysql.connection.cursor()
        query = """
            SELECT 
                a.id_absensi, a.id_staff, s.nama_staff, a.tanggal, 
                a.jam_masuk, a.jam_keluar, a.status, a.keterangan
            FROM absensi a
            JOIN staff s ON a.id_staff = s.id_staff
            WHERE a.id_absensi = %s
        """
        cursor.execute(query, (id_absensi,))
        absens = cursor.fetchone()
        cursor.close()
        return absens
    except Exception as e:
        print(f"Error fetching absensi by ID {id_absensi}: {e}")
        return None

#Create absensi
def create_absensi(id_staff: int, tanggal: date, jam_masuk: str, jam_keluar: str, status: str, keterangan: str):
    """
    Menambahkan absensi baru ke database.

    Args:
        id_staff (int): ID Staff.
        tanggal (date): Tanggal absensi (YYYY-MM-DD).
        jam_masuk (str): Jam masuk absensi (HH:MM:SS).
        jam_keluar (str): Jam keluar absensi (HH:MM:SS).
        status (str): Status kehadiran.
        keterangan (str): Keterangan tambahan.

    Returns:
        int | None: ID absensi yang baru dibuat jika berhasil, None jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        query = """
            INSERT INTO absensi (id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan))
        mysql.connection.commit()
        new_absen_id = cursor.lastrowid
        cursor.close()
        print(f"Absensi berhasil dibuat dengan ID: {new_absen_id}")
        return new_absen_id
    except Exception as e:
        print(f"Error creating absensi: {e}")
        mysql.connection.rollback()
        return None
    
# Ini buat update nya
def update_absensi(id_absensi: int, id_staff: int, tanggal: date, jam_masuk: str, jam_keluar: str, status: str, keterangan: str):
    """
    Memperbarui informasi absensi di database.

    Args:
        id_absensi (int): ID absensi yang akan diperbarui.
        id_staff (int): ID staff.
        tanggal (date): Tanggal absensi baru (YYYY-MM-DD).
        jam_masuk (str): Jam masuk baru (HH:MM:SS).
        jam_keluar (str): Jam keluar baru (HH:MM:SS).
        status (str): Status kehadiran baru.
        keterangan (str): Keterangan tambahan baru.

    Returns:
        bool: True jika berhasil diperbarui, False jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        query = """
            UPDATE absensi
            SET id_staff = %s, tanggal = %s, jam_masuk = %s, jam_keluar = %s, status = %s, keterangan = %s
            WHERE id_absensi = %s
        """
        cursor.execute(query, (id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan, id_absensi))
        mysql.connection.commit()

        updated = cursor.rowcount > 0
        cursor.close()

        if updated:
            print(f"Absensi ID {id_absensi} updated successfully.")
        else:
            print(f"Tidak ada absensi dengan ID {id_absensi} yang ditemukan.")

        return updated

    except Exception as e:
        mysql.connection.rollback()
        print(f"Error updating absensi ID {id_absensi}: {e}")
        return False

def delete_absensi(id_absensi: int):
    """
    Menghapus absensi dari database berdasarkan ID.

    Args:
        id_absensi (int): ID absensi yang akan dihapus.

    Returns:
        bool: True jika berhasil dihapus, False jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        query = "DELETE FROM absensi WHERE id_absensi = %s"
        cursor.execute(query, (id_absensi,))
        mysql.connection.commit()
        if cursor.rowcount > 0:
            print(f"Absensi ID {id_absensi} deleted successfully.")
            return True
        else:
            print(f"No staff found with ID {id_absensi} to delete.")
            return False # Staff dengan ID tersebut tidak ditemukan
        cursor.close()
    except Exception as e:
        mysql.connection.rollback()
        print(f"Error deleting absensi ID {id_absensi}: {e}")
        return False