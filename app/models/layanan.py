from app.config.Database import mysql

def get_all_layanan():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT id_layanan, nama_layanan, deskripsi, harga, durasi_menit, kategori 
            FROM layanan
        """)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        print(f"Error fetching layanan: {e}")
        return []
