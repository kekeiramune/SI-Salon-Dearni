from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi koneksi ke database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'           # ganti sesuai user MySQL kamu
app.config['MYSQL_PASSWORD'] = ''           # isi jika ada password
app.config['MYSQL_DB'] = 'salon_dearni'         # nama database

mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil data dari form
        id_supplier = request.form['id_supplier']
        nama_supplier = request.form['name']
        alamat = request.form['alamat']
        no_telp = request.form['notelp']
        email = request.form['almemail']

        # Simpan ke database
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO supplier (id_supplier, nama_supplier, alamat, no_telp, email)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_supplier, nama_supplier, alamat, no_telp, email))
        mysql.connection.commit()
        cur.close()


    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM supplier")
    data_sup = cur.fetchall()
    cur.close()

    return render_template('inputsupplier.html', supplier=data_sup)

if __name__ == '__main__':
    app.run(debug=True, port=5001)