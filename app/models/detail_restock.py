from app.config.Database import mysql

def get_detail_by_restock(id_restock):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT dr.*, p.nama_produk 
        FROM detail_restock dr
        JOIN produk p ON dr.id_produk = p.id_produk
        WHERE dr.id_restock=%s
    """, (id_restock,))
    result = cursor.fetchall()
    cursor.close()
    return result

def insert_detail(id_restock, id_produk, jumlah, harga_satuan):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO detail_restock (id_restock, id_produk, jumlah, harga_satuan)
        VALUES (%s, %s, %s, %s)
    """, (id_restock, id_produk, jumlah, harga_satuan))
    mysql.connection.commit()
    cursor.close()
    return True


def delete_detail(id_detail_restock):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM detail_restock WHERE id_detail_restock=%s", (id_detail_restock,))
    mysql.connection.commit()
    cursor.close()
    return True
