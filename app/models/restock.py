from app.config.Database import mysql

def get_all_restock():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM restock_produk")
    result = cursor.fetchall()
    cursor.close()
    return result

def get_restock_by_id(id_restock):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM restock_produk WHERE id_restock=%s", (id_restock,))
    result = cursor.fetchone()
    cursor.close()
    return result

def insert_restock(tanggal_restock, total_biaya, status, id_staff):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO restock_produk (tanggal_restock, total_biaya, status, id_staff)
        VALUES (%s, %s, %s, %s)
    """, (tanggal_restock, total_biaya, status, id_staff))
    mysql.connection.commit()
    id_restock = cursor.lastrowid
    cursor.close()
    return id_restock

def update_restock(id_restock, tanggal_restock, total_biaya, status):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE restock_produk 
        SET tanggal_restock=%s, total_biaya=%s, status=%s 
        WHERE id_restock=%s
    """, (tanggal_restock, total_biaya, status, id_restock))
    mysql.connection.commit()
    cursor.close()
    return True

def get_produk_by_restock(id_restock):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_produk FROM restock_produk WHERE id_restock=%s", (id_restock,))
    result = cursor.fetchall()
    cursor.close()
    return result