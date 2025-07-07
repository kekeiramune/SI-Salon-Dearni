from app.config.Database import mysql

def get_all_produk():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM produk")
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        print("Error:", e)
        return None
    
def get_produk_by_id(id_produk: int):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_produk, id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan FROM produk WHERE id_produk = %s", (id_produk,))
        produk = cursor.fetchone()
        cursor.close()
        return produk
    except Exception as e:
        print(f"Error fetching staff by ID {id_produk}: {e}")
        return None

def insert_produk(id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO produk (id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan))
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error insert produk:", e)
        return False

def delete_produk(id_produk: int):
    """
    Menghapus produk dari database berdasarkan ID.

    Args:
        id_produk (int): ID produk yang akan dihapus.

    Returns:
        bool: True jika berhasil dihapus, False jika gagal.
    """
    try:
        cursor = mysql.connection.cursor()
        query = "DELETE FROM produk WHERE id_produk = %s"
        cursor.execute(query, (id_produk,))
        mysql.connection.commit()
        if cursor.rowcount > 0:
            print(f"Produk ID {id_produk} deleted successfully.")
            return True
        else:
            print(f"No produk found with ID {id_produk} to delete.")
            return False
        cursor.close()
    except Exception as e:
        mysql.connection.rollback()
        print(f"Error deleting produk ID {id_produk}: {e}")
        return False

def update_produk(id_produk, id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE produk SET id_supplier=%s, nama_produk=%s, deskripsi=%s, harga_beli=%s, stok=%s, satuan=%s
            WHERE id_produk=%s
        """, (id_supplier, nama_produk, deskripsi, harga_beli, stok, satuan, id_produk))
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error update produk:", e)
        return False
