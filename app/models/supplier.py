from app.config.Database import mysql

def get_all_supplier():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM supplier")
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        print("Error:", e)
        return None