from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'salon_dearni'

mysql = MySQL(app)

status_choices = ['Hadir', 'Izin', 'Alpa']

@app.route('/')
def home() :
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        id_staff = request.form['id_staff']
        tanggal = request.form['tanggal']
        jam_masuk = request.form['jam_masuk']
        jam_keluar = request.form['jam_keluar']
        status = request.form['status']  # Ambil status dari form
        keterangan = request.form['keterangan']

        # Simpan data ke database (pastikan kolom status ada)
        cur.execute("""
            INSERT INTO absensi (id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_staff, tanggal, jam_masuk, jam_keluar, status, keterangan))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    # Ambil data staff untuk dropdown
    cur.execute("SELECT id_staff, nama_staff FROM staff")
    staff_list = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("""
    SELECT a.id_absensi, a.id_staff, s.nama_staff, a.tanggal, a.jam_masuk, a.jam_keluar, a.status, a.keterangan
    FROM absensi a
    JOIN staff s ON a.id_staff = s.id_staff
                """)
    data_absen = cur.fetchall()
    cur.close()


    return render_template('absen.html', staff_list=staff_list, status_choices=status_choices, absen=data_absen)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
