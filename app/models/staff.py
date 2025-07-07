from app.config.Database import mysql

# --- READ All Staffs ---
def get_all_staffs():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_staff, nama_staff, alamat, no_telp, email, posisi, password FROM staff")
        staffs = cursor.fetchall()  # <-- hasilnya langsung list of dict
        cursor.close()
        return staffs
    except Exception as e:
        print("Error fetching all staffs:", str(e))
        return None



# --- READ Staff by ID ---
def get_staff_by_id(id_staff: int):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_staff, nama_staff, alamat, no_telp, email, posisi, password FROM staff WHERE id_staff = %s", (id_staff,))
        staff = cursor.fetchone()  # <-- langsung dict kalau config-nya benar
        cursor.close()
        return staff
    except Exception as e:
        print(f"Error fetching staff by ID {id_staff}: {e}")
        return None


# --- CREATE Staff ---
def create_staff(nama_staff: str, alamat: str, no_telp: str, email: str, posisi: str):
    """
    Menambahkan staff baru ke database.

    Args:
        nama_staff (str): Nama lengkap staff.
        alamat (str): Alamat staff.
        no_telp (str): Nomor telepon staff.
        email (str): Alamat email staff.
        posisi (str): Posisi/jabatan staff.

    Returns:
        int/None: ID staff yang baru dibuat jika berhasil, None jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        # Sesuaikan nama tabel dan kolom dengan database Anda
        query = """
            INSERT INTO staff (nama_staff, alamat, no_telp, email, posisi)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nama_staff, alamat, no_telp, email, posisi))
        mysql.connection.commit() # Penting: commit perubahan
        new_staff_id = cursor.lastrowid # Mengambil ID terakhir yang dimasukkan
        cursor.close()
        print(f"Staff '{nama_staff}' created with ID: {new_staff_id}")
        return new_staff_id
    except Exception as e:
        print(f"Error creating staff: {e}")
        mysql.connection.rollback() # Gulirkan kembali jika ada kesalahan
        return None

# --- UPDATE Staff ---
def update_staff(id_staff: int, nama_staff: str, alamat: str, no_telp: str, email: str, posisi: str):
    """
    Memperbarui informasi staff di database.

    Args:
        id_staff (int): ID staff yang akan diperbarui.
        nama_staff (str): Nama lengkap staff baru.
        alamat (str): Alamat staff baru.
        no_telp (str): Nomor telepon staff baru.
        email (str): Alamat email staff baru.
        posisi (str): Posisi/jabatan staff baru.

    Returns:
        bool: True jika berhasil diperbarui, False jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        query = """
            UPDATE staff
            SET nama_staff = %s, alamat = %s, no_telp = %s, email = %s, posisi = %s
            WHERE id_staff = %s
        """
        cursor.execute(query, (nama_staff, alamat, no_telp, email, posisi, id_staff))
        mysql.connection.commit()
        # Memeriksa apakah ada baris yang terpengaruh
        if cursor.rowcount > 0:
            print(f"Staff ID {id_staff} updated successfully.")
            return True
        else:
            print(f"No staff found with ID {id_staff} to update.")
            return False # Staff dengan ID tersebut tidak ditemukan
        cursor.close()
    except Exception as e:
        mysql.connection.rollback()
        print(f"Error updating staff ID {id_staff}: {e}")
        return False

# --- DELETE Staff ---
def delete_staff(id_staff: int):
    """
    Menghapus staff dari database berdasarkan ID.

    Args:
        id_staff (int): ID staff yang akan dihapus.

    Returns:
        bool: True jika berhasil dihapus, False jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        query = "DELETE FROM staff WHERE id_staff = %s"
        cursor.execute(query, (id_staff,))
        mysql.connection.commit()
        if cursor.rowcount > 0:
            print(f"Staff ID {id_staff} deleted successfully.")
            return True
        else:
            print(f"No staff found with ID {id_staff} to delete.")
            return False # Staff dengan ID tersebut tidak ditemukan
        cursor.close()
    except Exception as e:
        mysql.connection.rollback()
        print(f"Error deleting staff ID {id_staff}: {e}")
        return False
    

def get_staff_by_email(email):
    try:
        cursor = mysql.connection.cursor() 
        cursor.execute("SELECT * FROM staff WHERE email = %s", (email,))
        staff_data = cursor.fetchone()
        cursor.close()
        return staff_data
    except Exception as e:
        print(f"Error fetching staff by email: {e}")
        return None


    
def get_staff_by_password(password):
    try:
        cursor = mysql.connection.cursor() 
        cursor.execute("SELECT * FROM staff WHERE password = %s", (password,))
        staff_data = cursor.fetchone()
        if staff_data:
            column_names = [desc[0] for desc in cursor.description]
            staff_dict = dict(zip(column_names, staff_data))
            cursor.close()
            return staff_dict
        cursor.close()
        return None
    except Exception as e:
        print(f"Error fetching staff by email: {e}")
        return None