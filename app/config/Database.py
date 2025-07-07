from flask_mysqldb import MySQL
from flask import Flask
from pymysql.cursors import DictCursor

mysql = MySQL()

def init_db(app: Flask):
    """
    Menginisialisasi objek MySQL dengan konfigurasi aplikasi Flask.
    Fungsi ini akan dipanggil sekali saat aplikasi dimulai.
    """
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '' # Kosongkan jika tidak ada password
    app.config['MYSQL_DB'] = 'salon_dearni'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    mysql.init_app(app) # Menghubungkan objek MySQL dengan aplikasi Flask